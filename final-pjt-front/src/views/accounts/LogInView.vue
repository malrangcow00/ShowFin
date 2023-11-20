<template>
  <div>
    <form @submit.prevent="logIn">
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username" />
      </div>
      <div>
        <label for="password">password : </label>
        <input type="password" id="password" v-model.trim="password" />
      </div>
      <input type="submit" value="LOG IN" />
    </form>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAccountStore } from "@/stores/accounts.js";

const store = useAccountStore();
const username = ref(null);
const password = ref(null);

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value,
  };
  store.logIn(payload);
};
</script>

<style scoped></style>
