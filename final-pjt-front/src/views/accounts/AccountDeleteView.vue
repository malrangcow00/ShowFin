<template>
  <div>
    <h1>real 탈퇴하고싶으면 비밀번호를 입력하thㅔ요 ~</h1>
    <form @submit.prevent="deleteAccount">
      <label for="password">비밀번호 : </label>
      <input type="password" id="password" v-model.trim="password" />
      <input type="submit" value="회원탈퇴" />
    </form>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";

const store = useAccountStore();

const password = ref(null);

const deleteAccount = function () {
  const payload = {
    password: password.value,
  };
  store.deleteAccount(payload);
};
</script>

<style scoped></style>
