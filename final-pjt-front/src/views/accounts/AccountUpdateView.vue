<template>
  <div>
    <h1>회원정보수정 가보입시더~</h1>
    <form @submit.prevent="updateAccountInfo">
      <div>
        <label for="username">username : </label>
        <input type="text" id="username" v-model.trim="username" disabled />
      </div>
      <div>
        <label for="nickname">nickname : </label>
        <input type="text" id="nickname" v-model.trim="nickname" />
      </div>
      <!-- <div>
        <label for="password1">password : </label>
        <input type="password" id="password1" v-model.trim="password1" />
      </div>
      <div>
        <label for="password2">password confirmation : </label>
        <input type="password" id="password2" v-model.trim="password2" />
      </div> -->
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
      <input type="submit" value="회원정보수정" />
    </form>
    <button @click.prevent="goAccountDelete">회원탈퇴</button>
    <button @click.prevent="goChangePassword">비밀번호변경</button>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";
import router from "@/router";

const store = useAccountStore();

const username = ref(store.userInfo.username);
const nickname = ref(store.userInfo.nickname);
const email = ref(store.userInfo.email);
const age = ref(store.userInfo.age);
const wealth = ref(store.userInfo.wealth);
const salary = ref(store.userInfo.salary);

const updateAccountInfo = function () {
  const payload = {
    nickname: nickname.value,
    email: email.value,
    age: age.value,
    wealth: wealth.value,
    salary: salary.value,
  };
  store.updateAccountInfo(payload);
};

const goAccountDelete = function () {
  router.push({ name: "AccountDeleteView" });
};

const goChangePassword = function () {
  router.push({ name: "AccountChangePasswordView" });
};
</script>

<style scoped></style>
