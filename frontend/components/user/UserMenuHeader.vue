<script setup lang="ts">
const localePath = useLocalePath()
const userStore = useUserStore()

const logout = () => {
  useCookie('accessToken').value = null
  useCookie('refreshToken').value = null
  useCookie('tokenType').value = null
  userStore.resetUserData()
  navigateTo(localePath('/'))
}
</script>

<template>
  <v-list class="pb-0">
    <v-list-item>
      <template v-slot:prepend>
        <v-avatar :size="48">
          <v-img
            v-if="userStore.primary_photo"
            :src="userStore.primary_photo"
            :alt="userStore.name ?? undefined"
          ></v-img>
          <v-icon
            v-else
            icon="mdi-account-circle"
            :size="48"
            role="img"
          ></v-icon>
        </v-avatar>
      </template>
      <template v-slot:title>
        {{ userStore.name }}
      </template>
      <template v-slot:subtitle>
        {{ userStore.email }}
      </template>
    </v-list-item>
    <v-list-item>
      <v-btn
        :to="localePath('/')"
        :active="$route.name?.toString().includes('index')"
        variant="tonal"
        color="primary"
        block
        class="text-none"
      >
        {{ $t('header.view_profile') }}
      </v-btn>
    </v-list-item>
  </v-list>
  <v-list
    nav
    density="compact"
    class="pt-0"
  >
    <v-list-item
      :to="localePath('/profile')"
      :active="$route.name?.toString().includes('profile')"
      prepend-icon="mdi-account-edit"
    >
      <v-list-item-title>
        {{ $t('header.edit_profile') }}
      </v-list-item-title>
    </v-list-item>
    <v-list-item
      :to="localePath('/how-it-works')"
      :active="$route.name?.toString().includes('how-it-works')"
      prepend-icon="mdi-cog"
    >
      <v-list-item-title>
        {{ $t('header.settings') }}
      </v-list-item-title>
    </v-list-item>
    <v-divider class="my-1"></v-divider>
    <v-list-item
      @click="logout()"
      prepend-icon="mdi-logout"
      class="mb-0"
    >
      <v-list-item-title>
        {{ $t('header.log_out') }}
      </v-list-item-title>
    </v-list-item>
  </v-list>
</template>
