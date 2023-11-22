<template>
    <div>
        <vue-good-table :columns="columns" :rows="rows" />
    </div>
</template>

<script setup>
// Import the styles
import 'vue-good-table-next/dist/vue-good-table-next.css'
import { VueGoodTable } from 'vue-good-table-next';


const columns = [
    { label: '공시 제출월', field: 'name' },
    { label: '금융회사명', field: 'name' },
    { label: '상품명', field: 'name' },
    { label: '6개월', field: 'name' },
    { label: '12개월', field: 'name' },
    { label: '24개월', field: 'name' },
    { label: '36개월', field: 'name' },
];

const rows = [
    { id: 1, name: 'John', age: 20, createdAt: '', score: 0.03343 },
    { id: 2, name: 'Jane', age: 24, createdAt: '2011-10-31', score: 0.03343 },
    { id: 3, name: 'Susan', age: 16, createdAt: '2011-10-30', score: 0.03343 },
    { id: 4, name: 'Chris', age: 55, createdAt: '2011-10-11', score: 0.03343 },
    { id: 5, name: 'Dan', age: 40, createdAt: '2011-10-21', score: 0.03343 },
    { id: 6, name: 'John', age: 20, createdAt: '2011-10-31', score: 0.03343 },
];

</script>

<style lang="scss" scoped>

</style>