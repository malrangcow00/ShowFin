<template>
    <tr
        v-if="
      store.selectedBank === '전체' || store.selectedBank === saving.kor_co_nm
    "
        class="accordion-item"
    >
        <th>{{ saving.id }}</th>
        <th>{{ saving.kor_co_nm }}</th>
        <th>{{ saving.fin_prdt_nm }}</th>
        <th>{{ saving.rsrv_type === "S" ? "정액적립식" : "자유적립식" }}</th>
        <th
            class="text-center"
            :class="{ 'bg-info bg-opacity-10': store.sortSavingsBy === 6 }"
        >
            {{ intr_rate_6 }}
        </th>
        <th
            class="text-center"
            :class="{ 'bg-info bg-opacity-10': store.sortSavingsBy === 12 }"
        >
            {{ intr_rate_12 }}
        </th>
        <th
            class="text-center"
            :class="{ 'bg-info bg-opacity-10': store.sortSavingsBy === 24 }"
        >
            {{ intr_rate_24 }}
        </th>
        <th
            class="text-center"
            :class="{ 'bg-info bg-opacity-10': store.sortSavingsBy === 36 }"
        >
            {{ intr_rate_36 }}
        </th>
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
    saving: Object,
});
const intr_rate_6 = ref("-");
const intr_rate_12 = ref("-");
const intr_rate_24 = ref("-");
const intr_rate_36 = ref("-");

props.saving.savingoptions_set.forEach((option) => {
    const save_trm = option.save_trm;
    if (save_trm === 6) {
        intr_rate_6.value = option.intr_rate;
    } else if (save_trm === 12) {
        intr_rate_12.value = option.intr_rate;
    } else if (save_trm === 24) {
        intr_rate_24.value = option.intr_rate;
    } else if (save_trm === 36) {
        intr_rate_36.value = option.intr_rate;
    }
});

const isSubscribed = computed(() => {
    if (store.isLogIn) {
        return store.userInfo.subscribed_savings.some(
            (product) => product.id === props.saving.id
        );
    } else {
        return false;
    }
});
</script>

<style scoped></style>