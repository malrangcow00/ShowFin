<template>
  <div>
    <h1>여기는 유저 디테일 뷰 입니다만?</h1>
    <p>회원 ID : {{ username }}</p>
    <p>닉네임 : {{ nickname }}</p>
    <p>이메일 : {{ email }}</p>
    <p>나이 : {{ age }}</p>
    <p>재산 : {{ wealth }}</p>
    <p>월급 : {{ salary }}</p>
    <p>가입상품 : {{ financial_products }}</p>
    <button @click.prevent="goUpdatePage">회원정보수정</button>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { useRouter } from "vue-router";

const store = useAccountStore();
const router = useRouter();

const { username, nickname, email, age, wealth, salary, financial_products } =
  store.userInfo;

const goUpdatePage = function () {
  router.push({ name: "AccountUpdateView" });
};
</script>

<style scoped></style>
