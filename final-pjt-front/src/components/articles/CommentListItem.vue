<template>
  <v-container v-if="props.comment">
    <v-row justify="center">
      <v-col class="pa-5" cols="12">
        <v-row v-if="!isUpdate">
          <v-col>
            <v-card>
              <v-card-text>
                <v-row>
                  <v-col>
                    <v-list>
                      <v-list-item>
                        <v-list-item-title>
                          <p>작성자: {{ props.comment.username }}</p>
                        </v-list-item-title>
                      </v-list-item>
                      <v-list-item>
                        <v-list-item-title>
                          <p>내용: {{ props.comment.content }}</p>
                        </v-list-item-title>
                      </v-list-item>
                      <v-list-item>
                        <v-list-item-title>
                          <p>좋아요 수: {{ props.comment.like_count }}</p>
                        </v-list-item-title>
                      </v-list-item>
                      <v-divider></v-divider>
                      <v-list-item>
                        <v-list-item-title>
                          <p>
                            작성일: {{ props.comment.created_at.slice(0, 10) }}
                          </p>
                        </v-list-item-title>
                      </v-list-item>
                    </v-list>
                  </v-col>
                </v-row>
              </v-card-text>
              <v-divider></v-divider>
              <v-container>
                <v-row>
                  <v-col cols="6">
                    <v-row>
                      <v-col align="start">
                        <v-btn
                          color="light-blue-darken-1"
                          @click="toggleLike(props.comment)"
                        >
                          {{
                            props.comment.liked_by_user
                              ? "좋아요 취소"
                              : "좋아요"
                          }}
                        </v-btn>
                      </v-col>
                      <v-col
                        align="center"
                        v-if="store.logInUser === props.comment.username"
                      >
                        <v-btn color="green-darken-1" @click="updateState"
                          >수정</v-btn
                        >
                      </v-col>
                    </v-row>
                  </v-col>
                  <v-col cols="2"></v-col>
                  <v-col align="end" cols="4">
                    <v-btn color="pink-lighten-1" @click="deleteComment"
                      >삭제</v-btn
                    >
                  </v-col>
                </v-row>
              </v-container>
            </v-card>
          </v-col>
        </v-row>
        <v-row v-else>
          <v-form class="w-100" @submit.prevent="updateComment">
            <v-col>
              <v-text-field
                v-model="props.comment.username"
                label="작성자"
                disabled
              ></v-text-field>
              <v-textarea
                v-model="props.comment.content"
                label="내용"
              ></v-textarea>
              <v-btn type="submit" color="primary">수정 완료</v-btn>
            </v-col>
          </v-form>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useAccountStore } from "@/stores/accounts.js";
import axios from "axios";
import { useRouter } from "vue-router";
import { ref } from "vue";

const props = defineProps(["comment"]);

const isUpdate = ref(false);
const store = useAccountStore();
const router = useRouter();
const articleId = props.comment.article;
const commentId = props.comment.id;

const updateState = () => (isUpdate.value = !isUpdate.value);

const updateComment = () => {
  axios({
    method: "PUT",
    url: `${store.API_URL}/api/articles/${articleId}/comments/${commentId}/`,
    data: {
      content: props.comment.content,
    },
    headers: {
      Authorization: `Token ${store.token}`,
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

const deleteComment = () => {
  axios({
    method: "DELETE",
    url: `${store.API_URL}/api/articles/${articleId}/comments/${commentId}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
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

const toggleLike = (comment) => {
  axios({
    method: "POST",
    url: `${store.API_URL}/api/articles/${articleId}/comments/${commentId}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      if (res.data.message === "댓글 좋아요 성공!") {
        alert("이 댓글을 좋아합니다.");
      } else if (res.data.message === "댓글 좋아요 취소!") {
        alert("이 댓글의 좋아요를 취소하였습니다.");
      }
      comment.like_count = res.data.like_count;
      comment.liked_by_user = res.data.liked;
    })
    .catch((err) => {
      console.error(err);
    });
};

// if (props.comment.liked_by === store.logInUser) {
//   axios({
//     method: "PUT",
//     url: `${store.API_URL}/api/articles/${articleId}/comments/${commentId}/`,
//     data: {
//       liked_by: store.logInUser,
//     },
//     headers: {
//       Authorization: `Token ${store.token}`,
//     },
//   })
//     .then((res) => {
//       console.log(res);
//     })
//     .catch((err) => {
//       console.error(err);
//     });
// }
</script>

<style scoped></style>
