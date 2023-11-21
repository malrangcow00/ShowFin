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

const store = useProductStore();
const savings = store.getSavingList()
console.log(savings)
</script>

<style scoped>

</style>