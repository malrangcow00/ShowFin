<template>
  <div>
    <h1>커뮤니티 게시판이에요~</h1>
    <RouterLink :to="{ name: 'ArticleCreateView' }">게시글 생성</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useArticleStore } from "@/stores/articles.js";
import ArticleList from "@/components/articles/ArticleList.vue";
import { RouterLink } from "vue-router";

const store = useArticleStore();

onMounted(() => {
  store.getArticleList();
});
</script>

<style scoped></style>
