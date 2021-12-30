<script setup>
import { useQueryProvider } from 'vue-query';
import { useQuasar } from 'quasar'

const $q = useQuasar()
$q.dark.toggle()

useQueryProvider();

</script>

<template>
    <transition appear enter-active-class="animated fadeIn" leave-active-class="animated fadeOut" mode="out-in" :duration="300">
      <router-view/>
    </transition>
</template>
