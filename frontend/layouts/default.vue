<script setup lang="ts">
const i18nHead = useLocaleHead()
</script>

<template>
  <Html
    :lang="i18nHead.htmlAttrs!.lang"
    :dir="i18nHead.htmlAttrs!.dir"
  >
    <Head>
      <template
        v-for="link in i18nHead.link"
        :key="link.hid"
      >
        <Link
          :id="link.hid"
          :rel="link.rel"
          :href="link.href"
          :hreflang="link.hreflang"
        />
      </template>
      <template
        v-for="meta in i18nHead.meta"
        :key="meta.hid"
      >
        <Meta
          :id="meta.hid"
          :property="meta.property"
          :content="meta.content"
        />
      </template>
    </Head>
    <Body>
      <v-app>
        <v-main>
          <slot />
        </v-main>
      </v-app>
    </Body>
  </Html>
</template>
