import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useProductStore = defineStore(
    "prducts",
    () => {
        const deposits = ref([]);
        const savings = ref([]);
        const depositOptions = ref({});
        const savingOptions = ref([]);
        const API_URL = import.meta.env.VITE_API_URL;
        const router = useRouter();
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
        const getDepositOptions = function (fin_prdt_cd) {
            axios({
                method: "GET",
                url: `${API_URL}/api/products/deposit_products/${fin_prdt_cd}/`,
                // header: { Authorization: `Token ${token.value}` },
            })
                .then((response) => {
                    // console.log(response.data);
                    // depositOptions.value = response.data;
                    for (let i = 0; i < response.data.length; i++) {
                        depositOptions[i] = response.data[i];
                    }
                    console.log(depositOptions);
                    return depositOptions;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
        const getSavingOptions = function (fin_prdt_cd) {
            axios({
                method: "GET",
                url: `${API_URL}/api/products/savings_products/${fin_prdt_cd}/`,
                // header: { Authorization: `Token ${token.value}` },
            })
                .then((response) => {
                    console.log(response.data);
                    savingOptions.value = response.data;
                })
                .catch((error) => {
                    console.log(error);
                });
        }
        return {
            API_URL,
            deposits,
            savings,
            getDepositList,
            getSavingList,
            depositOptions,
            savingOptions,
            getDepositOptions,
            getSavingOptions,
        };
    },
    { persist: true }
);
