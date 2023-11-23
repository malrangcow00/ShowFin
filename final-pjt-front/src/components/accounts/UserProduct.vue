<template>
  <div class="col-2">
    <div class="list-group list-group-flush">
      <RouterLink
        :to="{ name: 'UserDeposit' }"
        class="list-group-item list-group-item-action text-secondary"
      >
        가입한 상품
      </RouterLink>
      <RouterLink
        :to="{ name: 'AccountUpdateView' }"
        class="list-group-item text-success fs-5 fw-bold"
      >
        기본 정보 수정
      </RouterLink>
    </div>
  </div>
</template>

<script setup></script>

<style scoped></style>
