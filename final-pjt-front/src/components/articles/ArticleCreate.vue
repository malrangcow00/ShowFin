<template>
    <v-container>
        <i
            @click="router.go(-1)"
            class="fa-solid fa-arrow-right-to-bracket fa-rotate-180 h3 me-4 d-flex justify-content-end"
            style="cursor: pointer"
        ></i>
        <v-col></v-col>
        <v-row justify="center">
            <v-col cols="12" md="8">
                <v-card class="pa-3">
                    <v-card-title class="article-create-header">게시글 작성</v-card-title>
                    <v-divider class="my-3"></v-divider>
                    <v-form @submit.prevent="createArticle" class="pa-3">
                        <v-card-text>
                            <v-text-field
                                v-model.trim="title"
                                label="제목"
                                required
                            ></v-text-field>

                            <v-textarea
                                v-model.trim="content"
                                label="내용"
                                required
                            ></v-textarea>

                            <v-select
                                v-model.trim="category"
                                label="카테고리"
                                :items="['예금', '적금', '기타']"
                                required
                            ></v-select>
                        </v-card-text>

                        <v-divider class="my-3"></v-divider>

                        <v-card-actions>
                            <v-spacer></v-spacer>
                            <v-btn type="submit" color="primary">게시글 작성</v-btn>
                        </v-card-actions>
                    </v-form>
                </v-card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script setup>
import axios from "axios";
import { useAccountStore } from "@/stores/accounts.js";
import { ref } from "vue";
import { useRouter } from "vue-router";

const store = useAccountStore();
const router = useRouter();

const title = ref("");
const content = ref("");
const category = ref("");

const createArticle = async () => {
    if (!title.value) {
        alert("제목을 입력해주세요");
        return;
    } else if (!content.value) {
        alert("내용을 입력해주세요");
        return;
    } else if (!category.value) {
        alert("카테고리를 선택해주세요");
        return;
    }

    try {
        const response = await axios.post(
            `${store.API_URL}/api/articles/`,
            {
                title: title.value,
                content: content.value,
                category: category.value,
            },
            {
                headers: {
                    Authorization: `Token ${store.token}`,
                },
            }
        );

        console.log(response.data);
        router.push({ name: "ArticleView" });
    } catch (error) {
        console.error(error);
    }
};
</script>

<style scoped>
.article-create-header {
    font-family: "Noto Sans KR", sans-serif;
    font-size: 25px;
    font-weight: bold;
}
</style>