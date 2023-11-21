<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-8" max-width="100%">
          <v-card-title>
            <h1 class="text-h4 mb-5">회원가입</h1>
            <hr class="my-3" />
          </v-card-title>
          <v-form @submit.prevent="signUp">
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="username"
                  label="ID"
                  hint="아이디를 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="nickname"
                  label="닉네임"
                  hint="닉네임을 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model.trim="password1"
                  label="비빌번호"
                  type="password"
                  hint="비밀번호를 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model.trim="password2"
                  label="비밀번호 확인"
                  type="password"
                  hint="비밀번호를 한번 더 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="email"
                  label="이메일"
                  hint="이메일을 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="age"
                  label="나이"
                  hint="만 나이로 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model.trim="wealth"
                  label="재산"
                  hint="만원 단위로 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model.trim="salary"
                  label="연봉"
                  hint="만원 단위로 입력해주세요."
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-btn type="submit" color="primary">회원가입</v-btn>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
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

<style scoped>
/* Add any additional styling if needed */
</style>
