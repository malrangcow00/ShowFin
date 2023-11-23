<template>
  <div>
    <div class="row">
        <header class="d-flex justify-content-between align-items-center">
            <h1>상품 비교</h1>
            <div>
                <h2 class="d-inline-block mr-3">
                    <RouterLink
                        :to="{ name: 'ProductsView' }"
                        :class="{ 'nav-link-router-active': $route.name === 'ProductsView' }"
                        style="text-decoration: none;"
                    >
                        예금
                    </RouterLink>
                </h2>
                <h2 class="d-inline-block mr-3">
                    <RouterLink
                        :to="{ name: 'SavingList' }"
                        :class="{ 'nav-link-router-active': $route.name === 'SavingList' }"
                        style="text-decoration: none;"
                    >
                        적금
                    </RouterLink>
                </h2>
                <h2 class="d-inline-block">
                    <RouterLink
                        :to="{ name: 'LoanList' }"
                        :class="{ 'nav-link-router-active': $route.name === 'LoanList' }"
                        style="text-decoration: none;"
                    >
                        전세자금대출
                    </RouterLink>
                </h2>
            </div>
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
              <th scope="col">적립 유형</th>
              <th
                scope="col"
                class="text-center"
                @click="sortSavings(6)"
                :class="{ 'bg-success text-white': store.sortSavingsBy === 6 }"
                style="cursor: pointer"
              >
                6개월 <i class="fa-solid fa-caret-down"></i>
              </th>
              <th
                scope="col"
                class="text-center"
                @click="sortSavings(12)"
                :class="{ 'bg-success text-white': store.sortSavingsBy === 12 }"
                style="cursor: pointer"
              >
                12개월 <i class="fa-solid fa-caret-down"></i>
              </th>
              <th
                scope="col"
                class="text-center"
                @click="sortSavings(24)"
                :class="{ 'bg-success text-white': store.sortSavingsBy === 24 }"
                style="cursor: pointer"
              >
                24개월 <i class="fa-solid fa-caret-down"></i>
              </th>
              <th
                scope="col"
                class="text-center"
                @click="sortSavings(36)"
                :class="{ 'bg-success text-white': store.sortSavingsBy === 36 }"
                style="cursor: pointer"
              >
                36개월 <i class="fa-solid fa-caret-down"></i>
              </th>
              <th scope="col" class="text-center">가입 여부</th>
            </tr>
          </thead>
          <tbody class="accordion accordion-flush" id="accordionFlushExample">
            <SavingListItem
              v-for="saving in store.savings"
              :key="saving.id"
              :saving="saving"
              @click="goToDetail(saving.id)"
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
import SavingListItem from "@/components/products/SavingListItem.vue";

const router = useRouter();
const store = useAccountStore();

onMounted(() => {
  store.getSavings();
  store.sortSavingsBy = null;
});

const goToDetail = function (id) {
  router.push({ name: "SavingDetail", params: { id } });
};

const sortSavings = function (save_trm) {
  store.sortSavings(save_trm);
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
