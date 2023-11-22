<template>
<div>
    <h1>예/적금 상품 리스트</h1>
    <div>
    <RouterLink :to="{ name: 'DepositsView' }">예금 상품</RouterLink> |
    <RouterLink :to="{ name: 'SavingsView' }">적금 상품</RouterLink>
    </div>
    <div>
        <vue-good-table :columns="columns" :rows="store.deposits" @row-click="depositDetail">
        </vue-good-table>
    </div>
</div>
</template>

<script setup>
import {RouterLink, RouterView, useRouter } from "vue-router";
import { useProductStore } from "@/stores/products";
import 'vue-good-table-next/dist/vue-good-table-next.css'
import { VueGoodTable } from 'vue-good-table-next';
import DepositOptions from "@/components/products/DepositOptions.vue";

const store = useProductStore();
const router = useRouter();

const columns = [
    { label: '금융 상품 코드', field: 'dcls_month' },
    { label: '저축 금리 유형', field: 'kor_co_nm' },
    { label: '저축 금리 유형명', field: 'fin_prdt_nm' },
    { label: '가입 방법', field: 'join_way' },
    { label: '저축 기간', field: 'etc_note' },
    { label: '저축 금리', field: 'spcl_cnd' },
    { label: '최고 우대금리', field: 'spcl_cnd' },
    // { label: '6개월', field: 'name' },
    // { label: '12개월', field: 'name' },
    // { label: '24개월', field: 'name' },
    // { label: '36개월', field: 'name' },
];

const depositDetail = (params) => {
    const options = store.getDepositOptions(params.row.fin_prdt_cd)
    router.push({ name: "DepositOptions", params : { fin_prdt_cd: params.row.fin_prdt_cd } });
}
</script>

<style scoped>

</style>