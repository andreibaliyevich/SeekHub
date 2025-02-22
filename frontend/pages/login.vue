<script setup lang="ts">
import { isAxiosError } from 'axios'

const { $axios } = useNuxtApp()
const route = useRoute()
const { t } = useI18n()
const localePath = useLocalePath()

definePageMeta({ requiresGuest: true })
useHead({
  title: t('pages.login.title')
})

const isLoading = ref(false)
const username = ref('')
const password = ref('')
const passwordShow = ref(false)

const rspErrors = ref<Record<string, any>>({})

const login = async () => {
  isLoading.value = true

  let formData = new FormData()
  formData.append('username', username.value)
  formData.append('password', password.value)

  try {
    const { data } = await $axios.post('/auth/token', formData)

    useCookie('accessToken').value = data.access_token
    useCookie('refreshToken').value = data.refresh_token
    useCookie('tokenType').value = data.token_type

    rspErrors.value = {}

    const redirectPath = Array.isArray(route.query.redirect)
      ? route.query.redirect[0]
      : route.query.redirect
    return navigateTo(redirectPath || localePath('/'), { replace: true })
  } catch (error) {
    if (isAxiosError(error)) {
      rspErrors.value = {
        status: error.response?.status,
        detail: error.response?.data.detail
      }
    } else {
      console.error('Unexpected error:', error)
    }
  } finally {
    isLoading.value = false
  }
}
</script>

<template>
  <div
    class="d-flex align-center justify-center"
    style="min-height: 80vh;"
  >
    <v-sheet
      min-width="375"
      max-width="500"
      rounded="lg"
      elevation="10"
      class="pa-8"
    >
      <h1 class="text-h4 text-md-h3 text-center mb-4">
        {{ $t('pages.login.title') }}
      </h1>

      <v-alert
        v-if="
          rspErrors?.status === 401 &&
          rspErrors?.detail === 'Invalid username or password.'
        "
        :text="$t('pages.login.error')"
        type="error"
        variant="tonal"
      ></v-alert>

      <p class="text-grey-darken-2 mt-3 mb-5">
        {{ $t('pages.login.have_account') }}
        <NuxtLink
          :to="localePath('/register')"
          class="text-decoration-none"
        >
          {{ $t('pages.login.register') }}
        </NuxtLink>
      </p>

      <v-form @submit.prevent="login">
        <v-text-field
          v-model="username"
          :readonly="isLoading"
          type="email"
          maxlength="254"
          variant="filled"
          :label="$t('user.email')"
        ></v-text-field>
        <v-text-field
          v-model="password"
          :readonly="isLoading"
          :type="passwordShow ? 'text' : 'password'"
          variant="filled"
          :label="$t('user.password')"
          :append-inner-icon="passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
          @click:appendInner="passwordShow = !passwordShow"
        ></v-text-field>
        <v-btn
          :loading="isLoading"
          :disabled="!username || !password"
          type="submit"
          variant="flat"
          color="primary"
          size="x-large"
          block
        >
          {{ $t('pages.login.log_in') }}
        </v-btn>
      </v-form>

      <v-divider class="my-5"></v-divider>

      <p class="text-grey-darken-2">
        {{ $t('pages.login.forgot_your_password') }}
        <NuxtLink
          :to="localePath('/')"
          class="text-decoration-none"
        >
          {{ $t('pages.login.reset_password') }}
        </NuxtLink>
      </p>
    </v-sheet>
  </div>
</template>
