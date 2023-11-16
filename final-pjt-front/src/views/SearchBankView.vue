<template>
  <div>
      <div id="map" style="width:100%;height:350px;"></div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

let map = null;
let infowindow = null;
let ps = null;

const initialMap = () => {
    // 마커를 클릭하면 장소명을 표출할 인포윈도우 입니다
    var infowindow = new kakao.maps.InfoWindow({zIndex:1});
    // 지도를 표시할 div
    var mapContainer = document.getElementById('map'),
        mapOptions = {
            // 지도의 초기 중심좌표
            center: new kakao.maps.LatLng(37.566826, 126.9786567),
            // 지도의 초기 확대 레벨
            level: 3,
    };

    // 지도를 생성합니다
    var map = new kakao.maps.Map(mapContainer, mapOptions);

    // 장소 검색 객체를 생성합니다
    var ps = new kakao.maps.services.Places(map);

    // 키워드로 장소를 검색합니다
    ps.keywordSearch('서울특별시 강남구 국민은행', placesSearchCB);
};


// 키워드 검색 완료 시 호출되는 콜백함수 입니다
function placesSearchCB (data, status, pagination) {
    if (status === kakao.maps.services.Status.OK) {

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정하기위해
        // LatLngBounds 객체에 좌표를 추가합니다
        var bounds = new kakao.maps.LatLngBounds();

        for (var i=0; i<data.length; i++) {
            displayMarker(data[i]);
            bounds.extend(new kakao.maps.LatLng(data[i].y, data[i].x));
        }

        // 검색된 장소 위치를 기준으로 지도 범위를 재설정합니다
        map.setBounds(bounds);
    }
}

// 지도에 마커를 표시하는 함수입니다
function displayMarker(place) {

    // 마커를 생성하고 지도에 표시합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: new kakao.maps.LatLng(place.y, place.x)
    });

    // 마커에 클릭이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
        // 마커를 클릭하면 장소명이 인포윈도우에 표출됩니다
        infowindow.setContent('<div style="padding:5px;font-size:12px;">' + place.place_name + '</div>');
        infowindow.open(map, marker);
    });
}

onMounted(async () => {
  if (window.kakao && window.kakao.maps) {
    initialMap();
    console.log('if b',infowindow)
  } else {
    const script = document.createElement('script');
    /* global kakao */
    script.src = `//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=${fbdd32eecea9ea022e10dec2254581c7}&libraries=services`;
    document.head.appendChild(script);
    script.onload = () => {
      kakao.maps.load(initialMap);
    }
  }
});


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#map {
  width: 400px;
  height: 400px;
}
</style>
