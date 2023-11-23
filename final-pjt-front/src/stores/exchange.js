import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeStore = defineStore(
    'exchange',
    () => {
        const exchange_data = ref({})
        const money1 = ref(1)
        const money2 = ref(null)
        const selectedCurrency1 = ref('USD')
        const selectedCurrency2 = ref('KRW')
        const getExchange = function () {
            axios({
                method: "get",
                url: "http://127.0.0.1:8000/api/exchange_info/",
            })
                .then(function (response) {
                    for (let i = 0; i < response.data.length; i++) {
                        const curUnit = response.data[i].cur_unit
                        const dealBasR = response.data[i].deal_bas_r.replace(',', '')
                        exchange_data.value[curUnit] = {
                            cur_unit: curUnit,
                            deal_bas_r: Number(dealBasR),
                        }
                    }
                    console.log(exchange_data.value)
                    money2.value = exchange_data.value.USD.deal_bas_r
                    // selectedCurrency1.value = 'USD'
                    // selectedCurrency2.value = 'KRW'
                })
                .catch(error => console.log(error))
        };
        const calculateExchangeRate = () => {
            const rate1 = exchange_data.value[selectedCurrency1.value]?.deal_bas_r || 1;
            const rate2 = exchange_data.value[selectedCurrency2.value]?.deal_bas_r || 1;
            return (rate1 / rate2).toFixed(2);
        }
        const changeSelected1 = () => {
            money2.value = money1.value * calculateExchangeRate()
        }
        const changeSelected2 = () => {
            money2.value = money1.value / calculateExchangeRate()
        }
        const inputMoney1 = () => {
            money2.value = money1.value * calculateExchangeRate()
        }
        const inputMoney2 = () => {
            money1.value = money2.value / calculateExchangeRate()
        }

        return {
            exchange_data,
            getExchange,
            selectedCurrency1,
            selectedCurrency2,
            calculateExchangeRate,
            money1,
            money2,
            changeSelected1,
            changeSelected2,
            inputMoney1,
            inputMoney2,
        };
    },
    { persist: true }
)