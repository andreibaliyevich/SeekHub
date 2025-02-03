<script setup lang="ts">
const { locale, locales, setLocale } = useI18n()
const localePath = useLocalePath()
</script>

<template>
  <v-footer class="bg-grey-darken-4 text-white">
    <v-container class="pt-10">
      <v-row justify="space-around" class="pb-1">
        <v-col
          :cols="12"
          :sm="3"
        >
          <p class="mb-3">{{ $t('footer.description') }}</p>
          <div class="d-flex justify-space-evenly mb-5">
            <a
              class="text-secondary link-facebook me-3"
              href="https://www.facebook.com/"
              target="_blank"
            >
              <v-icon
                icon="mdi-facebook"
                size="small"
              ></v-icon>
            </a>
            <a
              class="text-secondary link-instagram me-3"
              href="https://www.instagram.com/"
              target="_blank"
            >
              <v-icon
                icon="mdi-instagram"
                size="small"
              ></v-icon>
            </a>
            <a
              class="text-secondary link-twitter me-3"
              href="https://twitter.com/"
              target="_blank"
            >
              <v-icon
                icon="mdi-twitter"
                size="small"
              ></v-icon>
            </a>
            <a
              class="text-secondary link-youtube me-3"
              href="https://www.youtube.com/"
              target="_blank"
            >
              <v-icon
                icon="mdi-youtube"
                size="small"
              ></v-icon>
            </a>
            <a
              class="text-secondary link-pinterest"
              href="https://www.pinterest.com/"
              target="_blank"
            >
              <v-icon
                icon="mdi-pinterest"
                size="small"
              ></v-icon>
            </a>
          </div>
          <v-select
          :model-value="locale"
          @update:modelValue="(value) => setLocale(value)"
          :items="locales"
          item-title="name"
          item-value="code"
          variant="outlined"
          density="comfortable"
          ></v-select>
        </v-col>
        <v-col
          :cols="12"
          :sm="3"
        >
          <ul class="d-flex flex-column">
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.rules') }}
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.advertising') }}
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.our_logos') }}
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.feedback') }}
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.more_about_seekhub') }}
              </NuxtLink>
            </li>
          </ul>
        </v-col>
        <v-col
          :cols="12"
          :sm="3"
        >
          <ul class="d-flex flex-column">
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.analytics') }}
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.career_at_seekhub') }}
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.terms_of_use') }}
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.privacy_policy') }}
              </NuxtLink>
            </li>
            <li>
              <NuxtLink
                :to="localePath('/')"
                class="d-block text-decoration-none text-white py-1"
              >
                {{ $t('footer.advertising_and_promotion') }}
              </NuxtLink>
            </li>
          </ul>
        </v-col>
      </v-row>
      <v-divider></v-divider>
      <div class="mt-5 text-center text-caption">Copyright © {{ new Date().getFullYear() }} SeekHub</div>
    </v-container>
  </v-footer>
</template>

<style scoped>
.link-facebook:hover {
  color: #1877f2 !important;
}
.link-instagram:hover {
  color: #e1306c !important;
}
.link-twitter:hover {
  color: #1da1f2 !important;
}
.link-youtube:hover {
  color: #ff0000 !important;
}
.link-pinterest:hover {
  color: #e60023 !important;
}

ul {
  list-style: none;
}
ul > li a:focus,
ul > li a:hover {
  color: #e72a26 !important;
}
</style>
