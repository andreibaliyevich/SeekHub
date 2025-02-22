<script setup lang="ts">
import { isAxiosError } from 'axios'
import type {
  GenderType,
  BodyType,
  EthnicityType,
  RelationshipStatus,
  DrinkStatus,
  SmokeStatus,
  EducationLevel,
  OccupationType,
  AnnualIncomeLevel,
  NetWorthLevel,
  SeekingTags
} from '~/types/profile'
import type { Photo } from '~/types/photo'

const { $axios } = useNuxtApp()
const { t } = useI18n()
const userStore = useUserStore()

definePageMeta({ requiresAuth: true })
useHead({
  title: t('pages.profile.title')
})

const isLoadingProfile = ref(true)
const isUpdatingProfile = ref(false)

const dateJoined = ref('')
const name = ref('')
const birthday = ref('')
const isVerified = ref(false)
const gender = ref<GenderType | null>(null)
const heading = ref<string | null>(null)
const height = ref<number | null>(null)
const bodyType = ref<BodyType | null>(null)
const ethnicity = ref<EthnicityType | null>(null)
const relationshipStatus = ref<RelationshipStatus | null>(null)
const children = ref(0)
const drink = ref<DrinkStatus | null>(null)
const smoke = ref<SmokeStatus | null>(null)
const education = ref<EducationLevel | null>(null)
const occupation = ref<OccupationType | null>(null)
const annualIncome = ref<AnnualIncomeLevel | null>(null)
const netWorth = ref<NetWorthLevel | null>(null)
const about = ref('')
const genderPreference = ref<GenderType | null>(null)
const agePreferenceMin = ref(18)
const agePreferenceMax = ref(55)
const seekingTags = ref<SeekingTags[]>([])
const photos = ref<Photo[]>([])

const rspErrors = ref<Record<string, any>>({})

const {
  genderOptions,
  bodyOptions,
  ethnicityOptions,
  relationshipOptions,
  drinkOptions,
  smokeOptions,
  educationOptions,
  occupationOptions,
  annualIncomeOptions,
  netWorthOptions,
  genderPreferenceOptions,
  seekingTagsOptions
} = useProfileOptions()
const {
  cityId,
  cityOptions,
  isLoadingCity,
  setUserCity,
  citySearch,
  getCityByLocation
} = useCity()

const getUserProfile = async () => {
  try {
    const { data } = await $axios.get('/auth/profile')
    dateJoined.value = data.date_joined
    name.value = data.name
    birthday.value = data.birthday
    isVerified.value = data.is_verified
    gender.value = data.profile.gender
    heading.value = data.profile.heading
    if (data.profile.city) setUserCity(data.profile.city)
    height.value = data.profile.height
    bodyType.value = data.profile.body_type
    ethnicity.value = data.profile.ethnicity
    relationshipStatus.value = data.profile.relationship_status
    children.value = data.profile.children
    drink.value = data.profile.drink
    smoke.value = data.profile.smoke
    education.value = data.profile.education
    occupation.value = data.profile.occupation
    annualIncome.value = data.profile.annual_income
    netWorth.value = data.profile.net_worth
    about.value = data.profile.about
    genderPreference.value = data.profile.gender_preference
    if (data.profile.age_preference_min) {
      agePreferenceMin.value = data.profile.age_preference_min
    }
    if (data.profile.age_preference_max) {
      agePreferenceMax.value = data.profile.age_preference_max
    }
    seekingTags.value = data.profile.seeking_tags
    photos.value = data.photos
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
    isLoadingProfile.value = false
  }
}

const updateUserProfile = async () => {
  isUpdatingProfile.value = true

  const userData: Record<string, any> = {}
  const profile: Record<string, any> = {}

  if (name.value) userData.name = name.value
  if (birthday.value) userData.birthday = birthday.value
  if (gender.value) profile.gender = gender.value
  if (heading.value) profile.heading = heading.value
  if (cityId.value) profile.city_id = cityId.value
  if (height.value) profile.height = height.value
  if (bodyType.value) profile.body_type = bodyType.value
  if (ethnicity.value) profile.ethnicity = ethnicity.value
  if (relationshipStatus.value) profile.relationship_status = relationshipStatus.value
  if (children.value) profile.children = children.value
  if (drink.value) profile.drink = drink.value
  if (smoke.value) profile.smoke = smoke.value
  if (education.value) profile.education = education.value
  if (occupation.value) profile.occupation = occupation.value
  if (annualIncome.value) profile.annual_income = annualIncome.value
  if (netWorth.value) profile.net_worth = netWorth.value
  if (about.value) profile.about = about.value
  if (genderPreference.value) profile.gender_preference = genderPreference.value
  if (agePreferenceMin.value) profile.age_preference_min = agePreferenceMin.value
  if (agePreferenceMax.value) profile.age_preference_max = agePreferenceMax.value
  if (seekingTags.value.length > 0) profile.seeking_tags = seekingTags.value

  if (Object.keys(profile).length > 0) {
    userData.profile = profile
  }

  try {
    const response = await $axios.put('/auth/profile-update', userData)
    rspErrors.value = {}
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
    isUpdatingProfile.value = false
  }
}

const uploadPhoto = (photo: Photo) => {
  photos.value.push(photo)
}

const updatePhotoPublic = (id: string, value: boolean) => {
  const photoIndex = photos.value.findIndex((item) => item.id === id)
  if (photoIndex !== -1) {
    photos.value[photoIndex].is_public = value
  }
}

const updatePhotoPrimary = (id: string, value: boolean) => {
  photos.value.forEach((item) => {
    item.is_primary = false
  })
  const photoIndex = photos.value.findIndex((item) => item.id === id)
  if (photoIndex !== -1) {
    photos.value[photoIndex].is_primary = value
    if (value) {
      userStore.updatePhoto(photos.value[photoIndex].file_url)
    } else {
      userStore.updatePhoto(null)
    }
  }
}

const deletePhoto = (id: string, isPrimary: boolean) => {
  photos.value = photos.value.filter((item) => item.id !== id)
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
    <v-row
      v-else
      class="mt-3 mb-5"
    >
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
        <v-form
          @submit.prevent="updateUserProfile"
          class="d-flex flex-column ga-2"
        >
          <v-text-field
            v-model="name"
            :readonly="isUpdatingProfile"
            type="text"
            maxlength="64"
            variant="filled"
            prepend-inner-icon="mdi-account-box"
            :label="$t('user.name')"
            :error-messages="rspErrors?.detail?.name ?? []"
          ></v-text-field>
          <v-text-field
            v-model="birthday"
            :readonly="isUpdatingProfile"
            variant="filled"
            type="date"
            prepend-inner-icon="mdi-cake-variant"
            :label="$t('user.birthday')"
            :error-messages="rspErrors?.detail?.birthday ?? []"
          ></v-text-field>
          <v-select
            v-model="gender"
            :readonly="isUpdatingProfile"
            :items="genderOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-gender-male-female"
            :label="$t('user.profile.gender')"
            :error-messages="rspErrors?.detail?.gender ?? []"
          ></v-select>
          <v-text-field
            v-model="heading"
            :readonly="isUpdatingProfile"
            type="text"
            maxlength="50"
            variant="filled"
            prepend-inner-icon="mdi-invoice-text"
            :label="$t('user.profile.heading')"
            :error-messages="rspErrors?.detail?.heading ?? []"
          ></v-text-field>
          <v-autocomplete
            v-model="cityId"
            @update:search="citySearch"
            @click:appendInner="getCityByLocation"
            :loading="isLoadingCity"
            :readonly="isUpdatingProfile"
            :items="cityOptions"
            item-value="value"
            item-title="title"
            no-filter
            hide-no-data
            variant="filled"
            prepend-inner-icon="mdi-city-variant"
            append-inner-icon="mdi-crosshairs-gps"
            :label="$t('user.profile.city')"
            :error-messages="rspErrors?.detail?.city_id ?? []"
          ></v-autocomplete>
          <v-text-field
            v-model="height"
            :readonly="isUpdatingProfile"
            type="number"
            min="50"
            max="250"
            variant="filled"
            prepend-inner-icon="mdi-human-male-height"
            :label="$t('user.profile.height')"
            :suffix="$t('user.profile.height_suffix')"
            :error-messages="rspErrors?.detail?.height ?? []"
          ></v-text-field>
          <v-select
            v-model="bodyType"
            :readonly="isUpdatingProfile"
            :items="bodyOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-human"
            :label="$t('user.profile.body_type')"
            :error-messages="rspErrors?.detail?.body_type ?? []"
          ></v-select>
          <v-select
            v-model="ethnicity"
            :readonly="isUpdatingProfile"
            :items="ethnicityOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-earth"
            :label="$t('user.profile.ethnicity')"
            :error-messages="rspErrors?.detail?.ethnicity ?? []"
          ></v-select>
          <v-select
            v-model="relationshipStatus"
            :readonly="isUpdatingProfile"
            :items="relationshipOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-heart-box"
            :label="$t('user.profile.relationship_status')"
            :error-messages="rspErrors?.detail?.relationship_status ?? []"
          ></v-select>
          <v-text-field
            v-model="children"
            :readonly="isUpdatingProfile"
            type="number"
            min="0"
            max="10"
            variant="filled"
            prepend-inner-icon="mdi-human-child"
            :label="$t('user.profile.children')"
            :error-messages="rspErrors?.detail?.children ?? []"
          ></v-text-field>
          <v-select
            v-model="drink"
            :readonly="isUpdatingProfile"
            :items="drinkOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-glass-wine"
            :label="$t('user.profile.drink')"
            :error-messages="rspErrors?.detail?.drink ?? []"
          ></v-select>
          <v-select
            v-model="smoke"
            :readonly="isUpdatingProfile"
            :items="smokeOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-smoking"
            :label="$t('user.profile.smoke')"
            :error-messages="rspErrors?.detail?.smoke ?? []"
          ></v-select>
          <v-select
            v-model="education"
            :readonly="isUpdatingProfile"
            :items="educationOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-school"
            :label="$t('user.profile.education')"
            :error-messages="rspErrors?.detail?.education ?? []"
          ></v-select>
          <v-select
            v-model="occupation"
            :readonly="isUpdatingProfile"
            :items="occupationOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-briefcase"
            :label="$t('user.profile.occupation')"
            :error-messages="rspErrors?.detail?.occupation ?? []"
          ></v-select>
          <v-select
            v-model="annualIncome"
            :readonly="isUpdatingProfile"
            :items="annualIncomeOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-cash"
            :label="$t('user.profile.annual_income')"
            :error-messages="rspErrors?.detail?.annual_income ?? []"
          ></v-select>
          <v-select
            v-model="netWorth"
            :readonly="isUpdatingProfile"
            :items="netWorthOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-cash-multiple"
            :label="$t('user.profile.net_worth')"
            :error-messages="rspErrors?.detail?.net_worth ?? []"
          ></v-select>
          <v-textarea
            v-model="about"
            :readonly="isUpdatingProfile"
            maxlength="5000"
            variant="filled"
            prepend-inner-icon="mdi-text-account"
            :label="$t('user.profile.about')"
            :hint="$t('user.profile.about_hint')"
            :error-messages="rspErrors?.detail?.about ?? []"
          ></v-textarea>
          <v-select
            v-model="genderPreference"
            :readonly="isUpdatingProfile"
            :items="genderPreferenceOptions"
            item-value="value"
            item-title="title"
            variant="filled"
            prepend-inner-icon="mdi-gender-male-female"
            :label="$t('user.profile.gender_preference')"
            :error-messages="rspErrors?.detail?.gender_preference ?? []"
          ></v-select>
          <v-range-slider
            :model-value="[agePreferenceMin, agePreferenceMax]"
            @update:modelValue="(value) => {
              agePreferenceMin = value[0]
              agePreferenceMax = value[1]
            }"
            :readonly="isUpdatingProfile"
            :step="1"
            :min="18"
            :max="55"
            thumb-label="always"
            :label="$t('user.profile.age_preference')"
            class="mt-3"
          ></v-range-slider>
          <v-select
            v-model="seekingTags"
            :readonly="isUpdatingProfile"
            :items="seekingTagsOptions"
            item-value="value"
            item-title="title"
            multiple
            chips
            variant="filled"
            prepend-inner-icon="mdi-tag-multiple"
            :label="$t('user.profile.seeking_tags')"
            :error-messages="rspErrors?.detail?.seeking_tags ?? []"
          ></v-select>
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
