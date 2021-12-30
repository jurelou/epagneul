<template>
  <q-item
    clickable
    :to="to"
  >
    <q-item-section
      v-if="icon"
      avatar
    >
      <q-icon class="text-secondary" :name="icon" />
    </q-item-section>

    <q-item-section>
      <q-item-label>{{ title }}</q-item-label>
      <q-item-label caption>
        {{ caption }}
      </q-item-label>
    </q-item-section>
  </q-item>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'EssentialLink',
  props: {
    title: {
      type: String,
      required: true
    },

    caption: {
      type: String,
      default: ''
    },
    to: {
      type: String,
    },
    icon: {
      type: String,
      default: ''
    }
  }
})
</script>
