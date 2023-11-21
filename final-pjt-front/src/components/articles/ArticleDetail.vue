<template>
  <div v-if="article">
    <h2>상세 정보</h2>
    <div>
      <p>글 번호: {{ article?.id }}</p>
      <p>작성자: {{ article?.user }}</p>
      <p>제목: {{ article?.title }}</p>
      <p>{{ article?.category }}</p>
      <p>내용: {{ article?.content }}</p>
      <p>댓글 수 : {{ article.comment_count }}</p>
      <p>좋아요 수 : {{ article.like_count }}</p>
      <button @click="toggleLike(article)">
        {{ article?.liked_by_user ? "좋아요 취소" : "좋아요" }}
      </button>
      <div>
        <button @click="updateArticle">수정</button>
        <button @click="deleteArticle">삭제</button>
      </div>
      <CommentCreate />
      <CommentList v-if="article && article.comment_set" />
    </div>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/articles.js";
import axios from "axios";
import { onMounted } from "vue";
import { useRoute } from "vue-router";
import { ref } from "vue";
import CommentCreate from "@/components/articles/CommentCreate.vue";
import CommentList from "@/components/articles/CommentList.vue";

const store = useArticleStore();
const route = useRoute();
const article = ref({});

onMounted(() => {
  axios({
    method: "get",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res);
      article.value = res.data;
    })
    .catch((err) => {
      console.log(err);
    });
});

defineProps({
  comment: Object,
});

const accountStore = useAccountStore();
const articleStore = useArticleStore();

const toggleLike = function (comment) {
  const articleId = comment.article;

  axios({
    method: "POST",
    url: `${accountStore.API_URL}/api/articles/${articleId}/like/`,
    headers: {
      Authorization: `Token ${accountStore.token}`,
    },
  })
    .then((res) => {
      if (res.data.message === "게시글 좋아요 성공!") {
        article.liked_by_user = true; // 좋아요 상태로 업데이트
        alert("이 댓글을 좋아합니다.");
      } else if (res.data.message === "게시글 좋아요 취소!") {
        article.liked_by_user = false; // 좋아요 취소 상태로 업데이트
        alert("이 댓글의 좋아요를 취소하였습니다.");
      }
      // 비동기 처리...
      // window.location.reload();
      console.log(res.data.message);
      article.like_count = res.data.like_count;
    })
    .catch((err) => {
      console.error(err);
    });
};
</script>

<style scoped></style>
