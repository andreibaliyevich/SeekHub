<script setup lang="ts">
const localePath = useLocalePath()
const navDrawer = ref(false)
</script>

<template>
  <v-app-bar
    height="64"
    scroll-behavior="elevate"
    style="border-bottom: 1px solid #E0E0E0;"
  >
    <v-app-bar-nav-icon
      @click.stop="navDrawer = !navDrawer"
      variant="text"
      class="d-block d-md-none"
    ></v-app-bar-nav-icon>
    <v-container class="d-flex align-center">
      <NuxtLink :to="localePath('/')">
        <v-img
          :width="50"
          src="/logo-navbar.png"
          class="d-block d-sm-none"
        ></v-img>
        <v-img
          :width="150"
          src="/logo-navbar-full.png"
          class="d-none d-sm-block"
        ></v-img>
      </NuxtLink>
      <nav class="d-none d-md-flex align-center">
        <v-btn
          :to="localePath('/about-us')"
          :active="$route.name === 'about-us'"
          variant="text"
          class="font-weight-bold"
        >
          {{ $t('header.about_us') }}
        </v-btn>
        <v-btn
          :to="localePath('/how-it-works')"
          :active="$route.name === 'how-it-works'"
          variant="text"
          class="font-weight-bold"
        >
          {{ $t('header.howItWorks') }}
        </v-btn>
      </nav>
      <div class="flex-grow-1">
        <div class="d-flex align-center justify-end">
          <v-btn
            :to="localePath('/login')"
            variant="outlined"
            color="primary"
            rounded="xl"
            class="text-none"
          >
            {{ $t('header.login') }}
          </v-btn>
          <v-btn
            :to="localePath('/register')"
            variant="tonal"
            color="primary"
            rounded="xl"
            class="d-none d-lg-inline-flex text-none ms-1"
          >
            {{ $t('header.register') }}
          </v-btn>
        </div>
      </div>
    </v-container>
  </v-app-bar>
  <v-navigation-drawer
    v-model="navDrawer"
    location="start"
    temporary
  >
    <v-list
      density="compact"
      nav
    >
      <v-list-item
        :to="localePath('/about-us')"
        :active="$route.name === 'about-us'"
        class="font-weight-bold text-uppercase"
      >
        {{ $t('header.about_us') }}
      </v-list-item>
      <v-list-item
        :to="localePath('/how-it-works')"
        :active="$route.name === 'how-it-works'"
        class="font-weight-bold text-uppercase"
      >
        {{ $t('header.howItWorks') }}
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>
