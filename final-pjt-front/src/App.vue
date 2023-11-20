<template>
  <header>
    <div v-if="store.isLogIn">
      <p>{{ store.logInUser }}님 환영합니다.</p>
      <button @click.prevent="store.logOut">LOG OUT</button>
      <button @click.prevent="store.getAccountInfo">회원 정보 조회</button>
    </div>
    <p v-else>로그인 하세요~~~ ㅎㅎ</p>
    <RouterLink :to="{ name: 'MainView' }">Main</RouterLink> |
    <RouterLink :to="{ name: 'ArticleView' }">Articles</RouterLink> |
    <RouterLink :to="{ name: 'SignUpView' }">SignUp</RouterLink> |
    <RouterLink :to="{ name: 'LogInView' }">LogIn</RouterLink> |
    <RouterLink :to="{ name: 'searchBank' }">SearchBank</RouterLink> |
    <RouterLink :to="{ name: 'exchange' }">Exchange</RouterLink> |
  </header>
  <RouterView />
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";

const store = useAccountStore();
</script>

<style scoped></style>
