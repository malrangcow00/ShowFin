<template>
  <div>
    <div class="d-flex justify-content-between align-items-center">
      <i
        @click="router.go(-1)"
        class="fa-solid fa-chevron-left h3 me-4"
        style="cursor: pointer"
      ></i>
      <h1 class="d-inline">{{ product.fin_prdt_nm }}</h1>
      <button
        v-if="isSubscribed"
        @click="subscribe"
        class="btn btn-outline-success"
      >
        탈퇴하기
      </button>
      <button v-else @click="subscribe" class="btn btn-success">
        가입하기
      </button>
    </div>
    <hr />

    <table class="table">
      <thead>
        <tr>
          <th scope="col">저축 기간</th>
          <th scope="col">저축 금리 유형</th>
          <th scope="col">저축 금리</th>
          <th scope="col">최고 우대 금리</th>
        </tr>
      </thead>
      <tbody>
        <tr v-if="term_6">
          <th scope="row">6개월</th>
          <td>{{ term_6.intr_rate_type_nm }}</td>
          <td>{{ term_6.intr_rate }}</td>
          <td>{{ term_6.intr_rate2 }}</td>
        </tr>
        <tr v-if="term_12">
          <th scope="row">12개월</th>
          <td>{{ term_12.intr_rate_type_nm }}</td>
          <td>{{ term_12.intr_rate }}</td>
          <td>{{ term_12.intr_rate2 }}</td>
        </tr>
        <tr v-if="term_24">
          <th scope="row">24개월</th>
          <td>{{ term_24.intr_rate_type_nm }}</td>
          <td>{{ term_24.intr_rate }}</td>
          <td>{{ term_24.intr_rate2 }}</td>
        </tr>
        <tr v-if="term_36">
          <th scope="row">36개월</th>
          <td>{{ term_36.intr_rate_type_nm }}</td>
          <td>{{ term_36.intr_rate }}</td>
          <td>{{ term_36.intr_rate2 }}</td>
        </tr>
      </tbody>
    </table>

    <table class="table table-borderless">
      <tbody>
        <tr>
          <th scope="row" class="text-nowrap">공시 제출월</th>
          <td>{{ product.dcls_month }}</td>
        </tr>
        <tr>
          <th scope="row" class="text-nowrap">금융 회사</th>
          <td>{{ product.kor_co_nm }}</td>
        </tr>
        <tr>
          <th scope="row" class="text-nowrap">만기 후 이자율</th>
          <td>{{ product.mtrt_int }}</td>
        </tr>
        <tr>
          <th scope="row" class="text-nowrap">우대조건</th>
          <td>{{ product.spcl_cnd }}</td>
        </tr>
        <tr>
          <th scope="row" class="text-nowrap">가입 방법</th>
          <td>{{ product.join_way }}</td>
        </tr>
        <tr>
          <th scope="row" class="text-nowrap">유의사항</th>
          <td>{{ product.etc_note }}</td>
        </tr>
        <tr>
          <th scope="row" class="text-nowrap">최고한도</th>
          <td>{{ product.max_limit }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { useRoute, useRouter } from "vue-router";
import { useAccountStore } from "@/stores/accounts.js";
import { ref, computed } from "vue";

const route = useRoute();
const router = useRouter();
const store = useAccountStore();
const product = ref(
  store.deposits.find(
    (product) => product.fin_prdt_cd === route.params.fin_prdt_cd
  )
);

// console.log(product.value);

const term_6 = ref(null);
const term_12 = ref(null);
const term_24 = ref(null);
const term_36 = ref(null);

product.value.depositoptions_set.forEach((option) => {
  const save_trm = option.save_trm;
  if (save_trm === 6) {
    term_6.value = option;
  } else if (save_trm === 12) {
    term_12.value = option;
  } else if (save_trm === 24) {
    term_24.value = option;
  } else if (save_trm === 36) {
    term_36.value = option;
  }
});

const subscribe = function () {
  if (store.isLogIn) {
    store.subscribe("deposit", product.value.id);
  } else {
    window.alert("로그인 후 가입 가능합니다. 로그인 페이지로 이동합니다.");
    router.push({ name: "LogInView" });
  }
};

const isSubscribed = computed(() => {
  if (store.isLogIn) {
    return store.userInfo.subscribed_deposit.some(
      (product) => product.fin_prdt_cd === route.params.fin_prdt_cd
    );
  } else {
    return false;
  }
});
</script>

<style scoped></style>
