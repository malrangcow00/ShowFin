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
import axios from "axios";
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";

// import { useRouter } from "vue-router";

const props = defineProps({
  articleId: Number,
});

const emit = defineEmits(["createComment"]);

const store = useAccountStore();
// const router = useRouter();
const content = ref("");

const createComment = function () {
  if (!content) {
    alert("내용을 입력해주세요.");
  }
  axios({
    method: "POST",
    url: `${store.API_URL}/api/articles/${props.articleId}/comments/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      emit("createComment");
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped></style>
