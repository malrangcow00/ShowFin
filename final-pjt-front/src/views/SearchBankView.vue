<template>
    <div>
        <h1>Search Bank</h1>
        <label class="select">
            <select name="city" id="city" v-model="selectedCityCode" @click="cityselect" required>
                <option v-for="city in cities" :value="city.code" :key="city.name">
                    {{ city.name }}
                </option>
            </select><span>　</span>
        </label>
        <label class="select">
            <select name="district" id="district" @click="districtselect" required>
                <option v-for="district in computedDistricts" :value="district" :key="district">
                    {{ district }}
                </option>
            </select><span>　</span>
        </label>
        <!--<select name="bank" id="bank" required>-->
        <!--    <option v-for="bank in banks" :value="bank" :key="bank"></option>-->
        <!--    {{ bank }}-->
        <!--</select><span>　</span>-->
        <button @click="searchBanks">Search</button>
    </div>
    <br>
    <div id="map"></div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import axios from 'axios';

const city_data = 'https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern=*00000000'

const cities = ref([]);
const selectedCityCode = ref(null);
// const districts = ref([]);


const cityselect = () => {
    axios({
        //request
        method: "get",
        url: city_data,
        responseType: "json",
    })
        .then(function (response) {
            cities.value = response.data.regcodes;
        })
        .catch(function (error) {
            console.log(error);
        });
}


const district_data = 'https://grpc-proxy-server-mkvo6j4wsq-du.a.run.app/v1/regcodes?regcode_pattern={tmpcode}*00000';

const computedDistricts = computed(() => {
    const districtsArray = [];

    if (selectedCityCode.value) {
        const url = district_data.replace('{tmpcode}', selectedCityCode.value.substr(0, 2));

        axios({
            method: 'get',
            url: url,
            responseType: 'json',
        })
            .then(function (response) {
                for (let i = 1; i < response.data.regcodes.length; i++) {
                    const tmp = response.data.regcodes[i].name.split(' ')[1];
                    if (!districtsArray.includes(tmp)) {
                        districtsArray.push(tmp);
                    }
                }
            })
            .catch(function (error) {
                console.error(error);
            });
    }

    return districtsArray;
});

const searchBanks = () => {
    const keyword = `${selectedCityCode.value} ${computedDistricts.value.join('-')}`;
    console.log(keyword);
    // Use the keyword for further processing or searching
};

const mapId = 'map';
let infowindow = null;
let map = null;

const initMap = () => {
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
    searchPlace('서울특별시 강남구 신한은행');
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
