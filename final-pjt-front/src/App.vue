<template>
  <header>
    <RouterLink :to="{ name: 'MainView' }">Main</RouterLink> |
    <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> |
    <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink> |
    <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink> |
    <RouterLink :to="{ name: 'searchBank' }">SearchBank</RouterLink> |
    <RouterLink :to="{ name: 'exchanger' }">Exchanger</RouterLink> |
  </header>
    <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";

const store = useAccountStore();
</script>

<style scoped></style>
