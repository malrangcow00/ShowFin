<template>
    <div>
        <div class="d-flex justify-content-between align-items-center">
            <i
                @click="router.go(-1)"
                class="fa-solid fa-chevron-left h3 me-4"
                style="cursor: pointer"
            ></i>
            <h1 class="d-inline">{{ product.fin_prdt_nm }}</h1>
            <button
                v-if="isSubscribed"
                @click="subscribe"
                class="btn btn-outline-success"
            >
                탈퇴하기
            </button>
            <button v-else @click="subscribe" class="btn btn-success">
                가입하기
            </button>
        </div>
        <hr />
        <table class="table">
            <thead>
            <tr>
                <th scope="col">대출 상환 유형</th>
                <th scope="col">금리 유형</th>
                <th scope="col">담보 유형</th>
                <th scope="col">최저 이율</th>
                <th scope="col">최고 이율</th>
                <th scope="col">평균 이율</th>
            </tr>
            </thead>
            <tbody>
            <tr v-for="product in product.jeonseloanoptions_set">
                <td>{{ product.rpay_type_nm }}</td>
                <td>{{ product.lend_rate_type_nm }}</td>
                <td>{{ product.mrtg_type_nm }}</td>
                <td>{{ product.lend_rate_min || "-" }}</td>
                <td>{{ product.lend_rate_max || "-" }}</td>
                <td>{{ product.lend_rate_avg || "-" }}</td>
            </tr>
            </tbody>
        </table>

        <table class="table table-borderless">
            <tbody>
            <tr>
                <th scope="row" class="text-nowrap">공시 제출월</th>
                <td>{{ product.dcls_month }}</td>
            </tr>
            <tr>
                <th scope="row" class="text-nowrap">금융 회사</th>
                <td>{{ product.kor_co_nm }}</td>
            </tr>
            <tr>
                <th scope="row" class="text-nowrap">연체 이자율</th>
                <td>{{ product.dly_rate }}</td>
            </tr>
            <tr>
                <th scope="row" class="text-nowrap">중도상환 수수료</th>
                <td>{{ product.erly_rpay_fee }}</td>
            </tr>
            <tr>
                <th scope="row" class="text-nowrap">대출 유형</th>
                <td>{{ product.fin_prdt_nm }}</td>
            </tr>
            <tr>
                <th scope="row" class="text-nowrap">가입 방법</th>
                <td>{{ product.join_way }}</td>
            </tr>
            <tr>
                <th scope="row" class="text-nowrap">세금</th>
                <td>{{ product.loan_inci_expn }}</td>
            </tr>
            <tr>
                <th scope="row" class="text-nowrap">대출 한도</th>
                <td>{{ product.loan_lmt }}</td>
            </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";
import { ref, computed } from "vue";

const route = useRoute();
const router = useRouter();
const store = useAccountStore();
const product = ref(
    store.loans.find((product) => product.id == route.params.id)
);
const rpay_type_nm = ref([]);
const lend_rate_min = ref([]);
const lend_rate_max = ref([]);
const lend_rate_avg = ref([]);
const lend_rate_type_nm = ref([]);

product.value.jeonseloanoptions_set.forEach((option) => {
    lend_rate_type_nm.value.push(option.lend_rate_type_nm);
    rpay_type_nm.value = option.rpay_type_nm;
    lend_rate_min.value = option.lend_rate_min || "-";
    lend_rate_max.value = option.lend_rate_max || "-";
    lend_rate_avg.value = option.lend_rate_avg || "-";
});

const subscribe = function () {
    if (store.isLogIn) {
        store.subscribe("jeonse", route.params.id);
    } else {
        window.alert("로그인 후 가입 가능합니다. 로그인 페이지로 이동합니다.");
        router.push({ name: "LogInView" });
    }
};

const isSubscribed = computed(() => {
    if (store.isLogIn) {
        return store.userInfo.subscribed_jeonse_loan.some(
            (product) => product.id == route.params.id
        );
    } else {
        return false;
    }
});
</script>

<style scoped></style>