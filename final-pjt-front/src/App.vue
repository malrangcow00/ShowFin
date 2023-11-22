<template>
  <v-app>
    <v-app-bar height="40">
      <v-col>
        <div v-if="store.isLogIn">
          <v-row justify="start">
            <v-col cols="4" align="center" class="font-weight-bold ma-1">
              🎉 {{ store.logInUser }}님 환영합니다
            </v-col>
            <v-col></v-col>
            <v-col cols="2" align="center">
              <v-btn @click.prevent="store.logOut" outlined color="black"
                >로그아웃</v-btn
              >
            </v-col>
            <v-col cols="2" align="center">
              <v-btn
                @click.prevent="store.getAccountInfo"
                outlined
                color="black"
                >회원 정보 조회</v-btn
              >
            </v-col>
          </v-row>
        </div>
        <v-btn v-else><span @click="goLogin">로그인 하세요.</span></v-btn>
      </v-col>
    </v-app-bar>
    <v-app-bar app color="deep-purple-accent-1" height="80">
      <v-container>
        <v-row justify="space-between">
          <v-col cols="3" align="start">
            <v-img
              align="center"
              justify="center"
              max-width="100"
              src="../assets/img/nav_logo.png"
              slot="v-app-bar-nav-icon"
            ></v-img>
          </v-col>
          <v-col align="end" justify="end">
            <v-btn :to="{ name: 'MainView' }" text>Main</v-btn>
            <v-btn :to="{ name: 'DepositsView' }" text>Products</v-btn>
            <v-btn :to="{ name: 'ArticleView' }" text>Articles</v-btn>
            <v-btn :to="{ name: 'SignUpView' }" text>SignUp</v-btn>
            <v-btn :to="{ name: 'LogInView' }" text>LogIn</v-btn>
            <v-btn :to="{ name: 'searchBank' }" text>SearchBank</v-btn>
            <v-btn :to="{ name: 'exchange' }" text>Exchange</v-btn>
          </v-col>
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
import { RouterLink, RouterView } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";

const store = useAccountStore();
</script>

<style scoped></style>
