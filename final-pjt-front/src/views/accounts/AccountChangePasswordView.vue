<template>
    <v-container>
        <v-card class="elevation-10 pa-6">
            <v-card-title>
                <h1 class="headline">새로운 비밀번호를 입력하세요! 💁</h1>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
                <form @submit.prevent="changePassword">
                    <v-row>
                        <v-col cols="12">
                            <v-text-field
                                v-model.trim="oldPassword"
                                :append-inner-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                :type="show1 ? 'text' : 'password'"
                                :rules="[rules.required, rules.min]"
                                label="기존 비밀번호"
                                id="old_password"
                                type="password"
                                @click:append-inner="show1 = !show1"
                            ></v-text-field>
                        </v-col>
                        <v-col cols="12">
                            <v-text-field
                                v-model.trim="newPassword"
                                :append-inner-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                                :type="show2 ? 'text' : 'password'"
                                :rules="[rules.required, rules.min]"
                                label="새 비밀번호"
                                id="new_password"
                                type="password"
                                @click:append-inner="show2 = !show2"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row justify="end">
                        <v-btn class="my-5" type="submit" color="primary" large
                        >비밀번호 변경</v-btn
                        >
                    </v-row>
                </form>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";
const store = useAccountStore();

const rules = {
    required: (input) => !!input || "필수 항목입니다.",
    min: (input) => (input && input.length >= 8) || "최소 8자 이상 입력하세요.",
};

const show1 = ref(false);
const show2 = ref(false);

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

<style scoped>
.elevation-10 {
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>