<script setup lang="ts">
import 'cropperjs/dist/cropper.css'
import Cropper from 'cropperjs'
import { useDate } from '@/composables/useDate'
import type { Photo } from '@/types/photo'
import BaseFileInputButton from '@/components/base/BaseFileInputButton.vue'

const { $axios } = useNuxtApp()
const emit = defineEmits<{
  (event: 'uploadPhoto', photo: Photo): void
  (event: 'updatePhotoPublic', id: string, value: boolean): void
  (event: 'updatePhotoPrimary', id: string, value: boolean): void
  (event: 'deletePhoto', id: string, isPrimary: boolean): void
}>()
const { photos } = defineProps<{
  photos: Photo[]
}>()
const { formatDate } = useDate()

const photoId = ref<string | null>(null)
const photoImg = ref<HTMLImageElement | null>(null)
const photoCropper = ref<Cropper | null>(null)

const isLoadingPhoto = ref(false)
const isUploadingPhoto = ref(false)
const isSettingPublic = ref(false)
const isSettingPrimary = ref(false)
const isDeletingPhoto = ref(false)

const photoUploadDialog = ref(false)
const updatePhotoDialog = ref(false)
const deletePhotoDialog = ref(false)

const openPhoto = computed(() => photos.find(photo => photo.id === photoId.value) || null)
const primaryPhoto = computed(() => photos.find(photo => photo.is_primary) || null)
const nonPrimaryPhotos = computed(() => photos.filter(photo => !photo.is_primary))

const loadPhotoImg = async (files) => {
  isLoadingPhoto.value = true
  photoUploadDialog.value = true

  const reader = new FileReader()
  reader.readAsDataURL(files[0])

  reader.onload = () => {
    photoImg.value.src = reader.result
    photoImg.value.alt = files[0].name

    photoCropper.value = new Cropper(photoImg.value, {
      viewMode: 1,
      dragMode: 'crop',
      aspectRatio: 3/4,
      zoomable: false,
      ready() {
        isLoadingPhoto.value = false
      }
    })
  }
}

const uploadPhoto = async () => {
  isUploadingPhoto.value = true

  const croppedCanvas = photoCropper.value.getCroppedCanvas({
    width: 1200,
    height: 1600
  })
  const canvasBlob = await new Promise((resolve) => {
    croppedCanvas.toBlob((blob) => {
      resolve(blob)
    })
  })

  let formData = new FormData()
  formData.append('file', canvasBlob, photoImg.value.alt)

  try {
    const response = await $axios.post('/photos/upload', formData)
    if (response.status === 201) {
      emit('uploadPhoto', response.data)
    }
  } catch (error) {
    console.error(error)
  } finally {
    isUploadingPhoto.value = false
    photoUploadDialog.value = false
    photoCropper.value.destroy()
    photoCropper.value = null
  }
}

const updatePhotoPublic = async () => {
  isSettingPublic.value = true
  const isPublic = !openPhoto.value.is_public

  let formData = new FormData()
  formData.append('is_public', isPublic)

  try {
    const response = await $axios.put(
      `/photos/update/${photoId.value}`,
      formData
    )
    if (response.status === 200) {
      emit('updatePhotoPublic', photoId.value, isPublic)
    }
  } catch (error) {
    console.error(error)
  } finally {
    isSettingPublic.value = false
  }
}

const updatePhotoPrimary = async () => {
  isSettingPrimary.value = true
  const isPrimary = !openPhoto.value.is_primary

  let formData = new FormData()
  formData.append('is_primary', isPrimary)

  try {
    const response = await $axios.put(
      `/photos/update/${photoId.value}`,
      formData
    )
    if (response.status === 200) {
      emit('updatePhotoPrimary', photoId.value, isPrimary)
    }
  } catch (error) {
    console.error(error)
  } finally {
    isSettingPrimary.value = false
  }
}

const deletePhoto = async () => {
  isDeletingPhoto.value = true
  try {
    const response = await $axios.delete(`/photos/delete/${photoId.value}`)
    if (response.status === 204) {
      emit('deletePhoto', photoId.value, openPhoto.value.is_primary)
    }
  } catch (error) {
    console.error(error)
  } finally {
    photoId.value = null
    isDeletingPhoto.value = false
    deletePhotoDialog.value = false
  }
}
</script>

<template>
  <v-hover v-slot="{ isHovering, props }">
    <v-card
      v-bind="props"
      rounded="lg"
    >
      <v-img
        :src="
          !!primaryPhoto
          ? primaryPhoto.file_url
          : '/user-avatar.png'
        "
        :aspect-ratio="3/4"
      ></v-img>
      <v-overlay
        v-if="!!primaryPhoto"
        :model-value="isHovering"
        contained
        scrim="black"
        :opacity="0.5"
        content-class="d-flex align-center justify-center w-100 h-100"
      >
        <v-btn
          @click="() => {
            photoId = primaryPhoto.id
            updatePhotoDialog = true
          }"
          icon="mdi-pencil"
          variant="flat"
          color="grey-lighten-3"
          size="x-small"
        ></v-btn>
        <v-btn
          @click="() => {
            photoId = primaryPhoto.id
            deletePhotoDialog = true
          }"
          icon="mdi-delete"
          variant="flat"
          color="red-darken-3"
          size="x-small"
          class="ms-1"
        ></v-btn>
      </v-overlay>
    </v-card>
  </v-hover>

  <BaseFileInputButton
    @selectedFiles="loadPhotoImg"
    accept="image/*"
    variant="tonal"
    color="primary"
    class="text-none my-3"
    block
    :text="$t('pages.profile.upload_photo')"
    append-icon="mdi-upload"
  />

  <v-row dense>
    <v-col
      v-for="photo in nonPrimaryPhotos"
      :key="photo.id"
      :cols="12"
      :md="6"
    >
      <v-hover v-slot="{ isHovering, props }">
        <v-card
          v-bind="props"
          rounded="lg"
        >
          <v-img
            :src="photo.file_url"
            :aspect-ratio="3/4"
          ></v-img>
          <v-overlay
            :model-value="isHovering"
            contained
            scrim="black"
            :opacity="0.5"
            content-class="d-flex flex-column align-center justify-center w-100 h-100"
          >
            <v-icon
              :icon="photo.is_public ? 'mdi-eye' : 'mdi-eye-off'"
              :size="24"
              color="white"
            ></v-icon>
            <div class="my-auto">
              <v-btn
                @click="() => {
                  photoId = photo.id
                  updatePhotoDialog = true
                }"
                icon="mdi-pencil"
                variant="flat"
                color="grey-lighten-3"
                size="x-small"
              ></v-btn>
              <v-btn
                @click="() => {
                  photoId = photo.id
                  deletePhotoDialog = true
                }"
                icon="mdi-delete"
                variant="flat"
                color="red-darken-3"
                size="x-small"
                class="ms-1"
              ></v-btn>
            </div>
            <small class="text-white">{{ formatDate(photo.uploaded_at) }}</small>
          </v-overlay>
        </v-card>
      </v-hover>
    </v-col>
  </v-row>

  <v-dialog
    :model-value="photoUploadDialog"
    width="auto"
    persistent
  >
    <v-card rounded="lg">
      <div class="d-flex justify-center align-center">
        <img
          ref="photoImg"
          src="/loading.gif"
          alt="loading"
          style="
            max-width: 100%;
            max-height: 80vh;
          "
        >
      </div>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click="() => {
            photoUploadDialog = false
            photoCropper.destroy()
            photoCropper = null
          }"
          :disabled="isLoadingPhoto"
        >
          {{ $t('base_btn.cancel') }}
        </v-btn>
        <v-btn
          @click="uploadPhoto"
          :loading="isUploadingPhoto"
          :disabled="isLoadingPhoto"
          variant="flat"
          color="primary"
        >
          {{ $t('base_btn.upload') }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog
    :model-value="updatePhotoDialog"
    width="auto"
    persistent
  >
    <v-card rounded="lg">
      <div class="d-flex justify-center align-center">
        <img
          :src="openPhoto?.file_url"
          style="
            max-width: 100%;
            max-height: 80vh;
          "
        >
      </div>
      <v-card-actions class="d-flex flex-wrap">
        <v-btn
          @click="updatePhotoPublic"
          :prepend-icon="openPhoto?.is_public ? 'mdi-eye-off' : 'mdi-eye'"
          :loading="isSettingPublic"
          :disabled="openPhoto?.is_primary"
          :text="openPhoto?.is_public ? $t('pages.profile.make_private') : $t('pages.profile.make_public')"
          variant="flat"
          color="grey-lighten-3"
          class="text-none"
        ></v-btn>
        <v-btn
          @click="updatePhotoPrimary"
          :prepend-icon="openPhoto?.is_primary ? 'mdi-star-off' : 'mdi-star'"
          :loading="isSettingPrimary"
          :disabled="!openPhoto?.is_public"
          :text="openPhoto?.is_primary ? $t('pages.profile.make_non_primary') : $t('pages.profile.make_primary')"
          variant="flat"
          color="grey-lighten-3"
          class="text-none"
        ></v-btn>
        <v-spacer></v-spacer>
        <v-btn
          @click="() => {
            updatePhotoDialog = false
            photoId = null
          }"
        >
          {{ $t('base_btn.close') }}
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>

  <v-dialog
    :model-value="deletePhotoDialog"
    width="auto"
    persistent
  >
    <v-card rounded="lg">
      <v-card-title>
        {{ $t('pages.profile.you_want_remove_photo') }}
      </v-card-title>
      <v-card-text>
        {{ $t('pages.profile.photo_information_will_lost') }}
      </v-card-text>
      <v-card-actions>
        <v-spacer></v-spacer>
        <v-btn
          @click="() => {
            photoId = null
            deletePhotoDialog = false
          }"
        >
          {{ $t('base_btn.no_cancel') }}
        </v-btn>
        <v-btn
          @click="deletePhoto"
          :loading="isDeletingPhoto"
        >
          <strong>{{ $t('base_btn.yes_i_am_sure') }}</strong>
        </v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
