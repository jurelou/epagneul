
<template>
    mytimeline {{ data }}
    <div id="timeline" />
</template>

<script setup>
import { defineProps } from 'vue'

const props = defineProps({
  data: Array
})

</script>