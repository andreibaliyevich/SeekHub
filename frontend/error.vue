<script setup lang="ts">
import type { NuxtError } from '#app'
const localePath = useLocalePath()

defineProps({
  error: Object as () => NuxtError
})

const handleError = () => clearError({
  redirect: localePath('/')
})
</script>

<template>
  <div
    class="d-flex align-center justify-center"
    style="height: 100vh;"
  >
    <v-empty-state
      v-if="error?.statusCode === 404"
      image="/error404.png"
      :headline="`${error?.statusCode}`"
      :title="error?.statusMessage"
      :text="$t('pages.error.text404')"
      :action-text="$t('pages.error.action_text')"
      @click:action="handleError"
    ></v-empty-state>
  </div>
</template>
