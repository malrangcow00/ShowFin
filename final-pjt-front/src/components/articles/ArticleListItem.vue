<template>
  <div>
    <h5>글 번호 : {{ article.id }}</h5>
    <p>작성자 : {{ article.username }}</p>
    <p>글 분류 : {{ article.category }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <RouterLink :to="{ name: 'DetailView', params: { id: article.id } }"
      ><p>{{ article.title }}</p></RouterLink
    >
    <hr />
    <p>댓글 수 : {{ article.comment_count }}</p>
    <p>좋아요 수 : {{ article.like_count }}</p>
  </div>
</template>

<script setup>
import { RouterLink } from "vue-router";

defineProps({
  article: Object,
});
</script>

<style scoped></style>
