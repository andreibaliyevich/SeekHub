interface UserState {
  id: string | null
  email: string | null
  name: string | null
  is_verified: boolean | null
  primary_photo: string | null
}

export const useUserStore = defineStore('userStore', {
  state: (): UserState => {
    return {
      id: null,
      email: null,
      name: null,
      is_verified: null,
      primary_photo: null
    }
  },
  getters: {
    isLoggedIn: (state) => !!state.id
  },
  actions: {
    setUserData(data: UserState) {
      this.$patch(data)
    },
    resetUserData() {
      this.$patch({
        id: null,
        email: null,
        name: null,
        is_verified: null,
        primary_photo: null
      })
    },
    updateEmail(value: string) {
      this.email = value
    },
    updateName(value: string) {
      this.name = value
    },
    updateVerified(value: boolean) {
      this.is_verified = value
    },
    updatePhoto(value: string) {
      this.primary_photo = value
    }
  }
})
