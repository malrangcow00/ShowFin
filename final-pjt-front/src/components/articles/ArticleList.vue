<template>
  <v-container>
    <h3>게시글 목록</h3>

    <v-row>
      <v-col v-for="article in store.articles" :key="article.id" cols="4">
        <ArticleListItem :article="article" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import ArticleListItem from "@/components/articles/ArticleListItem.vue";
const store = useAccountStore();
</script>

<style scoped></style>
