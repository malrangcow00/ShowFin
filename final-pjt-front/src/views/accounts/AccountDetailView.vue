<template>
  <v-card class="pa-8">
    <v-card-title class="headline">
      <h1>{{ username }} 님의 회원 정보</h1>
    </v-card-title>
    <v-divider></v-divider>
    <v-row>
      <v-col cols="12" md="6">
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >회원 ID:</v-list-item-title
              >
              <v-list-item-subtitle>{{ username }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >닉네임:</v-list-item-title
              >
              <v-list-item-subtitle>{{ nickname }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >이메일:</v-list-item-title
              >
              <v-list-item-subtitle>{{ email }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >주거래 은행:</v-list-item-title
              >
              <v-list-item-subtitle>{{ mainbank }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >활동지역 (거주지):</v-list-item-title
              >
              <v-list-item-subtitle>{{ location }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >나이:</v-list-item-title
              >
              <v-list-item-subtitle>{{ age }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >재산:</v-list-item-title
              >
              <v-list-item-subtitle>{{
                wealth.toLocaleString("ko-KR")
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >월급:</v-list-item-title
              >
              <v-list-item-subtitle>{{
                salary.toLocaleString("ko-KR")
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>

    <v-card-actions>
      <v-btn @click.prevent="goUserDeposit" color="primary">가입한 상품</v-btn>
      <v-btn @click.prevent="goUpdatePage" color="warning">회원정보수정</v-btn>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { useRouter, RouterLink } from "vue-router";

const store = useAccountStore();
const router = useRouter();

const { username, nickname, email, age, wealth, salary, mainbank, location } =
  store.userInfo;

const goUpdatePage = function () {
  router.push({ name: "AccountUpdateView" });
};

const goUserDeposit = function () {
  router.push({ name: "UserDeposit" });
};
</script>

<style scoped>
.headline {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.font-weight-bold {
  font-weight: bold;
}
</style>
