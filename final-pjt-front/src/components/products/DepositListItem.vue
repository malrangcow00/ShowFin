<template>
    <div>
        <div>
            공시 제출월 : {{ deposit.dcls_month  }}
        </div>
        <div>
            금융상품 코드 : {{ deposit.fin_prdt_cd }}
        </div>
        <div>
            금융회사 명 : {{ deposit.kor_co_nm }}
        </div>
        <div>
            금융상품 명 : {{ deposit.fin_prdt_nm }}
        </div>
        <div>
            기타 유의사항 : {{ deposit.etc_note }}
        </div>
        <div>
            <p>가입제한 : {{ deposit.join_deny }}</p>
            <p>(1: 제한없음, 2:서민전용, 3:일부제한)</p>
        </div>
        <div>
            가입대상 : {{ deposit.join_member }}
        </div>
        <div>
            가입 방법 : {{ deposit.join_way }}
        </div>
        <div>
            우대조건 : {{ deposit.spcl_cnd }}
        </div>
    </div>
    <hr>
</template>

<script setup>
defineProps({
    deposit: Object,
});
</script>

<style scoped>

</style>