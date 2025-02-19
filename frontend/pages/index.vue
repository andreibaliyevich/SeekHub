<script setup lang="ts">
const { t } = useI18n()

useSeoMeta({
  title: t('pages.home.title'),
  ogTitle: t('pages.home.title'),
  description: t('pages.home.description'),
  ogDescription: t('pages.home.description'),
  keywords: t('pages.home.keywords')
})
</script>

<template>
  <div>
    <h1>Welcome to the homepage</h1>
    <h2>{{ $t('hello', { name: 'Andrei' }) }}</h2>
    <p>{{ $t('min_number_hours', { n: 3 }) }}</p>
  </div>
</template>
