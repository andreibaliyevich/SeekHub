<script setup lang="ts">
import { isAxiosError } from 'axios'
import type { Photo } from '@/types/photo'

definePageMeta({ requiresAuth: true })

const { $axios } = useNuxtApp()
const { t } = useI18n()
const userStore = useUserStore()

useHead({
  title: t('pages.profile.title')
})

const isLoadingProfile = ref(true)
const isUpdatingProfile = ref(false)

const id = ref('')
const email = ref('')
const dateJoined = ref('')
const name = ref('')
const birthday = ref('')
const isVerified = ref(false)
const gender = ref<string | null>(null)
const heading = ref<string | null>(null)
const city = ref<object | null>(null)
const height = ref<number | null>(null)
const bodyType = ref<string | null>(null)
const ethnicity = ref<number | null>(null)
const relationshipStatus = ref<string | null>(null)
const children = ref(0)
const drink = ref<string | null>(null)
const smoke = ref<string | null>(null)
const education = ref<string | null>(null)
const occupation = ref<string | null>(null)
const annualIncome = ref<string | null>(null)
const netWorth = ref<string | null>(null)
const about = ref('')
const genderPreference = ref<string | null>(null)
const agePreferenceMin = ref<number | null>(null)
const agePreferenceMax = ref<number | null>(null)
const seekingTags = ref<string[]>([])
const photos = ref<Photo[]>([])

const errors = ref<Record<string, any>>({})

const getUserProfile = async () => {
  try {
    const response = await $axios.get('/auth/profile')
    id.value = response.data.id
    email.value = response.data.email
    dateJoined.value = response.data.date_joined
    name.value = response.data.name
    birthday.value = response.data.birthday
    isVerified.value = response.data.is_verified
    gender.value = response.data.profile.gender
    heading.value = response.data.profile.heading
    city.value = response.data.profile.city
    height.value = response.data.profile.height
    bodyType.value = response.data.profile.body_type
    ethnicity.value = response.data.profile.ethnicity
    relationshipStatus.value = response.data.profile.relationship_status
    children.value = response.data.profile.children
    drink.value = response.data.profile.drink
    smoke.value = response.data.profile.smoke
    education.value = response.data.profile.education
    occupation.value = response.data.profile.occupation
    annualIncome.value = response.data.profile.annual_income
    netWorth.value = response.data.profile.net_worth
    about.value = response.data.profile.about
    genderPreference.value = response.data.profile.gender_preference
    agePreferenceMin.value = response.data.profile.age_preference_min
    agePreferenceMax.value = response.data.profile.age_preference_max
    seekingTags.value = response.data.profile.seeking_tags
    photos.value = response.data.photos
  } catch (error) {
    if (isAxiosError(error)) {
      errors.value = {
        status: error.response?.status,
        detail: error.response?.data.detail
      }
    } else {
      console.error('Unexpected error:', error)
    }
  } finally {
    isLoadingProfile.value = false
  }
}

const updateUserProfile = async () => {
  isUpdatingProfile.value = true
  try {
    const response = await $axios.put('/auth/profile-update', {
      name: name.value,
      birthday: birthday.value,
      profile: {
        gender: gender.value,
        heading: heading.value,
        city_id: "1fe9e17b-b2f6-439a-b7c2-6ef76c1127a6",
        height: height.value,
        body_type: bodyType.value,
        ethnicity: ethnicity.value,
        relationship_status: relationshipStatus.value,
        children: children.value,
        drink: drink.value,
        smoke: smoke.value,
        education: education.value,
        occupation: occupation.value,
        annual_income: annualIncome.value,
        net_worth: netWorth.value,
        about: about.value,
        gender_preference: genderPreference.value,
        age_preference_min: agePreferenceMin.value,
        age_preference_max: agePreferenceMax.value,
        seeking_tags: seekingTags.value
      }
    })
    errors.value = {}
  } catch (error) {
    if (isAxiosError(error)) {
      errors.value = {
        status: error.response?.status,
        detail: error.response?.data.detail
      }
    } else {
      console.error('Unexpected error:', error)
    }
  } finally {
    isUpdatingProfile.value = false
  }
}

const uploadPhoto = (photo: Photo) => {
  photos.value.push(photo)
}

const updatePhotoPublic = (id: string, value: boolean) => {
  const photoIndex = photos.value.findIndex((element) => element.id === id)
  if (photoIndex !== -1) {
    photos.value[photoIndex].is_public = value
  }
}

const updatePhotoPrimary = (id: string, value: boolean) => {
  photos.value.forEach((element) => {
    element.is_primary = false
  })
  const photoIndex = photos.value.findIndex((element) => element.id === id)
  if (photoIndex !== -1) {
    photos.value[photoIndex].is_primary = value
  }
  if (value) {
    userStore.updatePhoto(photos.value[photoIndex].file_url)
  } else {
    userStore.updatePhoto(null)
  }
}

const deletePhoto = (id: string, isPrimary: boolean) => {
  photos.value = photos.value.filter((element) => element.id !== id)
  if (isPrimary) {
    userStore.updatePhoto(null)
  }
}

onMounted(() => {
  getUserProfile()
})
</script>

<template>
  <v-container>
    <div
      v-if="isLoadingProfile"
      class="d-flex justify-center"
    >
      <v-progress-circular
        indeterminate
        :size="50"
      ></v-progress-circular>
    </div>
    <v-row v-else>
      <v-col
        :cols="12"
        :sm="4"
      >
        <UserPhotos
          :photos="photos"
          @uploadPhoto="uploadPhoto"
          @updatePhotoPublic="updatePhotoPublic"
          @updatePhotoPrimary="updatePhotoPrimary"
          @deletePhoto="deletePhoto"
        />
      </v-col>
      <v-col
        :cols="12"
        :sm="8"
      >
        <v-form @submit.prevent="updateUserProfile">
          <v-text-field
            v-model="name"
            :readonly="isUpdatingProfile"
            type="text"
            maxlength="64"
            variant="filled"
            :label="$t('pages.profile.name')"
            :error-messages="errors?.detail?.name ?? []"
          ></v-text-field>
          <v-text-field
            v-model="birthday"
            :readonly="isUpdatingProfile"
            variant="filled"
            type="date"
            :label="$t('pages.profile.birthday')"
            :error-messages="errors?.detail?.birthday ?? []"
          ></v-text-field>
          <v-btn
            :loading="isUpdatingProfile"
            type="submit"
            variant="flat"
            color="primary"
            size="x-large"
            class="text-none"
          >
            {{ $t('pages.profile.update_profile') }}
          </v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>
