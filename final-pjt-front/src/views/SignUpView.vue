<template>
  <div>
    <h1>회원가입 가보입시더~</h1>
    <form @submit.prevent="signUp">
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username" />
      </div>
      <div>
        <label for="nickname">nickname : </label>
        <input type="text" id="nickname" v-model.trim="nickname" />
      </div>
      <div>
        <label for="password1">password : </label>
        <input type="password" id="password1" v-model.trim="password1" />
      </div>
      <div>
        <label for="password2">password confirmation : </label>
        <input type="password" id="password2" v-model.trim="password2" />
      </div>
      <div>
        <label for="email">email : </label>
        <input type="text" id="email" v-model.trim="email" />
      </div>
      <div>
        <label for="age">age : </label>
        <input type="text" id="age" v-model.trim="age" />
      </div>
      <div>
        <label for="wealth">wealth : </label>
        <input type="text" id="wealth" v-model.trim="wealth" />
      </div>
      <div>
        <label for="salary">salary : </label>
        <input type="text" id="salary" v-model.trim="salary" />
      </div>
      <input type="submit" value="회원가입" />
    </form>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";

const store = useAccountStore();

const username = ref(null);
const nickname = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const email = ref(null);
const age = ref(null);
const wealth = ref(null);
const salary = ref(null);

const signUp = function () {
  const payload = {
    username: username.value,
    nickname: nickname.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    age: age.value,
    wealth: wealth.value,
    salary: salary.value,
  };
  store.signUp(payload);
};
</script>

<style scoped></style>
