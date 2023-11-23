<template>
    <div>
        <h1>예/적금 상품 리스트</h1>
        <div>
            <RouterLink :to="{ name: 'DepositsView' }">예금 상품</RouterLink> |
            <RouterLink :to="{ name: 'SavingsView' }">적금 상품</RouterLink>
        </div>
        <SavingListItem
            v-for="saving in store.savings"
            :key="saving.id"
            :saving="saving"
        />
    </div>
</template>

<script setup>
import {RouterLink, RouterView} from "vue-router";
import { useProductStore } from "@/stores/products";
import SavingListItem from "@/components/products/SavingListItem.vue";
// saving.id에 해당하는 options에서 intr_rate와 intr_rate2를 가져오도록 ...
// http://127.0.0.1:8000/api/products/deposit_product_options/'금융상품 코드'/


const store = useProductStore();
</script>

<style scoped>

</style>