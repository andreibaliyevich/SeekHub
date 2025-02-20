<script setup lang="ts">
import { isAxiosError } from 'axios'

definePageMeta({ requiresGuest: true })

const { $axios } = useNuxtApp()
const route = useRoute()
const { t } = useI18n()
const localePath = useLocalePath()

const isLoading = ref(false)
const email = ref('')
const password = ref('')
const confirmPassword = ref('')
const name = ref('')
const birthday = ref('')

const passwordShow = ref(false)
const confirmPasswordShow = ref(false)

const status = ref<number | null>(null)
const errors = ref<Record<string, any>>({})

useHead({
  title: t('pages.register.title')
})

const registration = async () => {
  isLoading.value = true

  let formData = new FormData()
  formData.append('email', email.value)
  formData.append('password', password.value)
  formData.append('confirm_password', confirmPassword.value)
  formData.append('name', name.value)
  formData.append('birthday', birthday.value)

  try {
    const response = await $axios.post('/auth/register', formData)
    status.value = response.status
    errors.value = {}
  } catch (error) {
    status.value = null
    errors.value = {}
    if (isAxiosError(error)) {
      const detail = error.response?.data.detail
      if (Array.isArray(detail)) {
        detail.forEach(e => {
          if (e.msg === 'value is not a valid email address: An email address must have an @-sign.') {
            errors.value.email = t('pages.register.email_valid1')
          } else if (e.msg === 'value is not a valid email address: There must be something after the @-sign.') {
            errors.value.email = t('pages.register.email_valid2')
          } else if (e.msg === 'value is not a valid email address: The part after the @-sign is not valid. It should have a period.') {
            errors.value.email = t('pages.register.email_valid3')
          } else if (e.msg === 'value is not a valid email address: An email address cannot end with a period.') {
            errors.value.email = t('pages.register.email_valid4')
          } else if (e.msg === 'Value error, Password must be at least 8 characters long.') {
            errors.value.password = t('pages.register.password_valid1')
          } else if (e.msg === 'Value error, Password must contain at least one digit.') {
            errors.value.password = t('pages.register.password_valid2')
          } else if (e.msg === 'Value error, Password must contain at least one uppercase letter.') {
            errors.value.password = t('pages.register.password_valid3')
          } else if (e.msg === 'Value error, Password must contain at least one special character (e.g. @, $, !, %, *, ?, &).') {
            errors.value.password = t('pages.register.password_valid4')
          } else if (e.msg === 'Value error, Passwords do not match.') {
            errors.value.confirm_password = t('pages.register.confirm_password_not_match')
          } else if (e.msg === 'Input should be a valid date or datetime, input is too short') {
            errors.value.birthday = t('pages.register.birthday_valid')
          }
        })
      } else if (detail === 'A record with this unique field already exists.') {
        errors.value.email = t('pages.register.email_unique')
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
        {{ $t('pages.register.title') }}
      </h1>

      <v-alert
        v-if="status === 201"
        type="success"
        variant="tonal"
      >
        {{ $t('pages.register.success1') }}<br>
        {{ $t('pages.register.success2') }}<br>
        {{ $t('pages.register.success3') }}
      </v-alert>

      <div v-else>
        <p class="text-body-1 text-secondary mb-5">
          {{ $t('pages.register.have_account') }}
          <NuxtLink
            :to="localePath('/login')"
            class="text-decoration-none"
          >
            {{ $t('pages.register.log_in') }}
          </NuxtLink>
        </p>

        <v-form @submit.prevent="registration">
          <v-text-field
            v-model="email"
            :readonly="isLoading"
            type="email"
            maxlength="254"
            variant="filled"
            :label="$t('user.email')"
            :error-messages="errors.email ?? []"
            :class="{ 'mb-3': !!errors.email }"
          ></v-text-field>
          <v-text-field
            v-model="password"
            :readonly="isLoading"
            :type="passwordShow ? 'text' : 'password'"
            variant="filled"
            :label="$t('user.password')"
            :append-inner-icon="passwordShow ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append-inner="passwordShow = !passwordShow"
            :error-messages="errors.password ?? []"
            :class="{ 'mb-3': !!errors.password }"
          ></v-text-field>
          <v-text-field
            v-model="confirmPassword"
            :readonly="isLoading"
            :type="confirmPasswordShow ? 'text' : 'password'"
            variant="filled"
            :label="$t('user.confirm_password')"
            :append-inner-icon="confirmPasswordShow ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append-inner="confirmPasswordShow = !confirmPasswordShow"
            :error-messages="errors.confirm_password ?? []"
            :class="{ 'mb-3': !!errors.confirm_password }"
          ></v-text-field>
          <v-text-field
            v-model="name"
            :readonly="isLoading"
            type="text"
            variant="filled"
            :label="$t('user.name')"
            :error-messages="errors.name ?? []"
            :class="{ 'mb-3': !!errors.name }"
          ></v-text-field>
          <v-text-field
            v-model="birthday"
            :readonly="isLoading"
            variant="filled"
            type="date"
            :label="$t('user.birthday')"
            :error-messages="errors.birthday ?? []"
            :class="{ 'mb-3': !!errors.birthday }"
          ></v-text-field>
          <v-btn
            :loading="isLoading"
            :disabled="
              !email ||
              !password ||
              !confirmPassword ||
              !name ||
              !birthday
            "
            type="submit"
            variant="flat"
            color="primary"
            size="x-large"
            block
          >
            {{ $t('pages.register.register') }}
          </v-btn>
        </v-form>

        <v-divider class="my-3"></v-divider>
        <p class="text-body-1 text-secondary">
          {{ $t('pages.register.help') }}
        </p>
      </div>
    </v-sheet>
  </div>
</template>
