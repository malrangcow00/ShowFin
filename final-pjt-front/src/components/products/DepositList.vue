<template>
<div>
    <h1>예/적금 상품 리스트</h1>
    <div>
    <RouterLink :to="{ name: 'DepositsView' }">예금 상품</RouterLink> |
    <RouterLink :to="{ name: 'SavingsView' }">적금 상품</RouterLink>
    </div>
    <DepositListItem
        v-for="deposit in store.deposits"
        :key="deposit.id"
        :deposit="deposit"
    />
</div>
</template>

<script setup>
import {RouterLink, RouterView} from "vue-router";
import { useProductStore } from "@/stores/products";
import DepositListItem from "@/components/products/DepositListItem.vue";

const store = useProductStore();
const deposits = store.getDepositList()
console.log(deposits)
</script>

<style scoped>

</style>