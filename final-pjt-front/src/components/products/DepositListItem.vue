<template>
    <div>
        <div>
            {{ deposit.id }}
        </div>
        <div>
            {{ deposit.fin_prdt_cd }}
        </div>
        <div>
            {{ deposit.kor_co_nm }}
        </div>
        <div>
            {{ deposit.fin_prdt_nm }}
        </div>
        <div>
            {{ deposit.etc_note }}
        </div>
        <div>
            {{ deposit.join_deny }}
        </div>
        <div>
            {{ deposit.join_member }}
        </div>
        <div>
            {{ deposit.join_way }}
        </div>
        <div>
            {{ deposit.spcl_cnd }}
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