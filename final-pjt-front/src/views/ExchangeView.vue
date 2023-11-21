<template>
  <div>
    <h1>환율 계산기</h1>

    <div>
      <label class="select">
        <select
          name="currency1"
          id="currency1"
          @change="calculateExchange1"
          required
        >
          <option value="" selected disabled hidden>USD</option></select
        ><span>　</span>
      </label>

      <input type="number" @input="calculateExchange1" v-model="value1" />
    </div>

    <div>
      <label class="select">
        <select
          name="currency2"
          id="currency2"
          @change="calculateExchange2"
          required
        >
          <option value="" selected disabled hidden>KRW</option></select
        ><span>　</span>
      </label>

      <input type="number" @input="calculateExchange2" v-model="value2" />
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";

const exchange_info = {};

// 환율 정보를 가져오는 API 엔드포인트
const django_exchange_url = "http://127.0.0.1:8000/api/exchange_info/";

// Axios를 사용하여 환율 정보 가져오기
axios({
  method: "get",
  url: django_exchange_url,
  responseType: "json",
})
  .then(function (response) {
    const currency1 = document.getElementById("currency1");
    const currency2 = document.getElementById("currency2");
    // console.log(response.data)
    for (let i = response.data.length - 1; i >= 0; i--) {
      exchange_info[response.data[i].cur_unit] = response.data[i].deal_bas_r;
      const option1 = document.createElement("option");
      const option2 = document.createElement("option");
      option1.value = response.data[i].cur_unit;
      option2.value = response.data[i].cur_unit;
      option1.text = response.data[i].cur_unit;
      option2.text = response.data[i].cur_unit;
      currency1.add(option1);
      currency2.add(option2);
    }
    console.log(exchange_info);
    value2.value = Number(exchange_info["USD"].replace(",", ""));
  })
  .catch((error) => {
    console.error(error);
  });

const value1 = ref(1);
const value2 = ref();

const getExchangeRate = () => {
  const currency1 = document.getElementById("currency1");
  const currency2 = document.getElementById("currency2");
  console.log(currency1.value);
  console.log(exchange_info[currency1.value]);
  const rate =
    Number(exchange_info[currency1.value].replace(",", "")) /
    Number(exchange_info[currency2.value].replace(",", ""));
  console.log(rate);
  return rate;
};

const calculateExchange1 = () => {
  const currency1 = document.getElementById("currency1");
  const currency2 = document.getElementById("currency2");
  const rate = getExchangeRate(currency1, currency2);
  //   const input1 = document.getElementById("input1");
  //   const input2 = document.getElementById("input2");
  //   input2 = input1 * rate;
};

const calculateExchange2 = () => {
  const currency1 = document.getElementById("currency1");
  const currency2 = document.getElementById("currency2");
  const rate = getExchangeRate(currency1, currency2);
  const input2 = document.getElementById("input2");
  const input1 = document.getElementById("input1");
  // input1 = input2 / rate;
};
</script>

<style scoped>
select {
  text-align: right;
}
#currency1,
#currency2 {
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
