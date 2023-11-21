<template>
  <div v-if="!isUpdate">
    <h5>댓글</h5>
    <div v-if="comment">
      <div>
        <p>작성자: {{ comment.username }}</p>
        <p>내용: {{ comment.content }}</p>
        <p>좋아요 수: {{ comment.like_count }}</p>
      </div>
      <button @click="toggleLike(comment)">
        {{ comment.liked_by_user ? "좋아요 취소" : "좋아요" }}
      </button>
      <button @click="!isUpdate">수정</button>
      <button @click="deleteComment">삭제</button>
    </div>
    <div v-else>
      <form @submit.prevent="updateComment">
        <label for="username">작성자 : </label>
        <input
          v-model="comment.username"
          type="text"
          id="username"
          disabled
        /><br />
        <label for="content">내용 : </label>
        <textarea v-model="comment.content" id="content"></textarea><br />
      </form>
    </div>
  </div>
</template>

<script setup>
import { useArticleStore } from "@/stores/articles.js";
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";
import axios from "axios";

defineProps({
  comment: Object,
});

const isUpdate = ref(false);
const articleId = comment.article;
const commentId = comment.id;

// 댓글 수정
const updateComment = function () {
  axios({
    method: "PUT",
    url: `${store.API_URL}/api/v1/articles/${articleId}/comments/${commentId}/`,
    data: {
      content: comment.content,
    },
  })
    .then((res) => {
      console.log(res);
      isUpdate.value = false;
    })
    .catch((err) => {
      console.log(err);
    });
};

// 댓글 삭제
const deleteComment = function () {
  axios({
    method: "DELETE",
    url: `${store.API_URL}/api/v1/articles/${articleId}/comments/${commentId}/`,
  })
    .then((res) => {
      console.log(res);
      alert("댓글이 삭제되었습니다.");
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.log(err);
    });
};

const accountStore = useAccountStore();
const articleStore = useArticleStore();

const toggleLike = function (comment) {
  axios({
    method: "POST",
    url: `${accountStore.API_URL}/api/articles/${articleId}/comments/${commentId}/like/`,
    headers: {
      Authorization: `Token ${accountStore.token}`,
    },
  })
    .then((res) => {
      if (res.data.message === "댓글 좋아요 성공!") {
        comment.liked_by_user = true; // 좋아요 상태로 업데이트
        alert("이 댓글을 좋아합니다.");
      } else if (res.data.message === "댓글 좋아요 취소!") {
        comment.liked_by_user = false; // 좋아요 취소 상태로 업데이트
        alert("이 댓글의 좋아요를 취소하였습니다.");
      }
      // 비동기 처리...
      // window.location.reload();
      console.log(res.data.message);
      comment.like_count = res.data.like_count;
    })
    .catch((err) => {
      console.error(err);
    });
};
</script>

<style scoped></style>
