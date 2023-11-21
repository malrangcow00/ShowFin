import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useProductStore = defineStore(
    "prducts",
    () => {
        const deposits = ref([]);
        const savings = ref([]);
        const API_URL = import.meta.env.VITE_API_URL;
        const getDepositList = function () {
            axios({
                method: "GET",
                url: `${API_URL}/api/products/deposit_products/`,
                // header: { Authorization: `Token ${token.value}` },
            })
                .then((response) => {
                    console.log(response.data);
                    deposits.value = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        };
        const getSavingList = function () {
            axios({
                method: "GET",
                url: `${API_URL}/api/products/savings_products/`,
                // header: { Authorization: `Token ${token.value}` },
            })
                .then((response) => {
                    console.log(response.data);
                    savings.value = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        };

        return {
            API_URL,
            deposits,
            savings,
            getDepositList,
            getSavingList,
        };
    },
    { persist: true }
);
