<!-- <template>
  <header>
    <div v-if="store.isLogIn">
      <p>{{ store.logInUser }}님 환영합니다.</p>
      <button @click.prevent="store.logOut">LOG OUT</button>
      <button @click.prevent="store.getAccountInfo">회원 정보 조회</button>
    </div>
    <p v-else>로그인 하세요~~~ ㅎㅎ</p>
    <RouterLink :to="{ name: 'MainView' }">Main</RouterLink> |
    <RouterLink :to="{ name: 'DepositsView' }">Products</RouterLink> |
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

<style scoped></style> -->
<template>
  <v-app>
    <v-app-bar app color="deep-purple-accent-1" height="80">
      <v-container>
        <v-row align="center" justify="space-between">
          <v-col-2>
            <div v-if="store.isLogIn">
              <v-row align="center" justify="center">
                <v-text class="text-h6 font-weight-bold"
                  >{{ store.logInUser }}님 환영합니다.</v-text
                >
              </v-row>
              <v-row>
                <v-btn @click.prevent="store.logOut" outlined color="white"
                  >로그아웃</v-btn
                >
                <v-btn
                  @click.prevent="store.getAccountInfo"
                  outlined
                  color="white"
                  >회원 정보 조회</v-btn
                >
              </v-row>
            </div>
            <v-text v-else>로그인 하세요.</v-text>
          </v-col-2>
          <v-col-auto>
            <v-row align="center" justify="end">
              <v-btn :to="{ name: 'MainView' }" text>Main</v-btn>
              <v-btn :to="{ name: 'DepositsView' }" text>Products</v-btn>
              <v-btn :to="{ name: 'ArticleView' }" text>Articles</v-btn>
              <v-btn :to="{ name: 'SignUpView' }" text>SignUp</v-btn>
              <v-btn :to="{ name: 'LogInView' }" text>LogIn</v-btn>
              <v-btn :to="{ name: 'searchBank' }" text>SearchBank</v-btn>
              <v-btn :to="{ name: 'exchange' }" text>Exchange</v-btn>
            </v-row>
          </v-col-auto>
        </v-row>
      </v-container>
    </v-app-bar>

    <v-main>
      <v-container>
        <RouterView />
      </v-container>
    </v-main>
  </v-app>
</template>

<script setup>
import { ref } from "vue";
import { useAccountStore } from "@/stores/accounts.js";
import { RouterLink, RouterView } from "vue-router";

const store = useAccountStore();
</script>

<style scoped>
/* 스타일링 */
</style>
