<template>
  <v-container>
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
import { useArticleStore } from "@/stores/articles.js";
import { useAccountStore } from "@/stores/accounts.js";
import ArticleList from "@/components/articles/ArticleList.vue";

const articleStore = useArticleStore();

onMounted(() => {
  const accountStore = useAccountStore();
  articleStore.getArticleList(accountStore.token);
});
</script>

<style scoped>
.article-heading {
  font-size: 2rem;
  font-weight: bold;
  margin: 1rem;
}
</style>
