<template>
  <div>
    <h1>환율 계산기</h1>

    <div>
      <label class="select">
        <select
          name="currency1"
          id="currency1"
          @change="changeseledted(this)"
          required
        >
          <option value="" selected disabled hidden>USD</option>
          <option v-for="currency in store.exchange_data" value="{{ currency.cur_unit }}">{{ currency.cur_unit }}</option>

        </select><span>　</span>
      </label>

      <input type="number" @input="calculateExchange1" v-model="value1" />
    </div>

    <div>
      <label class="select">
        <select
          name="currency2"
          id="currency2"
          @change="changeseledted(this)"
          required
        >
          <option value="" selected disabled hidden>KRW</option>
          <option v-for="currency in store.exchange_data" value="{{ currency.cur_unit }}">{{ currency.cur_unit }}</option>

        </select><span>　</span>
      </label>

      <input type="number" @input="calculateExchange2" v-model="value2" />
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import {onMounted, ref} from "vue";
import { useExchangeStore } from "@/stores/exchange";

const store = useExchangeStore();


const value1 = ref(1);
const value2 = ref(store.exchange_data.USD.deal_bas_r);

const changeseledted = (target) => {
    console.log(target.value);
    console.log(target.options[target.selectedIndex].text);
}
//
//
// const getExchangeRate = () => {
//   const currency1 = document.getElementById("currency1");
//   const currency2 = document.getElementById("currency2");
//   console.log(currency1.value);
//   console.log(exchange_info[currency1.value]);
//   const rate =
//     Number(exchange_info[currency1.value].replace(",", "")) /
//     Number(exchange_info[currency2.value].replace(",", ""));
//   console.log(rate);
//   return rate;
// };
//
// const calculateExchange1 = () => {
//   const currency1 = document.getElementById("currency1");
//   const currency2 = document.getElementById("currency2")
//   console.log(currency1)
//   console.log(currency2)
//   const rate = getExchangeRate(currency1, currency2);
//   //   const input1 = document.getElementById("input1");
//   //   const input2 = document.getElementById("input2");
//   //   input2 = input1 * rate;
// };
//
// const calculateExchange2 = () => {
//   const currency1 = document.getElementById("currency1");
//   const currency2 = document.getElementById("currency2");
//   const rate = getExchangeRate(currency1, currency2);
//   const input2 = document.getElementById("input2");
//   const input1 = document.getElementById("input1");
//   // input1 = input2 / rate;
// };



onMounted(() => {
    const store = useExchangeStore();
    store.getExchange();
});
</script>

<style scoped>
select {
  text-align: right;
}
#currency1,
#currency2 {
    width: 80px;
    border: 1px solid black;
    padding: 9px;
    border-radius: 5px;
    margin: 10px 0px;
}
input {
    width: 200px;
    text-align: right;
    border: 1px solid black;
    padding: 9px;
    border-radius: 5px;
}
span {
  font-size: 5px;
}
</style>
