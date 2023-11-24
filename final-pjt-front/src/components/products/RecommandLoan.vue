<template>
    <v-container>
        <v-row
        ><i
            @click="router.go(-1)"
            class="fa-solid fa-arrow-right-to-bracket fa-rotate-180 h3 me-4 d-flex justify-content-end"
            style="cursor: pointer"
        ></i
        ></v-row>
        <v-card class="mx-auto pa-5" style="width: 60%">
            <v-card-title>
                <h1 class="mb-3">
                    금융
                    <i class="fa-solid fa-question fa-shake" style="color: #ff0000"></i>
                    몰라도 전세대출 가능해 👍
                </h1>
            </v-card-title>
            <v-divider></v-divider>
            <v-card-text>
                <form @submit.prevent="recommandLoan">
                    <v-row align="center">
                        <v-col cols="12" class="w-100">
                            <v-text-field
                                v-model="jeonsePrice"
                                label="전세금액을 입력해 주세요"
                                placeholder="숫자만 입력해주세요"
                            ></v-text-field>
                        </v-col>
                    </v-row>
                    <v-row>
                        <v-col justify="end" class="w-50">
                            <v-btn class="btn-primary text-success" @click="recommandLoan">
                                도와줘 ShowFin 🧚‍♂️
                            </v-btn>
                        </v-col>
                    </v-row>
                </form>

                <v-divider></v-divider>

                <v-card
                    v-if="sortLoans.length > 0"
                    @click="goToDetail(sortLoans[0].id)"
                    class="pa-5"
                >
                    <v-card-title>
                        <h2>
                            {{ sortLoans[0].kor_co_nm }} - {{ sortLoans[0].fin_prdt_nm }}
                        </h2>
                    </v-card-title>
                    <v-divider></v-divider>
                    <v-card-text>
                        <p v-if="extractMaxLTV(sortLoans[0].loan_lmt) > 0">
                            최대 LTV: {{ extractMaxLTV(sortLoans[0].loan_lmt) }}%
                        </p>
                        <p>
                            최대 대출금액:
                            {{
                                (
                                    (extractMaxLTV(sortLoans[0].loan_lmt) * jeonsePrice) /
                                    100
                                ).toLocaleString("ko-KR")
                            }}원
                        </p>
                        <p>
                            월 최저 상환금액:
                            {{
                                (
                                    (((extractMaxLTV(sortLoans[0].loan_lmt) * jeonsePrice) /
                                            100 /
                                            12) *
                                        sortLoans[0].jeonseloanoptions_set[0].lend_rate_min) /
                                    100
                                ).toLocaleString("ko-KR")
                            }}원
                        </p>
                        <p>
                            월 최대 상환금액:
                            {{
                                (
                                    (((extractMaxLTV(sortLoans[0].loan_lmt) * jeonsePrice) /
                                            100 /
                                            12) *
                                        sortLoans[0].jeonseloanoptions_set[0].lend_rate_max) /
                                    100
                                ).toLocaleString("ko-KR")
                            }}원
                        </p>
                        <!-- 다른 대출 정보 출력 로직 추가 -->
                    </v-card-text>
                </v-card>
            </v-card-text>
        </v-card>
    </v-container>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { useRouter, RouterLink } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";

const router = useRouter();
const store = useAccountStore();
const jeonsePrice = ref(null);
const sortLoans = ref([]);

const recommandLoan = () => {
    if (!jeonsePrice.value) {
        alert("전세금액을 입력해주세요.");
        return;
    } else if (isNaN(jeonsePrice.value)) {
        alert("전세금액은 숫자만 입력 가능합니다.");
        return;
    }
    sortLoans.value = [...store.loans].sort((a, b) => {
        const maxLoanAmountA =
            (extractMaxLTV(a.loan_lmt) * jeonsePrice.value) / 100; // loan_lmt : 대출 한도
        const maxLoanAmountB =
            (extractMaxLTV(b.loan_lmt) * jeonsePrice.value) / 100;

        const minRepaymentA =
            (((extractMaxLTV(a.loan_lmt) * jeonsePrice.value) / 100 / 12) *
                a.jeonseloanoptions_set[0].lend_rate_min) /
            100;
        const minRepaymentB =
            (((extractMaxLTV(b.loan_lmt) * jeonsePrice.value) / 100 / 12) *
                b.jeonseloanoptions_set[0].lend_rate_min) /
            100;

        // Sorting logic: maxLoanAmount를 기준으로 내림차순으로 정렬하고, minRepayment를 기준으로 오름차순으로 정렬
        if (maxLoanAmountB !== maxLoanAmountA) {
            return maxLoanAmountB - maxLoanAmountA;
        } else {
            return minRepaymentA - minRepaymentB;
        }
    });
};

// 각 대출의 "loan_lmt"에서 최대 LTV 추출하는 함수
const extractMaxLTV = (loanLimit) => {
    // "loan_lmt" 값이 존재하는 경우에만 추출 작업 수행
    if (loanLimit) {
        // "LTV"를 찾아서 그 뒤의 문자열에서 숫자를 추출
        const index = loanLimit.lastIndexOf("%");
        const extractedValue = index !== -1 ? loanLimit.slice(index - 2) : null;

        // 숫자만 추출하여 반환
        const extractedNumber = extractedValue ? parseInt(extractedValue) : null;

        // 추출된 값이 숫자인 경우에만 반환
        return extractedNumber !== null && !isNaN(extractedNumber)
            ? extractedNumber
            : null;
    } else {
        return null;
    }
};
const goToDetail = function (id) {
    router.push({ name: "LoanDetail", params: { id } });
};
</script>

<style scoped>
/* 필요한 스타일 추가 */
</style>