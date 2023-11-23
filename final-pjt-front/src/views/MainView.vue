<template>
  <div class="carousel">
      <v-carousel
          cycle
          :height="500"
          hide-delimiter-background
          :show-arrows="false"
          class="carousel-inner"
      >
          <a href="http://localhost:5173/products">
          <v-carousel-item
              src="../assets/main/comparing.png"
              class="carousel-item"
          ></v-carousel-item>
          </a>

          <a href="http://localhost:5173/products">
          <v-carousel-item
              src="../assets/main/algo.jpg"
              class="carousel-item"
          ></v-carousel-item>
          </a>

          <a href="http://localhost:5173/articles">
          <v-carousel-item
              src="../assets/main/event.jpg"
              class="carousel-item"
          ></v-carousel-item>
          </a>
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
    //z-index: -1;
}
.choonsik {
    position: absolute;
    top: -10%;
    left: 70%;
    z-index: 1;
}
</style>
