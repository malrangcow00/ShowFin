<template>
  <v-container>
    <v-row justify="center">
      <v-col></v-col>
      <v-col cols="5">
        <v-card class="pa-8" max-width="100%">
          <v-row v-if="!isUpdate">
            <v-col v-if="article">
              <v-row>
                <v-col>
                  <v-row>
                    <v-col>
                      <v-card-title class="headline text-h5 font-weight-bold">{{
                        article?.title
                      }}</v-card-title>
                    </v-col>
                  </v-row>
                  <v-divider></v-divider>
                  <v-row>
                    <v-col>
                      <v-list>
                        <v-list-item>
                          <v-list-item-content>
                            <v-list-item-title>
                              글 번호:
                              {{ article?.id }}
                            </v-list-item-title>
                          </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                          <v-list-item-content>
                            <v-list-item-title
                              >작성자:
                              {{ article?.username }}</v-list-item-title
                            >
                          </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                          <v-list-item-content>
                            <v-list-item-title
                              >카테고리 :
                              {{ article?.category }}</v-list-item-title
                            >
                          </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                          <v-list-item-content>
                            <v-list-item-title
                              >내용: {{ article?.content }}</v-list-item-title
                            >
                          </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                          <v-list-item-content>
                            <v-list-item-title
                              >댓글 수:
                              {{ article?.comment_count }}</v-list-item-title
                            >
                          </v-list-item-content>
                        </v-list-item>
                        <v-list-item>
                          <v-list-item-content>
                            <v-list-item-title
                              >좋아요 수:
                              {{ article?.like_count }}</v-list-item-title
                            >
                          </v-list-item-content>
                        </v-list-item>
                      </v-list>
                    </v-col>
                  </v-row>
                  <v-divider class="my-3"></v-divider>
                  <v-btn
                    class="my-5"
                    :color="
                      article?.liked_by_user
                        ? 'orange-darken-1'
                        : 'light-blue-darken-1'
                    "
                    @click="toggleLike(article)"
                  >
                    {{ article?.liked_by_user ? "좋아요 취소" : "좋아요" }}
                  </v-btn>
                  <v-container>
                    <v-row
                      v-if="store.logInUser === article?.username"
                      justify="space-around"
                    >
                      <v-col cols="6" md="3">
                        <v-btn
                          @click="updateState"
                          outlined
                          color="green-darken-1"
                          class="w-100"
                          >수정</v-btn
                        >
                      </v-col>
                      <v-col cols="6" md="3">
                        <v-btn
                          @click="deleteArticle"
                          outlined
                          color="pink-lighten-1"
                          class="w-100"
                          >삭제</v-btn
                        >
                      </v-col>
                    </v-row>
                  </v-container>
                  <v-divider class="my-3"></v-divider>
                  <CommentCreate :article="article" />
                </v-col>
              </v-row>
            </v-col>
          </v-row>
          <v-row v-else>
            <v-form class="w-100" @submit.prevent="updateArticle">
              <v-col>
                <v-row>
                  <v-text-field
                    v-model="article.title"
                    label="제목"
                  ></v-text-field>
                </v-row>
                <v-row>
                  <v-textarea
                    v-model="article.content"
                    label="내용"
                  ></v-textarea>
                </v-row>
                <v-row>
                  <v-select
                    v-model="article.category"
                    :items="['예금', '적금', '기타']"
                    label="카테고리"
                  ></v-select>
                </v-row>
              </v-col>
              <v-divider class="my-3"></v-divider>

              <v-btn type="submit" color="primary">수정 완료</v-btn>
            </v-form>
          </v-row>
        </v-card>
      </v-col>
      <v-col cols="5">
        <CommentList
          v-if="article && article.comment_set"
          :comments="article.comment_set"
        />
      </v-col>
      <v-col></v-col>
    </v-row>
  </v-container>
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
const isUpdate = ref(false);
const article = ref(null);

// 업데이트 상태 변경
const updateState = function () {
  isUpdate.value = !isUpdate.value;
};

// 게시글 상세 조회
onMounted(() => {
  axios({
    method: "GET",
    url: `${store.API_URL}/api/articles/${route.params.id}/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
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
    url: `${store.API_URL}/api/articles/${route.params.id}/`,
    data: {
      title: article.value.title,
      content: article.value.content,
      category: article.value.category,
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

// 게시글 좋아요 요청
const toggleLike = function (article) {
  console.log(article);
  const articleId = route.params.id;
  axios({
    method: "POST",
    url: `${store.API_URL}/api/articles/${articleId}/like/`,
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then((res) => {
      if (res.data.message === "게시글 좋아요 성공!") {
        alert("이 게시글을 좋아합니다.");
      } else if (res.data.message === "게시글 좋아요 취소!") {
        alert("이 게시글의 좋아요를 취소하였습니다.");
      }
      // 비동기 처리...
      // window.location.reload();
      console.log(res.data.message);
      article.like_count = res.data.like_count;
      article.liked_by_user = res.data.liked;
    })
    .catch((err) => {
      console.error(err);
    });
};
</script>

<style scoped></style>
