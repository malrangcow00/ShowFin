<template>
  <div>
    <h1>비밀번호 바꾸고싶군요 ?</h1>
    <form @submit.prevent="changePassword">
      <div>
        <label for="old_password">기존 비밀번호 : </label>
        <input type="password" id="old_password" v-model.trim="oldPassword" />
      </div>
      <div>
        <label for="new_password">새 비밀번호 : </label>
        <input type="password" id="new_password" v-model.trim="newPassword" />
      </div>
      <input type="submit" value="비밀번호변경" />
    </form>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";
const store = useAccountStore();

const oldPassword = ref(null);
const newPassword = ref(null);

const changePassword = function () {
  const payload = {
    old_password: oldPassword.value,
    new_password: newPassword.value,
  };
  store.changePassword(payload);
};
</script>

<style scoped></style>
