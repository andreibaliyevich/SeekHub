<script setup lang="ts">
const { t } = useI18n()

useSeoMeta({
  title: t('pages.about.title'),
  ogTitle: t('pages.about.title'),
  description: t('pages.about.description'),
  ogDescription: t('pages.about.description'),
  keywords: t('pages.about.keywords')
})
</script>

<template>
  <div>
    <h1>Welcome to the About page</h1>
  </div>
</template>
