<template>
    <div>
<h1>예/적금 상품 리스트</h1>
        <div>
            <RouterLink :to="{ name: 'DepositsView' }">예금 상품</RouterLink> |
            <RouterLink :to="{ name: 'SavingsView' }">적금 상품</RouterLink>
        </div>
        <div>
            {{ options }}
        </div>
        <!--&lt;!&ndash;<div>&ndash;&gt;-->
        <!--<div v-for="option in store.depositOptions">-->
        <!--    &lt;!&ndash;<vue-good-table :columns="columns" :rows="store.depositOptions">&ndash;&gt;-->
        <!--    <vue-good-table :columns="columns" :rows="option">-->
        <!--    </vue-good-table>-->
        <!--</div>-->
    </div>
</template>

<script setup>
import {RouterLink, RouterView, useRouter } from "vue-router";
import { onMounted, computed } from "vue";
import 'vue-good-table-next/dist/vue-good-table-next.css'
import { VueGoodTable } from 'vue-good-table-next';
import { useProductStore } from "@/stores/products";

const store = useProductStore();
const router = useRouter();

const finPrdtCd = computed(() => router.currentRoute.value.params.fin_prdt_cd);


const columns = [
    { label: '공시 제출월', field: 'dcls_month' },
    { label: '금융회사 코드', field: 'fin_co_no' },
    { label: '금융상품 코드', field: 'fin_prdt_cd' },
    { label: '저축 금리 유형', field: 'intr_rate_type' },
    { label: '저축 금리 유형명', field: 'intr_rate_type_nm' },
    { label: '저축 기간', field: 'save_trm' },
    { label: '저축 금리', field: 'intr_rate' },
    { label: '최고 우대금리', field: 'intr_rate2' },
];

// router.push로 가져온 주소값을 통해 해당 상품의 상세 정보를 가져온다.
onMounted(() => {
    store.getDepositOptions(finPrdtCd.value);
})
</script>

<style lang="scss" scoped>

</style>