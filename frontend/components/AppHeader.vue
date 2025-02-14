<script setup lang="ts">
import { useDisplay } from 'vuetify'
import UserMenuHeader from './UserMenuHeader.vue'

const { $axios } = useNuxtApp()
const localePath = useLocalePath()
const userStore = useUserStore()
const tokenType = useCookie('tokenType')

const loadingStatus = ref(true)
const isMobile = ref(false)
const navDrawer = ref(false)
const userDrawer = ref(false)

const getUser = async () => {
  try {
    const response = await $axios.get('/auth/user')
    const fileUrl = response.data.photos[0]?.file_url
    userStore.setUserData({
      id: response.data.id,
      email: response.data.email,
      name: response.data.name,
      is_verified: response.data.is_verified,
      primary_photo: fileUrl ? `http://127.0.0.1:8000/photos/get/${fileUrl}` : null
    })
  } catch (error) {
    console.error(error)
  } finally {
    loadingStatus.value = false
  }
}

watch(tokenType, async (newValue) => {
  if (newValue) {
    getUser()
  } else {
    userStore.resetUserData()
  }
})

onMounted(() => {
  isMobile.value = useDisplay().mobile.value

  if (tokenType.value) {
    getUser()
  } else {
    loadingStatus.value = false
  }
})
</script>

<template>
  <v-app-bar
    height="64"
    scroll-behavior="elevate"
    style="border-bottom: 1px solid #E0E0E0;"
  >
    <v-container
      v-if="!loadingStatus"
      class="d-flex align-center"
    >
      <v-app-bar-nav-icon
        v-show="isMobile"
        @click.stop="navDrawer = !navDrawer"
        variant="text"
      ></v-app-bar-nav-icon>

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

      <nav
        v-if="userStore.isLoggedIn && !isMobile"
        class="d-flex align-center"
      >
        <v-btn
          :to="localePath('/')"
          :active="$route.name?.toString().includes('index')"
          variant="text"
          prepend-icon="mdi-magnify"
        >
          {{ $t('header.search') }}
        </v-btn>
        <v-btn
          :to="localePath('/about-us')"
          :active="$route.name?.toString().includes('about-us')"
          variant="text"
          prepend-icon="mdi-heart-outline"
        >
          {{ $t('header.interests') }}
        </v-btn>
        <v-btn
          :to="localePath('/how-it-works')"
          :active="$route.name?.toString().includes('how-it-works')"
          variant="text"
          prepend-icon="mdi-message-outline"
        >
          {{ $t('header.messages') }}
        </v-btn>
      </nav>

      <nav
        v-else-if="!isMobile"
        class="d-flex align-center"
      >
        <v-btn
          :to="localePath('/about-us')"
          :active="$route.name?.toString().includes('about-us')"
          variant="text"
          class="font-weight-bold"
        >
          {{ $t('header.about_us') }}
        </v-btn>
        <v-btn
          :to="localePath('/how-it-works')"
          :active="$route.name?.toString().includes('how-it-works')"
          variant="text"
          class="font-weight-bold"
        >
          {{ $t('header.howItWorks') }}
        </v-btn>
      </nav>

      <div class="flex-grow-1">
        <div
          v-if="userStore.isLoggedIn && isMobile"
          class="d-flex align-center justify-end"
        >
          <v-btn
            @click.stop="userDrawer = !userDrawer"
            icon
          >
            <v-avatar :size="32">
              <v-img
                v-if="userStore.primary_photo"
                :src="userStore.primary_photo"
                :alt="userStore.name ?? undefined"
              ></v-img>
              <v-icon
                v-else
                icon="mdi-account-circle"
                :size="32"
                role="img"
              ></v-icon>
            </v-avatar>
          </v-btn>
        </div>

        <div
          v-else-if="userStore.isLoggedIn"
          class="d-flex align-center justify-end"
        >
          <v-menu location="bottom end">
            <template v-slot:activator="{ props }">
              <v-btn
                v-bind="props"
                icon
              >
                <v-avatar :size="32">
                  <v-img
                    v-if="userStore.primary_photo"
                    :src="userStore.primary_photo"
                    :alt="userStore.name ?? undefined"
                  ></v-img>
                  <v-icon
                    v-else
                    icon="mdi-account-circle"
                    :size="32"
                    role="img"
                  ></v-icon>
                </v-avatar>
              </v-btn>
            </template>

            <v-sheet
              :min-width="210"
              :max-width="290"
              rounded="lg"
            >
              <UserMenuHeader />
            </v-sheet>
          </v-menu>
        </div>

        <div
          v-else-if="isMobile"
          class="d-flex align-center justify-end"
        >
          <v-btn
            :to="localePath('/login')"
            variant="outlined"
            color="primary"
            rounded="xl"
            class="text-none"
          >
            {{ $t('header.login') }}
          </v-btn>
        </div>

        <div
          v-else
          class="d-flex align-center justify-end"
        >
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
            class="text-none ms-1"
          >
            {{ $t('header.register') }}
          </v-btn>
        </div>

      </div>
    </v-container>
  </v-app-bar>

  <v-navigation-drawer
    v-if="isMobile"
    v-model="navDrawer"
    location="start"
    temporary
  >
    <v-list
      v-if="userStore.isLoggedIn"
      density="compact"
      nav
    >
      <v-list-item
        :to="localePath('/')"
        :active="$route.name?.toString().includes('index')"
        prepend-icon="mdi-magnify"
        class="text-uppercase"
      >
        {{ $t('header.search') }}
      </v-list-item>
      <v-list-item
        :to="localePath('/about-us')"
        :active="$route.name?.toString().includes('about-us')"
        prepend-icon="mdi-heart-outline"
        class="text-uppercase"
      >
        {{ $t('header.interests') }}
      </v-list-item>
      <v-list-item
        :to="localePath('/how-it-works')"
        :active="$route.name?.toString().includes('how-it-works')"
        prepend-icon="mdi-message-outline"
        class="text-uppercase"
      >
        {{ $t('header.messages') }}
      </v-list-item>
    </v-list>
    <v-list
      v-else
      density="compact"
      nav
    >
      <v-list-item
        :to="localePath('/about-us')"
        :active="$route.name?.toString().includes('about-us')"
        class="font-weight-bold text-uppercase"
      >
        {{ $t('header.about_us') }}
      </v-list-item>
      <v-list-item
        :to="localePath('/how-it-works')"
        :active="$route.name?.toString().includes('how-it-works')"
        class="font-weight-bold text-uppercase"
      >
        {{ $t('header.howItWorks') }}
      </v-list-item>
    </v-list>
  </v-navigation-drawer>

  <v-navigation-drawer
    v-if="isMobile"
    v-model="userDrawer"
    location="right"
    temporary
  >
    <UserMenuHeader />
  </v-navigation-drawer>
</template>
