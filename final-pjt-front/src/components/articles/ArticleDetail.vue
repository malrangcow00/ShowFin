<template>
  <div>
    <h2>상세 정보</h2>
    <div v-if="!isUpdate">
      <div v-if="article">
        <p>글 번호: {{ article?.id }}</p>
        <p>작성자: {{ article?.username }}</p>
        <p>제목: {{ article?.title }}</p>
        <p>{{ article?.category }}</p>
        <p>내용: {{ article?.content }}</p>
        <p>댓글 수 : {{ article.comment_count }}</p>
        <p>좋아요 수 : {{ article.like_count }}</p>
        <button @click="toggleLike(article)">
          {{ article?.liked_by_user ? "좋아요 취소" : "좋아요" }}
        </button>
        <div>
          <button @click="!isUpdate">수정</button>
          <button @click="deleteArticle">삭제</button>
        </div>
        <CommentCreate :articleId="article.id" />
        <CommentList
          v-if="article && article.comment_set"
          :comments="article.comment_set"
        />
      </div>
    </div>
    <div v-else>
      <form @submit.prevent="updateArticle">
        <label for="id">글 번호 : </label>
        <input v-model="article.id" type="text" id="id" disabled /><br />
        <label for="username">작성자 : </label>
        <textarea v-model="article.username" id="username" disabled></textarea
        ><br />
        <label for="title">제목 : </label>
        <input
          v-model="article.title"
          type="text"
          id="title"
          placeholder="제목"
        /><br />
        <label for="content">내용 : </label>
        <textarea
          v-model="article.content"
          id="content"
          placeholder="내용"
        ></textarea
        ><br />
        <label for="category">카테고리:</label>
        <select v-model="article.category" id="category" placeholder="카테고리">
          <option value="예금">예금</option>
          <option value="적금">적금</option>
          <option value="기타">기타</option>
        </select>
        <br />
        <button type="submit">수정 완료</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import axios from "axios";
import { onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { ref } from "vue";
import CommentCreate from "@/components/articles/CommentCreate.vue";
import CommentList from "@/components/articles/CommentList.vue";

const store = useAccountStore();
const route = useRoute();
const router = useRouter();
const article = ref(null);
const isUpdate = ref(false);

// 게시글 상세 조회
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

// 게시글 수정
const updateArticle = function () {
  axios({
    method: "PUT",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
    data: {
      title: article.title,
      content: article.content,
      category: article.category,
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

// 게시글 삭제
const deleteArticle = function () {
  axios({
    method: "DELETE",
    url: `${store.API_URL}/api/v1/articles/${route.params.id}/`,
  })
    .then((res) => {
      console.log(res);
      alert("게시글이 삭제되었습니다.");
      router.push({ name: "ArticleView" });
    })
    .catch((err) => {
      console.log(err);
    });
};

// 게시글 좋아요 요청
const toggleLike = function (article) {
  const articleId = route.params.id;
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
