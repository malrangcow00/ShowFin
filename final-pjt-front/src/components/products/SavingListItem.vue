<template>
    <div>
        <div>
            {{ saving.dcls_month  }}
        </div>
        <div>
            {{ saving.fin_prdt_cd }}
        </div>
        <div>
            {{ saving.kor_co_nm }}
        </div>
        <div>
            {{ saving.fin_prdt_nm }}
        </div>
        <div>
            {{ saving.etc_note }}
        </div>
        <div>
            {{ saving.join_deny }}
        </div>
        <div>
            {{ saving.join_member }}
        </div>
        <div>
            {{ saving.join_way }}
        </div>
        <div>
            {{ saving.spcl_cnd }}
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