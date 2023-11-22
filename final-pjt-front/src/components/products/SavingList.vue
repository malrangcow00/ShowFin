<template>
    <div>
        <h1>예/적금 상품 리스트</h1>
        <div>
            <RouterLink :to="{ name: 'DepositsView' }">예금 상품</RouterLink> |
            <RouterLink :to="{ name: 'SavingsView' }">적금 상품</RouterLink>
        </div>
        <div>
            <vue-good-table :columns="columns" :rows="store.savings" />
        </div>
    </div>
</template>

<script setup>
import {RouterLink, RouterView} from "vue-router";
import { useProductStore } from "@/stores/products";


import 'vue-good-table-next/dist/vue-good-table-next.css'
import { VueGoodTable } from 'vue-good-table-next';

const columns = [
    { label: '금융 상품 코드', field: 'dcls_month' },
    { label: '금융회사명', field: 'kor_co_nm' },
    { label: '상품명', field: 'fin_prdt_nm' },
    { label: '가입 방법', field: 'join_way' },
    { label: '내용', field: 'etc_note' },
    { label: '우대 조건', field: 'spcl_cnd' },
    // { label: '6개월', field: 'name' },
    // { label: '12개월', field: 'name' },
    // { label: '24개월', field: 'name' },
    // { label: '36개월', field: 'name' },
];


const store = useProductStore();
</script>

<style scoped>

</style>