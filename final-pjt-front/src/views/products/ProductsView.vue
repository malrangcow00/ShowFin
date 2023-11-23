<template>
  <div>
    <div class="row">
      <header class="d-flex">
          <nav class="navbar navbar-expand-lg navbar-light bg-light">
              <a class="navbar-brand">
                  <h1>상품 비교</h1>
              </a>
              <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarNav">
                  <ul class="navbar-nav">
                      <li class="nav-item active">
                          <a class="nav-link">
                              <RouterLink :to="{ name: 'ProductsView' }">예금</RouterLink>
                              <span class="sr-only">(current)</span>
                          </a>
                      </li>
                      <li class="nav-item">
                          <a class="nav-link">
                              <RouterLink :to="{ name: 'SavingList' }">적금</RouterLink>
                          </a>
                      </li>
                      <li class="nav-item">
                          <a class="nav-link">
                              <RouterLink :to="{ name: 'LoanList' }">전세자금대출</RouterLink>
                          </a>
                      </li>
                  </ul>
              </div>
          </nav>
      </header>

      <div class="col-2 mt-5">
        <h4>검색하기</h4>
        <hr />

        <label for="bank-select" class="mb-2">은행을 선택하세요</label>
        <select id="bank-select" v-model="store.selectedBank" class="product-selector">
          <option selected>전체</option>
          <option v-for="bank in store.bankList" :key="bank.id">
            {{ bank }}
          </option>
        </select>
      </div>

      <div class="col-10">
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
                  'bg-success text-white': store.sortDepositsBy === 6,
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
                  'bg-success text-white': store.sortDepositsBy === 12,
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
                  'bg-success text-white': store.sortDepositsBy === 24,
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
                  'bg-success text-white': store.sortDepositsBy === 36,
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
    -webkit-appearance:none; /* for chrome */

    appearance:none;
}
.product-selector::-ms-expand{

    display:none;/*for IE10,11*/

}
.product-selector {
    background:url('../../../assets/bank_img/filterarrow.png') no-repeat 97% 50%/15px auto;
}
</style>
