<template>
    <div>
        <h1>Exchange Rate Calculator</h1>
        <div>
            <label class="select">
                <select name="currency1" id="currency1" @change="selectCurrency" required>
                </select><span>　</span>
                <input type="number" id="input1">
            </label>
        </div>
        <div>
            <label class="select">
                <select name="currency2" id="currency2" @change="selectCurrency" required>
                </select><span>　</span>
                <input type="number" id="input2">
            </label>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, watch } from "vue";
import axios from "axios";

const input1 = document.getElementById('input1');
const input2 = document.getElementById('input2');
const currency1 = document.getElementById('currency1');
const currency2 = document.getElementById('currency2');

let prevInput1Value = input1.value;
let prevInput2Value = input2.value;

input1.addEventListener('input', updateInput1);
input2.addEventListener('input', updateInput2);
currency1.addEventListener('change', updateInput1);
currency2.addEventListener('change', updateInput2);


// 환율을 계산할 함수...




// input1 값 업데이트 함수
function updateInput1() {
    const val1 = parseFloat(input1.value);
    const cur1 = currency1.value;

    const exchangeRate = 1.5; // 임의의 환율 값 예시
    const calculated1to2 = val1 * exchangeRate;

    if (!isNaN(calculated1to2) && input1.value !== prevInput1Value) {
        prevInput1Value = input1.value;
        input2.value = calculated1to2.toFixed(2); // 결과를 소수점 2자리까지 표시
    }
}

// input2 값 업데이트 함수
function updateInput2() {
    const val2 = parseFloat(input2.value);
    const cur2 = currency2.value;

    const exchangeRate = 1.5; // 임의의 환율 값 예시
    const calculated2to1 = val2 / exchangeRate;

    if (!isNaN(calculated2to1) && input2.value !== prevInput2Value) {
        prevInput2Value = input2.value;
        input1.value = calculated2to1.toFixed(2); // 결과를 소수점 2자리까지 표시
    }
}





axios({
    //request
    method: "get",
    url: 'http://127.0.0.1:8000/api/exchange_info/',
})
    .then(function (response) {
        console.log(response.data);
        // console.log(response.data[0].cur_unit);
        // const selectCurrency1 = document.getElementById('currency1');
        // const selectCurrency2 = document.getElementById('currency2');
        for (let i = response.data.length-1; i >= 0; i--) {
            const option1 = document.createElement('option');
            option1.value = response.data[i].cur_unit;
            option1.text = response.data[i].cur_unit;
            currency1.add(option1);
            const option2 = document.createElement('option');
            option2.value = response.data[i].cur_unit;
            option2.text = response.data[i].cur_unit;
            currency2.add(option2);
        }
    })
    .catch(function (error) {
        console.log(error);
    });

</script>

<style scoped>
select {
    text-align: right;
}
#currency1, #currency2 {
    width: 80px;
}
input {
    width: 200px;
    text-align: right;
}
span {
    font-size: 5px;
}
</style>