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
                    // console.log(exchange_data.value)
                    money2.value = exchange_data.value.USD.deal_bas_r
                    // selectedCurrency1.value = 'USD'
                    // selectedCurrency2.value = 'KRW'
                })
                .catch(error => console.log(error))
        };
        const calculateExchangeRate = () => {

            const rate1 = exchange_data.value[selectedCurrency1.value]?.deal_bas_r || 1;
            const rate2 = exchange_data.value[selectedCurrency2.value]?.deal_bas_r || 1;

            if (rate2 === 0) {
                // rate2가 0일 때, 다른 처리를 해줄 수 있도록 원하는 로직 추가
                return 0; // 혹은 다른 기본값으로...
            }

            return rate1 / rate2
        }
        const changeSelected1 = () => {
            const calculatedValue = Number(money1.value.replace(/,/g, '')) * calculateExchangeRate();
            money2.value = addCommas(calculatedValue.toFixed(2));
        }

        const changeSelected2 = () => {
            const calculatedValue = Number(money1.value.replace(/,/g, '')) / calculateExchangeRate();
            money2.value = addCommas(calculatedValue.toFixed(2));
        }

        const inputMoney1 = () => {
            const calculatedValue = Number(money1.value.replace(/,/g, '')) * calculateExchangeRate();
            money2.value = addCommas(calculatedValue.toFixed(2));
        }

        const inputMoney2 = () => {
            const calculatedValue = Number(money2.value.replace(/,/g, '')) / calculateExchangeRate();
            money1.value = addCommas(calculatedValue.toFixed(2));
        }

        const addCommas = (value) => {
            return value.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
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