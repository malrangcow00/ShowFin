<template>
  <v-app>
    <v-app-bar height="40">
      <v-col>
        <div v-if="store.isLogIn">
          <v-row justify="start">
            <v-col cols="4" align="center" class="font-weight-bold ma-1">
              🎉 {{ store.userInfo.nickname }}님 환영합니다
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
              @click="goMain"
            ></v-img>
          </v-col>
          <v-col align="end" justify="end">
            <v-btn :to="{ name: 'MainView' }" text>HOME</v-btn>
            <!-- <v-btn :to="{ name: 'DepositsView' }" text>Products</v-btn> -->
            <v-btn :to="{ name: 'ProductsView' }" text>상품비교</v-btn>
            <v-btn :to="{ name: 'ArticleView' }" text>게시판</v-btn>
            <v-btn :to="{ name: 'SignUpView' }" text>회원가입</v-btn>
            <v-btn :to="{ name: 'LogInView' }" text>로그인</v-btn>
            <v-btn :to="{ name: 'searchBank' }" text>은행지도</v-btn>
            <v-btn :to="{ name: 'exchange' }" text>환율계산</v-btn>
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
  <footer>
    <p>&copy; 2023 피난길. All rights reserved.</p>
  </footer>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { useRouter, RouterView } from "vue-router";

const store = useAccountStore();
const router = useRouter();

const goLogin = function () {
  router.push({ name: "LogInView" });
};

const goMain = function () {
  router.push({ name: "MainView" });
};
</script>

<style scoped>
* {
  font-family: "Noto Sans KR", sans-serif;
}
footer {
  background-color: #f0f0f0;
  color: black;
  text-align: center;
  padding: 1em;
  position: relative;
  bottom: 0;
  width: 100%;
  height: 30px;
}
footer > p {
  line-height: 30px;
}
</style>
