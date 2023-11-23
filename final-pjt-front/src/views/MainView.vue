<template>
  <div>
    <h1>MainView</h1>
      <v-carousel
          cycle
          height="800"
          hide-delimiter-background
          show-arrows="hover"
      >
          <v-carousel-item
              src="https://www.jungle.co.kr/image/ea06cd0346fa8777cb624e3f"
              cover
          ></v-carousel-item>

          <v-carousel-item
              src="https://blog.kakaocdn.net/dn/bKy6Mm/btqKfqu72Ga/05lByPgN2H0tYN3lHP3VU1/img.png"
              cover
          ></v-carousel-item>

          <v-carousel-item
              src="https://cdn.maily.so/7o7grtuc8937i1sd30x6ezf68b4g"
              cover
          ></v-carousel-item>
      </v-carousel>
  </div>
</template>


<script setup></script>

<style scoped>

.carousel-inner > .item > img {
    min-width: 50% !important;
    min-height: 200px !important;
}
</style>
