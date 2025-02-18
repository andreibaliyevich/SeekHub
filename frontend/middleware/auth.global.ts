export default defineNuxtRouteMiddleware(async (to, from) => {
  const { $axios } = useNuxtApp()
  const localePath = useLocalePath()
  const userStore = useUserStore()
  const accessToken = useCookie('accessToken')
  const tokenType = useCookie('tokenType')

  if (!tokenType.value || !accessToken.value) {
    userStore.resetUserData()
    if (to.meta.requiresAuth) {
      return navigateTo({
        path: localePath('/login'),
        query: { redirect: to.fullPath }
      })
    }
    return
  }

  if (userStore.isLoggedIn) {
    if (to.meta.requiresGuest) {
      return navigateTo(localePath('/'), { replace: true })
    }
    return
  }

  const getUser = async () => {
    try {
      const response = await $axios.get('/auth/user', {
        headers: {
          Authorization: `${tokenType.value} ${accessToken.value}`
        }
      })
      const fileUrl = response.data.photos[0]?.file_url
      userStore.setUserData({
        id: response.data.id,
        email: response.data.email,
        name: response.data.name,
        is_verified: response.data.is_verified,
        primary_photo: fileUrl ?? null
      })
    } catch (error) {
      userStore.resetUserData()
      console.error(error)
    }
    return userStore.isLoggedIn
  }

  const userIsLoggedIn = await getUser()

  if (to.meta.requiresAuth && !userIsLoggedIn) {
    return navigateTo({
      path: localePath('/login'),
      query: { redirect: to.fullPath }
    })
  }

  if (to.meta.requiresGuest && userIsLoggedIn) {
    return navigateTo(localePath('/'), { replace: true })
  }
})
