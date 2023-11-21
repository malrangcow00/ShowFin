<template>
  <div>
    <h3>댓글작성</h3>
    <form @submit.prevent="createComment">
      <label for="content">내용 : </label>
      <textarea id="content" cols="20" rows="10" v-model="content"></textarea
      ><br />
      <input type="submit" value="댓글작성" />
    </form>
  </div>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";
import { useRouter } from "vue-router";

defineProps({
  articleId: Number,
});

const store = useAccountStore();
const router = useRouter();
const content = ref("");

const createComment = function () {
  if (!content) {
    alert("내용을 입력해주세요.");
  }
  axios({
    method: "POST",
    url: `${store.API_URL}/api/v1/articles/${articleId.value}/comments/`,
    data: {
      content: content.value,
    },
  })
    .then((res) => {
      console.log(res);
      router.push({ name: "ArticleDetail", params: { id: route.params.id } });
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
