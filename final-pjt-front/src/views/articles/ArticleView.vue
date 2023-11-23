<template>
  <v-container>
    <i
      @click="router.go(-1)"
      class="fa-solid fa-arrow-right-to-bracket fa-rotate-180 h3 me-4 d-flex justify-content-end"
      style="cursor: pointer"
    ></i>
    <v-col></v-col>
    <v-row align="center" justify="space-between">
      <v-col-3>
        <v-heading class="article-heading">커뮤니티 게시판</v-heading>
      </v-col-3>
      <v-col-2>
        <v-btn :to="{ name: 'ArticleCreate' }" color="green-darken-1"
          >게시글 생성</v-btn
        >
      </v-col-2>
    </v-row>
  </v-container>
  <v-container>
    <v-row justify="center">
      <v-col cols="12">
        <ArticleList />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { onMounted } from "vue";
import { useAccountStore } from "@/stores/accounts.js";
import ArticleList from "@/components/articles/ArticleList.vue";

onMounted(() => {
  const store = useAccountStore();
  store.getArticleList(store.token);
});
</script>

<style scoped>
.article-heading {
  font-size: 2rem;
  font-weight: bold;
  margin: 1rem;
}
</style>
