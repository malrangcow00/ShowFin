<template>
    <v-container>
        <v-card class="elevation-10 pa-6">
            <v-card-title>
                <h1 class="headline">비밀번호를 입력해 주세요 😭</h1>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
                <form @submit.prevent="deleteAccount">
                    <v-row>
                        <v-col cols="12">
                            <v-text-field
                                v-model.trim="password"
                                :append-inner-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                                clearable
                                :rules="[rules.required, rules.min]"
                                label="비밀번호"
                                id="password"
                                type="password"
                                @click:append-inner="showPassword = !showPassword"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row justify="end">
                        <v-btn type="submit" color="error" class="w-25">회원탈퇴</v-btn>
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
    required: (value) => !!value || "필수 항목입니다.",
    min: (value) => (value && value.length >= 8) || "최소 8자 이상 입력하세요.",
};

const showPassword = ref(false);
const password = ref(null);

const deleteAccount = function () {
    const payload = {
        password: password.value,
    };
    store.deleteAccount(payload);
};
</script>

<style scoped>
.elevation-10 {
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
</style>