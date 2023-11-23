<template>
  <div>
    <div class="row gx-5">
      <h1>가입한 상품</h1>
      <hr />
      <div class="col-2">
        <div class="list-group list-group-flush">
          <RouterLink
            :to="{ name: 'UserDeposit' }"
            class="list-group-item text-success fs-5 fw-bold"
          >
            가입한 상품
          </RouterLink>
          <RouterLink
            :to="{ name: 'AccountDetailView' }"
            class="list-group-item list-group-item-action text-secondary"
          >
            MY PAGE
          </RouterLink>
        </div>
      </div>
      <div class="col-10">
        <nav>
          <RouterLink :to="{ name: 'UserDeposit' }">
            예금 상품 조회
          </RouterLink>
          |
          <RouterLink :to="{ name: 'UserSaving' }"> 적금 상품 조회 </RouterLink>
          |
          <RouterLink :to="{ name: 'UserLoan' }">
            전세 대출 상품 조회
          </RouterLink>
        </nav>

        <table class="table table-hover table-striped">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">금융 회사명</th>
              <th scope="col">금융 상품명</th>
              <th scope="col" class="text-center">6개월</th>
              <th scope="col" class="text-center">12개월</th>
              <th scope="col" class="text-center">24개월</th>
              <th scope="col" class="text-center">36개월</th>
              <th scope="col" class="text-center">가입 여부</th>
            </tr>
          </thead>
          <tbody class="accordion accordion-flush" id="accordionFlushExample">
            <DepositListItem
              v-for="deposit in store.userInfo?.subscribed_deposit"
              :key="deposit.fin_prdt_cd"
              :deposit="deposit"
              @click="goToDetail(deposit.fin_prdt_cd)"
              style="cursor: pointer"
            />
          </tbody>
        </table>
      </div>
    </div>
  </div>
  <div style="width: 2000px; height: 400px">
    <canvas canvas id="myChart"></canvas>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { RouterLink, useRouter } from "vue-router";
import DepositListItem from "@/components/products/DepositListItem.vue";
import { useAccountStore } from "@/stores/accounts.js";

const store = useAccountStore();
const router = useRouter();

onMounted(() => {
  store.getDeposits();
  store.sortDepositsBy = null;
  renderChart();
});

const goToDetail = function (fin_prdt_cd) {
  router.push({ name: "DepositDetail", params: { fin_prdt_cd } });
};

const chartData = ref([]);
console.log(typeof store.userInfo.subscribed_deposit);
console.log(store.userInfo.subscribed_deposit);
store.userInfo.subscribed_deposit.forEach((element) => {
  chartData.value.push({
    fin_prdt_nm: element.fin_prdt_nm,
    intr_rate: element.depositoptions_set[0].intr_rate,
  });
});

console.log(chartData);

function renderChart() {
  const ctx = document.getElementById("myChart").getContext("2d");

  const labels = chartData.value.map((item) => item.fin_prdt_nm);
  const data = chartData.value.map((item) => item.intr_rate);

  new Chart(ctx, {
    type: "bar",
    data: {
      labels: labels,
      datasets: [
        {
          label: "Interest Rate",
          data: data,
          backgroundColor: "rgba(75, 192, 192, 0.2)", // 막대 색상
          borderColor: "rgba(75, 192, 192, 1)", // 막대 테두리 색상
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
        },
      },
    },
  });
}
</script>

<style scoped></style>
