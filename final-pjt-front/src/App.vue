<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
    <RouterLink :to="{ name: 'main' }">Main</RouterLink> |
    <RouterLink :to="{ name: 'searchBank' }">SearchBank</RouterLink> |
    <RouterView />
</template>

<style scoped>

</style>
