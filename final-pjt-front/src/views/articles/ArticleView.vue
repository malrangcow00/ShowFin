<template>
  <div>
    <h1>커뮤니티 게시판이에요~</h1>
    <RouterLink :to="{ name: 'ArticleCreate' }">게시글 생성</RouterLink>
    <ArticleList />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useArticleStore } from "@/stores/articles.js";
import { useAccountStore } from "@/stores/accounts.js";
import ArticleList from "@/components/articles/ArticleList.vue";
import { RouterLink } from "vue-router";

const articleStore = useArticleStore();

onMounted(() => {
  const accountStore = useAccountStore();
  articleStore.getArticleList(accountStore.token);
});
</script>

<style scoped></style>
