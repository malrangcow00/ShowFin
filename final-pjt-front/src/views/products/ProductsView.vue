<template>
  <div>
    <div class="row">
      <i
        @click="router.go(-1)"
        class="fa-solid fa-arrow-right-to-bracket fa-rotate-180 h3 me-4 d-flex justify-content-end"
        style="cursor: pointer"
      ></i>
      <header class="d-flex">
        <h1>⚖️ 상품 비교</h1>
      </header>

      <div class="col-2 mt-5">
        <h4>검색하기</h4>
        <hr />
        <label for="bank-select" class="mb-2">은행을 선택하세요</label>
        <select
          class="form-select"
          id="bank-select"
          v-model="store.selectedBank"
        >
          <option selected>전체</option>
          <option v-for="bank in store.bankList" :key="bank.id">
            {{ bank }}
          </option>
        </select>
      </div>

      <div class="col-10">
        <nav class="d-flex justify-content-end">
          <button
            @click="router.push({ name: 'ProductsView' })"
            class="btn btn-outline-primary rounded-pill me-2"
          >
            예금
          </button>
          <button
            @click="router.push({ name: 'SavingList' })"
            class="btn btn-outline-primary rounded-pill me-2"
          >
            적금
          </button>
          <button
            @click="router.push({ name: 'LoanList' })"
            class="btn btn-outline-warning rounded-pill me-2"
          >
            전세자금대출
          </button>
        </nav>

        <v-divider></v-divider>

        <table class="table table-hover table-striped">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">금융 회사명</th>
              <th scope="col">금융 상품명</th>
              <th
                scope="col"
                class="text-center"
                @click="sortDeposits(6)"
                :class="{
                  'bg-primary text-white': store.sortDepositsBy === 6,
                }"
                style="cursor: pointer"
              >
                6개월 <i class="fa-solid fa-caret-down"></i>
              </th>
              <th
                scope="col"
                class="text-center"
                @click="sortDeposits(12)"
                :class="{
                  'bg-primary text-white': store.sortDepositsBy === 12,
                }"
                style="cursor: pointer"
              >
                12개월 <i class="fa-solid fa-caret-down"></i>
              </th>
              <th
                scope="col"
                class="text-center"
                @click="sortDeposits(24)"
                :class="{
                  'bg-primary text-white': store.sortDepositsBy === 24,
                }"
                style="cursor: pointer"
              >
                24개월 <i class="fa-solid fa-caret-down"></i>
              </th>
              <th
                scope="col"
                class="text-center"
                @click="sortDeposits(36)"
                :class="{
                  'bg-primary text-white': store.sortDepositsBy === 36,
                }"
                style="cursor: pointer"
              >
                36개월 <i class="fa-solid fa-caret-down"></i>
              </th>
              <th scope="col" class="text-center">가입 여부</th>
            </tr>
          </thead>
          <tbody class="accordion accordion-flush" id="accordionFlushExample">
            <DepositListItem
              v-for="deposit in store.deposits"
              :key="deposit"
              :deposit="deposit"
              @click="goToDetail(deposit.fin_prdt_cd)"
              style="cursor: pointer"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRouter, RouterLink, onBeforeRouteLeave } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";
import DepositListItem from "@/components/products/DepositListItem.vue";

const router = useRouter();
const store = useAccountStore();

onMounted(() => {
  store.getDeposits();
  store.sortDepositsBy = null;
});

const goToDetail = function (fin_prdt_cd) {
  router.push({ name: "DepositDetail", params: { fin_prdt_cd } });
};

const sortDeposits = function (save_trm) {
  store.sortDeposits(save_trm);
};

onBeforeRouteLeave(() => {
  store.selectedBank = "전체";
});
</script>

<style scoped>
.product-selector {
  font-size: 25px;
  font-family: Georgia, "Malgun Gothic", serif;
  border-bottom: 1px solid #ced4da;
  //text-align: right;
  -webkit-appearance: none; /* for chrome */

  appearance: none;
}
.product-selector::-ms-expand {
  display: none; /*for IE10,11*/
}
.product-selector {
  background: url("../../../assets/bank_img/filterarrow.png") no-repeat 97% 50%/15px
    auto;
}
</style>
