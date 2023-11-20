<template>
    <div>
        <h1>Search Bank</h1>
        <label class="select">
            <select name="city" id="city" @change="selectDistrict" required>
            </select><span>　</span>
        </label>
        <label class="select">
            <select name="district" id="district" required>
            </select><span>　</span>
        </label>
        <label class="select">
            <select name="bank" id="bank" required>
            </select><span>　</span>
        </label>
        <button @click="searchBanks">Search</button>
    </div>
    <br>
    <div id="map"></div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';

const city_data = 'https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=*00000000'

axios({
    //request
    method: "get",
    url: city_data,
    responseType: "json",
})
    .then(function (response) {
        const selectCity = document.getElementById('city');
        for (let i = 0; i < response.data.regcodes.length; i++) {
            if (i === 0) {
                const defaultSelectedCityCode = document.getElementById('city').value;
                const defaultUrl = district_data.replace('{tmpcode}', defaultSelectedCityCode.substr(0, 2));

                axios({
                    //request
                    method: "get",
                    url: defaultUrl,
                    responseType: "json",
                })
                    .then(function (response) {
                        const selectDistrict = document.getElementById('district');
                        for (let i = 1; i < response.data.regcodes.length; i++) {
                            const option = document.createElement('option');
                            // 중복 제거
                            if (response.data.regcodes[i].name.split(' ')[1] === response.data.regcodes[i - 1].name.split(' ')[1]) {
                                continue;
                            } else {
                                option.value = response.data.regcodes[i].code;
                            }
                            option.text = response.data.regcodes[i].name.split(' ')[1];
                            selectDistrict.add(option);
                        }
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            }
            const option = document.createElement('option');
            option.value = response.data.regcodes[i].code;
            option.text = response.data.regcodes[i].name;
            selectCity.add(option);
        }
    })
    .catch(function (error) {
        console.log(error);
    });


const district_data = 'https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern={tmpcode}*00000';

const selectDistrict = () => {
    // select city에서 선택한 option의 city.code값 호출
    const selectedCityCode = document.getElementById('city').value;
    const url = district_data.replace('{tmpcode}', selectedCityCode.substr(0, 2));

    axios({
        //request
        method: "get",
        url: url,
        responseType: "json",
    })
        .then(function (response) {
            const selectDistrict = document.getElementById('district');
            // option 초기화 방법 1
            selectDistrict.options.length = 0;
            // option 초기화 방법 2
            // while (selectDistrict.options.length > 0) {
            //     selectDistrict.remove(0);
            // }
            // option 초기화 방법 3
            // selectDistrict.innerHTML = '';
            for (let i = 1; i < response.data.regcodes.length; i++) {
                const option = document.createElement('option');
                // 중복 제거
                if (response.data.regcodes[i].name.split(' ')[1] === response.data.regcodes[i - 1].name.split(' ')[1]) {
                    continue;
                } else {
                    option.value = response.data.regcodes[i].code;
                }
                option.text = response.data.regcodes[i].name.split(' ')[1];
                selectDistrict.add(option);
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

// http://127.0.0.1:8000/api/products/get_banks/에서 bank 목록를 호출
axios({
    //request
    method: "get",
    url: 'http://127.0.0.1:8000/api/products/get_banks/',
})
    .then(function (response) {
        const selectBank = document.getElementById('bank');
        selectBank.options.length = 0;
        // console.log(response.data.company_name);
        for (let i = 0; i < response.data.company_name.length; i++) {
            const option = document.createElement('option');
            option.text = response.data.company_name[i];
            selectBank.add(option);
        }
    })
    .catch(function (error) {
        console.log(error);
    });

const searchBanks = () => {
    // select city에서 선택한 option의 city.name값 호출
    const selectedCityName = document.getElementById('city').options[document.getElementById('city').selectedIndex].text;
    // 로컬스토리지에 저장
    localStorage.setItem('city', selectedCityName);
    // select city에서 선택한 option의 city.name값 호출
    const selectedDistrictName = document.getElementById('district').options[document.getElementById('district').selectedIndex].text;
    // 로컬스토리지에 저장
    localStorage.setItem('district', selectedDistrictName);
    // select bank에서 선택한 option의 bank.name값 호출
    const selectedBankName = document.getElementById('bank').options[document.getElementById('bank').selectedIndex].text;
    // 로컬스토리지에 저장
    localStorage.setItem('bank', selectedBankName);
    const keyword = `${localStorage.getItem('city')} ${localStorage.getItem('district')} ${localStorage.getItem('bank')}`;
    initMap(keyword);
};

const mapId = 'map';
let infowindow = null;
let map = null;

const keyword = `${localStorage.getItem('city')} ${localStorage.getItem('district')} ${localStorage.getItem('bank')}`;

const initMap = (keyword) => {
    // Map container
    const mapContainer = document.getElementById(mapId);

    // Map options
    const mapOption = {
        center: new kakao.maps.LatLng(37.514575, 127.0495556),
        level: 3,
    };

    // Create the map
    map = new kakao.maps.Map(mapContainer, mapOption);

    // Initialize the infowindow
    infowindow = new kakao.maps.InfoWindow({ zIndex: 1 });

    // Perform the place search
    // searchPlace('서울특별시 강남구 신한은행');
    searchPlace(keyword);
};

const searchPlace = (keyword) => {
    const ps = new kakao.maps.services.Places();

    // Keyword search
    ps.keywordSearch(keyword, placesSearchCB);
};

const placesSearchCB = (data, status, pagination) => {
    if (status === kakao.maps.services.Status.OK) {
        // Create bounds
        const bounds = new kakao.maps.LatLngBounds();

        for (let i = 0; i < data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
        }

        // Set map bounds
        map.setBounds(bounds);
    }
};

const displayMarker = (place) => {
    const marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x),
    });

    kakao.maps.event.addListener(marker, 'click', () => {
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        infowindow.open(map, marker);
    });
};

onMounted(initMap);

</script>


<style scoped>
#map {
    width: 800px;
    height: 600px;
}
select {
    text-align: right;
}
#city {
    width: 120px;
}
#district {
    width: 75px;
}
#bank {
    width: 80px;
}
span {
    font-size: 5px;
}
</style>