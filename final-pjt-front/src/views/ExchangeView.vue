<template>
  <div>
    <h1>환율 계산기</h1>

    <div>
      <label class="select">
        <select
          name="currency1"
          id="currency1"
          @change="store.changeSelected1"
          v-model="store.selectedCurrency1"
          required
        >
          <!--<option value="" selected disabled hidden>USD</option>-->
          <option v-for="currency in store.exchange_data" :key="currency.cur_unit">{{ currency.cur_unit }}</option>

        </select><span>　</span>
      </label>

      <input type="text" @keyup="store.inputMoney1" v-model="store.money1" />
    </div>

    <div>
      <label class="select">
        <select
          name="currency2"
          id="currency2"
          @change="store.changeSelected2"
          v-model="store.selectedCurrency2"
          required
        >
          <!--<option value="" selected disabled hidden>KRW</option>-->
          <option v-for="currency in store.exchange_data" :key="currency.cur_unit">{{ currency.cur_unit }}</option>

        </select><span>　</span>
      </label>

      <input type="text" @keyup="store.inputMoney2" v-model="store.money2" />
    </div>
  </div>
</template>

<script setup>
import {onMounted, ref, watch} from "vue";
import { useExchangeStore } from "@/stores/exchange";


const store = useExchangeStore();

const money1 = ref(store.money1);
const money2 = ref(store.money2);
const selectedCurrency1 = ref(store.selectedCurrency1);
const selectedCurrency2 = ref(store.selectedCurrency2);

onMounted(() => {
    store.getExchange();
});

// 입력 값과 선택된 화폐를 감시하고 변경될 때마다 업데이트
watch(money1, () => {
    store.inputMoney1();
});

watch(money2, () => {
    store.inputMoney2();
});

watch(selectedCurrency1, () => {
    store.changeSelected1();
});

watch(selectedCurrency2, () => {
    store.changeSelected2();
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
    width: 500px;
    text-align: right;
    border: 1px solid black;
    padding: 9px;
    border-radius: 5px;
}
span {
  font-size: 5px;
}
</style>
