<template>
    <tr
        v-if="
      store.selectedBank === '전체' || store.selectedBank === loan.kor_co_nm
    "
        class="accordion-item"
    >
        <th>{{ loan.id }}</th>
        <th>{{ loan.kor_co_nm }}</th>
        <th>{{ loan.fin_prdt_nm }}</th>
        <th>{{ rpay_type_nm }}</th>
        <th class="text-center">{{ lend_rate_min }}</th>
        <th class="text-center">{{ lend_rate_max }}</th>
        <th class="text-center">{{ lend_rate_avg }}</th>
        <th class="text-center">
            <i v-if="isSubscribed" class="fa-solid fa-heart fa-beat text-danger"></i>
            <i v-else class="fa-regular fa-heart text-warning"></i>
        </th>
    </tr>
</template>

<script setup>
import { ref, computed } from "vue";
import { useAccountStore } from "@/stores/accounts.js";

const store = useAccountStore();
const props = defineProps({
    loan: Object,
});
const rpay_type_nm = ref("");
const lend_rate_min = ref("-");
const lend_rate_max = ref("-");
const lend_rate_avg = ref("-");

props.loan.jeonseloanoptions_set.forEach((option) => {
    rpay_type_nm.value = option.rpay_type_nm;
    lend_rate_min.value = option.lend_rate_min || "-";
    lend_rate_max.value = option.lend_rate_max || "-";
    lend_rate_avg.value = option.lend_rate_avg || "-";
});

const isSubscribed = computed(() => {
    if (store.isLogIn) {
        return store.userInfo.subscribed_jeonse_loan.some(
            (product) => product.id === props.loan.id
        );
    } else {
        return false;
    }
});
</script>

<style scoped></style>