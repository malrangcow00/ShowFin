<template>
  <div>
    <i
      @click="router.go(-1)"
      class="fa-solid fa-arrow-right-to-bracket fa-rotate-180 h3 me-4 d-flex justify-content-end"
      style="cursor: pointer"
    ></i>
    <v-col></v-col>
    <div class="row gx-5">
      <h1>
        <i
          class="fa-regular fa-address-card fa-beat-fade"
          style="color: #feb4f8"
        ></i>
        가입한 상품
      </h1>
      <hr />
      <div class="col-2">
        <div class="list-group list-group-flush">
          <RouterLink
            :to="{ name: 'UserDeposit' }"
            class="list-group-item text-primary fs-5 fw-bold"
          >
            가입한 상품
          </RouterLink>
          <RouterLink
            :to="{ name: 'AccountDetailView' }"
            class="list-group-item list-group-item-action text-primary"
          >
            MY PAGE
          </RouterLink>
        </div>
      </div>
      <div class="col-10">
        <nav class="d-flex justify-content-end">
          <button
            @click="router.push({ name: 'UserDeposit' })"
            class="btn btn-outline-primary rounded-pill me-2"
          >
            예금 상품 조회
          </button>
          <button
            @click="router.push({ name: 'UserSaving' })"
            class="btn btn-outline-primary rounded-pill me-2"
          >
            적금 상품 조회
          </button>
          <button
            @click="router.push({ name: 'UserLoan' })"
            class="btn btn-outline-warning rounded-pill me-2"
          >
            전세 대출 조회
          </button>
        </nav>
        <v-divider></v-divider>

        <table class="table table-hover table-striped">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">금융 회사명</th>
              <th scope="col">금융 상품명</th>
              <th scope="col">적립 유형</th>
              <th scope="col" class="text-center">6개월</th>
              <th scope="col" class="text-center">12개월</th>
              <th scope="col" class="text-center">24개월</th>
              <th scope="col" class="text-center">36개월</th>
              <th scope="col" class="text-center">가입 여부</th>
            </tr>
          </thead>
          <tbody class="accordion accordion-flush" id="accordionFlushExample">
            <SavingListItem
              v-for="saving in store.userInfo?.subscribed_savings"
              :key="saving.id"
              :saving="saving"
              @click="goToDetail(saving.id)"
              style="cursor: pointer"
            />
          </tbody>
        </table>
        <div
          v-if="chartData.length > 0"
          style="width: 2000px; height: 400px; margin: 50px; margin-right: auto"
        >
          <canvas canvas id="myChart"></canvas>
        </div>
        <div v-else>
          <h1 style="text-align: center" class="text-secondary">
            가입한 상품이 없습니다.
          </h1>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from "vue";
import { RouterLink, useRouter } from "vue-router";
import SavingListItem from "@/components/products/SavingListItem.vue";
import { useAccountStore } from "@/stores/accounts.js";

const store = useAccountStore();
const router = useRouter();

onMounted(() => {
  store.getSavings();
  store.sortSavingsBy = null;
  renderChart();
});

const goToDetail = function (id) {
  router.push({ name: "SavingDetail", params: { id } });
};

const chartData = ref([]);
store.userInfo.subscribed_savings.forEach((element) => {
  chartData.value.push({
    fin_prdt_nm: element.fin_prdt_nm,
    intr_rate: element.savingoptions_set[0].intr_rate,
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
          backgroundColor: "rgba(242, 165, 255, 0.5)", // 막대 색상
          borderColor: "rgba(242, 0, 255, 0.51)", // 막대 테두리 색상
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
