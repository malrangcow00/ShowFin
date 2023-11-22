<template>
  <v-card class="mx-auto my-8" max-width="500" elevation="4" outlined>
    <v-card-title class="title-style">
      {{ props.article.title }}
    </v-card-title>

    <v-card-subtitle>
      <v-row>
        <v-col>
          <p>글 번호 : {{ props.article.id }}</p>
          <p>작성자 : {{ props.article.username }}</p>
          <p>글 분류 : {{ props.article.category }}</p>
        </v-col>
      </v-row>
    </v-card-subtitle>

    <v-card-actions>
      <v-row>
        <v-col>
          <v-btn
            :to="{ name: 'ArticleDetail', params: { id: props.article.id } }"
            outlined
            color="primary"
            class="font-weight-bold"
          >
            자세히 보기
          </v-btn>
        </v-col>
      </v-row>
    </v-card-actions>
  </v-card>
</template>

<script setup>
import { RouterLink } from "vue-router";

const props = defineProps({
  article: Object,
});
</script>

<style scoped>
.title-style {
  text-decoration: none;
  font-family: "Noto Sans KR", sans-serif;
  font-size: 1.5rem;
}
</style>
