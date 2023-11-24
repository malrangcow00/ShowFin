<template>
  <div class="carousel">
      <v-carousel
          cycle
          :height="680"
          hide-delimiter-background
          :show-arrows="false"
          class="carousel-inner"
      >
          <RouterLink :to="{ name: 'ProductsView' }">
          <v-carousel-item
              src="../assets/main/comparing.png"
              class="carousel-item"
          ></v-carousel-item>
          </RouterLink>

          <!-- 알고리즘 추천 서비스 활성화시 RouterLink 수정 -->
          <RouterLink :to="{ name: 'RecommendLoan' }">
          <v-carousel-item
              src="../assets/main/algo.jpg"
              class="carousel-item"
          ></v-carousel-item>
          </RouterLink>

          <RouterLink :to="{ name: 'ArticleView' }">
          <v-carousel-item
              src="../assets/main/event.jpg"
              class="carousel-item"
          ></v-carousel-item>
          </RouterLink>
      </v-carousel>
  </div>
    <div class="bg-img">
        <v-img
            :width="1000"
            :height="1000"
            aspect-ratio="16/9"
            src="../assets/main/bono.png"
            class="bono"
        ></v-img>
        <v-img
            :width="1000"
            :height="1000"
            aspect-ratio="16/9"
            src="../assets/main/choonsik.png"
            class="choonsik"
        ></v-img>
    </div>
</template>


<script setup>

import {RouterLink} from "vue-router";
</script>

<style scoped>
.carousel {
    display: flex;
    justify-content: center;
}
a {
    //width: 35%;
    height: 100%;
    z-index: 1;
}
.carousel-inner {
    //width: 35%;
    height: 100%;
    z-index: 1;
}
.carousel-item {
    //width: 50%;
    height: 100%;
    //z-index: 1;
}
.bono {
    position: absolute;
    top: 5%;
    left: -15%;
    z-index: 1;
}
.choonsik {
    position: absolute;
    top: -10%;
    left: 70%;
    z-index: 1;
}
</style>
