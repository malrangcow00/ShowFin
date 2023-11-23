<template>
  <i
    @click="router.go(-1)"
    class="fa-solid fa-arrow-right-to-bracket fa-rotate-180 h3 me-4 d-flex justify-content-end"
    style="cursor: pointer"
  ></i>
  <v-col></v-col>
  <v-card class="pa-8">
    <v-card-title class="headline">
      <h1>{{ username }} 님의 회원 정보</h1>
    </v-card-title>
    <v-divider></v-divider>
    <v-row>
      <div class="col-2">
        <div class="list-group list-group-flush">
          <RouterLink
            :to="{ name: 'UserDeposit' }"
            class="list-group-item text-success fs-5 fw-bold"
          >
            가입한 상품
          </RouterLink>
          <RouterLink
            :to="{ name: 'AccountDetailView' }"
            class="list-group-item list-group-item-action text-success"
          >
            MY PAGE
          </RouterLink>
        </div>
      </div>
      <v-col cols="10" md="6">
        <v-list>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >회원 ID :
              </v-list-item-title>
              <v-list-item-subtitle class="my-2">{{
                username
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >닉네임 :
              </v-list-item-title>
              <v-list-item-subtitle class="my-2">{{
                nickname
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >이메일 :
              </v-list-item-title>
              <v-list-item-subtitle class="my-2">{{
                email
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >주거래 은행 :
              </v-list-item-title>
              <v-list-item-subtitle class="my-2">{{
                mainbank
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content class="my-2">
              <v-list-item-title class="font-weight-bold"
                >활동지역 (거주지) :
              </v-list-item-title>
              <v-list-item-subtitle class="my-2">{{
                location
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >나이 :
              </v-list-item-title>
              <v-list-item-subtitle class="my-2">{{
                age
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >재산 :
              </v-list-item-title>
              <v-list-item-subtitle class="my-2">{{
                wealth.toLocaleString("ko-KR")
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>

          <v-list-item>
            <v-list-item-content>
              <v-list-item-title class="font-weight-bold"
                >연봉 :
              </v-list-item-title>
              <v-list-item-subtitle class="my-2">{{
                salary.toLocaleString("ko-KR")
              }}</v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list>
        <v-card-actions>
          <v-btn @click.prevent="goUserDeposit" color="primary"
            >가입한 상품</v-btn
          >
          <v-btn @click.prevent="goUpdatePage" color="warning"
            >회원정보수정</v-btn
          >
        </v-card-actions>
      </v-col>
    </v-row>
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
