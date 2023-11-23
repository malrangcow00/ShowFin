<template>
    <div>
        <!--금융상품 번호 : {{ saving.id }}-->
        <div>
            금융회사 명 : {{ saving.kor_co_nm }}
        </div>
        <div>
            금융상품 명 : {{ saving.fin_prdt_nm }}
        </div>
        <div>
            기타 유의사항 : {{ saving.etc_note }}
        </div>
        <div>
            <p>가입제한 : {{ saving.join_deny }}</p>
            <p>(1: 제한없음, 2:서민전용, 3:일부제한)</p>
        </div>
        <div>
            가입대상 : {{ saving.join_member }}
        </div>
        <div>
            우대조건 : {{ saving.spcl_cnd }}
        </div>
    </div>
    <hr>
</template>

<script setup>
defineProps({
    saving: Object,
});
</script>

<style scoped>

</style>