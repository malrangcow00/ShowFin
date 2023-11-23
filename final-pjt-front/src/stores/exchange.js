import { ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useExchangeStore = defineStore(
    'exchange',
    () => {
        const exchange_data = ref({})
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
                })
                .catch(error => console.log(error))
        };
        return {
            exchange_data,
            getExchange,
        };
    },
    { persist: true }
)