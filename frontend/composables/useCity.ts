import type { City } from '~/types/city'

export const useCity = () => {
  const { $axios } = useNuxtApp()

  const cityId = ref<string | null>(null)
  const cityOptions = ref<{ value: string; title: string }[]>([])
  const isLoadingCity = ref(false)

  const setUserCity = (city: City) => {
    cityId.value = city.id
    cityOptions.value.push({
      value: city.id,
      title: `${city.name}, ${city.country}, ${city.region}`
    })
  }

  const citySearch = async (value: string | null) => {
    if (value && value.length >= 3) {
      const isMatchFound = cityOptions.value.some(item => item.title === value)
      if (!isMatchFound) {
        isLoadingCity.value = true
        try {
          const { data } = await $axios.get('/cities/search', {
            params: { query: value }
          })
          if (Array.isArray(data)) {
            cityId.value = null
            cityOptions.value.length = 0
            data.forEach((item) => {
              cityOptions.value.push({
                value: item.id,
                title: `${item.name}, ${item.country}, ${item.region}`
              })
            })
          }
        } catch (error) {
          console.error(error)
        } finally {
          isLoadingCity.value = false
        }
      }
    }
  }

  const getCityByLocation = async (event: PointerEvent) => {
    navigator.geolocation.getCurrentPosition(
      async (position) => {
        isLoadingCity.value = true
        const { latitude, longitude } = position.coords
        try {
          const { data } = await $axios.get('/cities/nearest', {
            params: {
              latitude: latitude,
              longitude: longitude
            }
          })
          cityOptions.value.length = 0
          setUserCity(data)
        } catch (error) {
          console.error(error)
        } finally {
          isLoadingCity.value = false
        }
      },
      (error) => {
        console.error(error.message)
      },
      { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
    )
  }

  return {
    cityId,
    cityOptions,
    isLoadingCity,
    setUserCity,
    citySearch,
    getCityByLocation
  }
}
