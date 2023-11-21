<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12">
        <v-card>
          <v-card-title>
            <h3>댓글작성</h3>
          </v-card-title>
          <v-card-text>
            <v-form @submit.prevent="createComment">
              <v-textarea
                v-model="content"
                label="내용"
                outlined
                rows="5"
              ></v-textarea>
              <v-btn type="submit" color="primary">댓글작성</v-btn>
            </v-form>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import axios from "axios";
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";

const props = defineProps(["article"]);

const store = useAccountStore();
const content = ref("");

const createComment = function () {
  if (!content.value) {
    alert("내용을 입력해주세요.");
    return;
  }

  axios({
    method: "POST",
    url: `${store.API_URL}/api/articles/${props.article.id}/comments/`,
    data: {
      content: content.value,
    },
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      console.log(res);
      content.value = "";
      props.article.comment_set.push(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
};
</script>

<style scoped>
/* Add any additional styling if needed */
</style>
