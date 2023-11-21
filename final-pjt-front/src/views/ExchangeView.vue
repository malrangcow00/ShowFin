<template>
    <div>
        <select v-model="fromCurrency" @change="calculateExchange">
            <!-- 환율 정보에서 가져온 통화 목록 -->
            <option v-for="currency in currencies" :key="currency.code" :value="currency.code">
                {{ currency.name }}
            </option>
        </select>

        <input type="number" v-model="fromAmount" @input="calculateExchange">

        <select v-model="toCurrency" @change="calculateExchange">
            <!-- 환율 정보에서 가져온 통화 목록 -->
            <option v-for="currency in currencies" :key="currency.code" :value="currency.code">
                {{ currency.name }}
            </option>
        </select>

        <input type="number" v-model="toAmount" @input="calculateExchange">
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            currencies: [], // 환율 정보를 담을 배열
            fromCurrency: '', // 변환하고자 하는 통화 코드
            toCurrency: '', // 변환될 통화 코드
            fromAmount: 0, // 변환하고자 하는 금액
            toAmount: 0 // 변환된 금액
        };
    },
    created() {
        // 환율 정보를 가져오는 API 엔드포인트
        const apiUrl = 'http://127.0.0.1:8000/api/exchange_info/'; // API 엔드포인트

        // Axios를 사용하여 환율 정보 가져오기
        axios.get(apiUrl)
            .then(response => {
                this.currencies = response.data; // API로부터 받은 환율 정보를 배열에 저장
                this.fromCurrency = this.currencies[0].code; // 기본으로 첫 번째 통화를 선택
                this.toCurrency = this.currencies[1].code; // 기본으로 두 번째 통화를 선택
                this.calculateExchange(); // 초기 변환율 계산
            })
            .catch(error => {
                console.error('Error fetching currency data:', error);
            });
    },
    // axios({
    //           //request
    //           method: "get",
    //           url: 'http://127.0.0.1:8000/api/exchange_info/',
    //       })
    // .then(function (response) {
    //     console.log(response.data);
    //     // console.log(response.data[0].cur_unit);
    //     // const selectCurrency1 = document.getElementById('currency1');
    //     // const selectCurrency2 = document.getElementById('currency2');
    //     for (let i = response.data.length-1; i >= 0; i--) {
    //         const option1 = document.createElement('option');
    //         option1.value = response.data[i].cur_unit;
    //         option1.text = response.data[i].cur_unit;
    //         currency1.add(option1);
    //         const option2 = document.createElement('option');
    //         option2.value = response.data[i].cur_unit;
    //         option2.text = response.data[i].cur_unit;
    //         currency2.add(option2);
    //     }
    // })
    //     .catch(function (error) {
    //         console.log(error);
    //     });
    methods: {
        calculateExchange() {
            // 변환하고자 하는 금액과 환율을 기반으로 계산
            const fromRate = this.getExchangeRate(this.fromCurrency);
            const toRate = this.getExchangeRate(this.toCurrency);

            this.toAmount = (this.fromAmount * toRate) / fromRate || 0;
        },
        getExchangeRate(currencyCode) {
            // 선택한 통화 코드에 해당하는 환율 정보 반환
            const currency = this.currencies.find(currency => currency.code === currencyCode);
            return currency ? currency.rate : 1; // 기본값으로 1 설정
        }
    }
};


</script>



<style scoped>
select {
    text-align: right;
}
#currency1, #currency2 {
    width: 80px;
}
input {
    width: 200px;
    text-align: right;
}
span {
    font-size: 5px;
}
</style>