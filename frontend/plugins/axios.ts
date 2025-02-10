import axios from 'axios'

export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()
  const accessToken = useCookie('accessToken')
  const refreshToken = useCookie('refreshToken')
  const tokenType = useCookie('tokenType')

  const api = axios.create({
    baseURL: config.public.apiBase as string
  })

  api.interceptors.request.use((request) => {
    if (tokenType.value && accessToken.value) {
      request.headers['Authorization'] = `${tokenType.value} ${accessToken.value}`
    }
    return request
  })

  let refreshing = false
  let refreshSubscribers: ((token: string) => void)[] = []

  api.interceptors.response.use(
    (response) => response,
    async (error) => {
      if (
        error.response.status === 401 &&
        error.response.data.detail == 'Invalid credentials.'
      ) {
        if (!refreshToken.value || error.config.url === '/auth/refresh') {
          console.error('Re-login required!')
          logout()
          return Promise.reject(error)
        }
        accessToken.value = null

        if (refreshing) {
          return new Promise((resolve) => {
            refreshSubscribers.push((token) => {
              error.config.headers.Authorization = `${tokenType.value} ${token}`
              resolve(api(error.config))
            })
          })
        }

        refreshing = true
        try {
          const { data } = await api.post('/auth/refresh', { refresh_token: refreshToken.value })
          accessToken.value = data.access_token
          refreshToken.value = data.refresh_token
          tokenType.value = data.token_type

          refreshing = false
          refreshSubscribers.forEach((callback) => callback(data.access_token))
          refreshSubscribers = []

          error.config.headers['Authorization'] = `${data.token_type} ${data.access_token}`
          return api(error.config)
        } catch (refreshError) {
          console.error('Token update error:', refreshError)
          logout()
          return Promise.reject(refreshError)
        }
      }
      return Promise.reject(error)
    }
  )

  function logout() {
    accessToken.value = null
    refreshToken.value = null
    tokenType.value = null
    navigateTo(`/login?redirect=${encodeURIComponent(window.location.pathname)}`)
  }

  return {
    provide: {
      axios: api
    }
  }
})
