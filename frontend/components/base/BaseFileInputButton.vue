<script setup lang="ts">
defineOptions({
  inheritAttrs: false
})

const emit = defineEmits<{
  (event: 'selectedFiles', files: File[]): void
}>()

const { accept, multiple } = withDefaults(defineProps<{
  accept?: string
  multiple?: boolean
}>(), {
  accept: '*/*',
  multiple: false
})

const fileInput = ref<HTMLInputElement | null>(null)

const changeInput = (event: Event) => {
  const target = event.target as HTMLInputElement
  if (target.files) {
    emit('selectedFiles', Array.from(target.files))
    fileInput.value.value = ''
  }
}
</script>

<template>
  <input
    ref="fileInput"
    @change="changeInput"
    type="file"
    :accept="accept"
    :multiple="multiple"
    class="d-none"
  >
  <v-btn
    @click.stop="fileInput?.click()"
    v-bind="$attrs"
  ></v-btn>
</template>
