<template>
  <div>
    <h3>Article List</h3>

    <ArticleListItem
      v-for="article in store.articles"
      :key="article.id"
      :article="article"
    />
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/articles.js";
import ArticleListItem from "@/components/articles/ArticleListItem.vue";
const store = useArticleStore();
// console.log(store.articles);
</script>

<style scoped></style>
