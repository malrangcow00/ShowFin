<template>
    <i
        @click="router.go(-1)"
        class="fa-solid fa-arrow-right-to-bracket fa-rotate-180 h3 me-4 d-flex justify-content-end"
        style="cursor: pointer"
    ></i>
    <v-container>
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card class="pa-8" max-width="100%">
                    <v-card-title>
                        <h1 class="sign-up-header mb-5">회원정보수정</h1>
                        <hr class="my-3" />
                    </v-card-title>
                    <v-form @submit.prevent="updateAccountInfo">
                        <v-row>
                            <v-col cols="12">
                                <v-text-field
                                    :model-value="username"
                                    label="ID"
                                    disabled
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
                        <v-row justify="space-around">
                            <v-btn @click.prevent="goAccountDelete">회원탈퇴</v-btn>
                            <v-btn type="submit" color="primary">회원정보수정</v-btn>
                            <v-btn @click.prevent="goChangePassword">비밀번호변경</v-btn>
                        </v-row>
                    </v-form>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { ref, onMounted } from "vue";
import router from "@/router";

onMounted(() => {
    selectedAge.value = getSelectedAge();
    selectedSalary.value = getSelectedSalary();
    selectedWealth.value = getSelectedWealth();
});

const store = useAccountStore();

const username = ref(store.userInfo.username);
const nickname = ref(store.userInfo.nickname);
const email = ref(store.userInfo.email);
const age = ref(store.userInfo.age);
const mainbank = ref(store.userInfo.mainbank);
const location = ref(store.userInfo.location);
const wealth = ref(store.userInfo.wealth);
const salary = ref(store.userInfo.salary);

const selectedAge = ref(null);
const selectedSalary = ref(null);
const selectedWealth = ref(null);

const rules = {
    required: (input) => !!input || "필수 항목입니다.",
};

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

const getSelectedAge = function () {
    const idx = ageValue.findIndex((v) => v.value === age.value);
    return ageValue[idx].text;
};

const getSelectedWealth = function () {
    const idx = optionValue.findIndex((v) => v.money === wealth.value);
    return optionValue[idx].text;
};

const getSelectedSalary = function () {
    const idx = optionValue.findIndex((v) => v.money === salary.value);
    return optionValue[idx].text;
};

const updateAccountInfo = function () {
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

    if (!nickname.value) {
        alert("닉네임을 입력해주세요.");
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
    }

    const payload = {
        username: username.value,
        nickname: nickname.value,
        email: email.value,
        mainbank: mainbank.value,
        location: location.value,
        age: age.value,
        wealth: wealth.money,
        salary: salary.money,
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