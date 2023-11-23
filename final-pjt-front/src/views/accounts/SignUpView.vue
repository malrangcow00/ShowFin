<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="8">
        <v-card class="pa-8" max-width="100%">
          <v-card-title>
            <h1 class="sign-up-header mb-5">회원가입 🍀</h1>
            <hr class="my-3" />
          </v-card-title>
          <v-form @submit.prevent="signUp">
            <v-row>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="username"
                  clearable
                  :rules="[rules.required]"
                  hide-details="auto"
                  label="ID"
                  hint="아이디를 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="nickname"
                  clearable
                  :rules="[rules.required]"
                  hide-details="auto"
                  label="닉네임"
                  hint="닉네임을 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model.trim="password1"
                  clearable
                  hide-details="auto"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show1 ? 'text' : 'password'"
                  label="비밀번호"
                  hint="비밀번호를 입력해주세요. (영문, 숫자, 특수문자 포함 8자 이상)"
                  counter
                  @click:append="show1 = !show1"
                ></v-text-field>
              </v-col>
              <v-col cols="12" md="6">
                <v-text-field
                  v-model.trim="password2"
                  clearable
                  hide-details="auto"
                  :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show2 ? 'text' : 'password'"
                  label="비밀번호"
                  hint="비밀번호를 한번 더 입력해주세요."
                  counter
                  @click:append="show2 = !show2"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="email"
                  clearable
                  :rules="[rules.required]"
                  hide-details="auto"
                  label="이메일"
                  hint="이메일을 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-select
                  v-model="mainbank"
                  :rules="[rules.required]"
                  :items="store.bankList"
                  label="주거래은행"
                  hint="주거래 은행을 선택해주세요"
                ></v-select>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model.trim="location"
                  clearable
                  :rules="[rules.required]"
                  hide-details="auto"
                  label="활동지역 (거주지)"
                  hint="현재 활동 지역(도시)를 입력해주세요."
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-select
                  v-model="selectedAge"
                  :rules="[rules.required]"
                  :items="ageList"
                  label="나이"
                  hint="나이대를 선택해주세요"
                ></v-select>
              </v-col>
              <v-col cols="12" md="6">
                <v-select
                  v-model="selectedWealth"
                  :rules="[rules.required]"
                  :items="options"
                  label="재산"
                  hint="재산 범위를 선택해주세요"
                ></v-select>
              </v-col>
              <v-col cols="12" md="6">
                <v-select
                  v-model="selectedSalary"
                  :rules="[rules.required]"
                  :items="options"
                  label="연봉"
                  hint="연봉 범위를 선택해주세요."
                ></v-select>
              </v-col>
            </v-row>
            <v-row justify="center">
              <v-btn type="submit" color="primary" class="w-25">회원가입</v-btn>
            </v-row>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { onMounted, ref } from "vue";

const store = useAccountStore();

onMounted(() => {
  store.getDeposits();
});

const username = ref(null);
const nickname = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const email = ref(null);
const show1 = ref(false);
const show2 = ref(false);
const mainbank = ref(null);
const location = ref(null);

const selectedAge = ref(null);
const selectedSalary = ref(null);
const selectedWealth = ref(null);

const ageList = ref([
  "10대",
  "20대",
  "30대",
  "40대",
  "50대",
  "60대",
  "70대 이상",
]);
const ageValue = [
  { text: "10대", value: 15 },
  { text: "20대", value: 25 },
  { text: "30대", value: 35 },
  { text: "40대", value: 45 },
  { text: "50대", value: 55 },
  { text: "60대", value: 65 },
  { text: "70대 이상", value: 75 },
];
const options = ref([
  "3000만원 이하",
  "3000만원 ~ 5000만원",
  "5000만원 ~ 8000만원",
  "8000만원 이상",
]);
const optionValue = [
  { text: "3000만원 이하", money: 30000000 },
  { text: "3000만원 ~ 5000만원", money: 50000000 },
  { text: "5000만원 ~ 8000만원", money: 70000000 },
  { text: "8000만원 이상", money: 80000000 },
];

const rules = {
  required: (input) => !!input || "필수 항목입니다.",
  min: (input) => (input && input.length >= 8) || "최소 8자 이상 입력하세요.",
};

const signUp = function () {
  const salary = optionValue.find((option) => {
    if (option.text === selectedSalary.value) {
      return option;
    }
  });
  const wealth = optionValue.find((option) => {
    if (option.text === selectedWealth.value) {
      return option;
    }
  });
  const age = ageValue.find((option) => {
    if (option.text === selectedAge.value) {
      return option;
    }
  });

  // console.log
  // console.log(salary.money);
  // console.log(wealth.money);
  // console.log(age.value);
  if (!username.value) {
    alert("아이디를 입력해주세요.");
    return;
  } else if (!nickname.value) {
    alert("닉네임을 입력해주세요.");
    return;
  } else if (!password1.value) {
    alert("비밀번호를 입력해주세요.");
    return;
  } else if (!password2.value) {
    alert("비밀번호를 한번 더 입력해주세요.");
    return;
  } else if (!email.value) {
    alert("이메일을 입력해주세요.");
    return;
  } else if (!mainbank.value) {
    alert("주거래 은행을 선택해주세요.");
    return;
  } else if (!location.value) {
    alert("거주지를 입력해주세요.");
    return;
  } else if (!selectedAge.value) {
    alert("나이대를 선택해주세요.");
    return;
  } else if (!selectedSalary.value) {
    alert("연봉 범위를 선택해주세요.");
    return;
  } else if (!selectedWealth.value) {
    alert("재산 범위를 선택해주세요.");
    return;
  } else if (password1.value !== password2.value) {
    alert("비밀번호가 일치하지 않습니다.");
    return;
  }
  const payload = {
    username: username.value,
    nickname: nickname.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
    mainbank: mainbank.value,
    location: location.value,
    age: age.value,
    wealth: wealth.money,
    salary: salary.money,
  };
  store.signUp(payload);
};
</script>

<style scoped>
.sign-up-header {
  font-family: "Noto Sans KR", sans-serif;
  font-size: 30px;
}
</style>
