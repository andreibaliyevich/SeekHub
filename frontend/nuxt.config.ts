import vuetify, { transformAssetUrls } from 'vite-plugin-vuetify'

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  css: ['~/assets/main.css'],
  build: {
    transpile: ['vuetify']
  },
  modules: [
    '@pinia/nuxt',
    '@nuxtjs/i18n',
    (_options, nuxt) => {
      nuxt.hooks.hook('vite:extendConfig', (config) => {
        // @ts-expect-error
        config.plugins.push(vuetify({ autoImport: true }))
      })
    }
  ],
  runtimeConfig: {
    public: {
      apiBase: 'http://localhost:8000/'
    }
  },
  i18n: {
    baseUrl: 'http://localhost:3000/',
    vueI18n: './i18n.config.ts',
    strategy: 'prefix_except_default',
    defaultLocale: 'en',
    lazy: true,
    langDir: '../locales',
    locales: [
      { code: 'en', language: 'en-US', file: 'en.ts', name: 'English' },
      { code: 'ru', language: 'ru-RU', file: 'ru.ts', name: 'Русский' }
    ]
  },
  devtools: { enabled: true },
  devServer: {
    host: '0.0.0.0',
    port: 3000
  },
  vite: {
    vue: {
      template: {
        transformAssetUrls
      },
    },
    server: {
      watch: {
        usePolling: true
      }
    }
  }
})
