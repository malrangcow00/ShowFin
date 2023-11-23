<template>
  <div>
    <div class="row">
        <header class="d-flex justify-content-between align-items-center">
            <h1>상품 비교</h1>
            <div>
                <h2 class="d-inline-block mr-3">
                    <RouterLink :to="{ name: 'ProductsView' }" :class="{ 'nav-link-router-active': $route.name === 'ProductsView' }">예금</RouterLink>
                </h2>
                <h2 class="d-inline-block mr-3">
                    <RouterLink :to="{ name: 'SavingList' }" :class="{ 'nav-link-router-active': $route.name === 'SavingList' }">적금</RouterLink>
                </h2>
                <h2 class="d-inline-block">
                    <RouterLink :to="{ name: 'LoanList' }" :class="{ 'nav-link-router-active': $route.name === 'LoanList' }">전세자금대출</RouterLink>
                </h2>
            </div>
        </header>

      <div class="col-2 mt-5">
        <h4>검색하기</h4>
        <hr />

        <label for="bank-select" class="mb-2">은행을 선택하세요</label>
        <select
          class="form-select product-selector"
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
        <table class="table table-hover table-striped">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">금융 회사명</th>
              <th scope="col">금융 상품명</th>
              <th scope="col">대출 유형</th>
              <th scope="col" class="text-center">최저 이율</th>
              <th scope="col" class="text-center">최고 이율</th>
              <th scope="col" class="text-center">평균 이율</th>
              <th scope="col" class="text-center">가입 여부</th>
            </tr>
          </thead>
          <tbody class="accordion accordion-flush" id="accordionFlushExample">
            <LoanListItem
              v-for="loan in store.loans"
              :key="loan.id"
              :loan="loan"
              @click="goToDetail(loan.id)"
              style="cursor: pointer"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useRouter, RouterLink, onBeforeRouteLeave } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";
import LoanListItem from "@/components/products/LoanListItem.vue";

const router = useRouter();
const store = useAccountStore();

onMounted(() => {
  store.getLoans();
});

const goToDetail = function (id) {
  router.push({ name: "LoanDetail", params: { id } });
};

onBeforeRouteLeave(() => {
  store.selectedBank = "전체";
});
</script>

<style scoped>
.nav-link-router-active {
    text-decoration: underline; /* 밑줄 스타일 */
    font-weight: bold; /* 강조를 위해 폰트 굵기 변경 */
}
.product-selector {
    font-size: 25px;
    font-family: Georgia, "Malgun Gothic", serif;
    border-bottom: 1px solid #ced4da;
//text-align: right;
    -webkit-appearance:none; /* for chrome */

    appearance:none;
}
.product-selector::-ms-expand{

    display:none;

}
.product-selector {
    background:url('../../../assets/bank_img/filterarrow.png') no-repeat 97% 50%/15px auto;
}
</style>
