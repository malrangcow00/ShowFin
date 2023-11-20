import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useArticleStore = defineStore("article", () => {
  const article = ref([]);
  // DRF 에 ArticleList 조회 요청
  // login을 하면 전체 게시글을 조회할 수 있다.
  const getAritleList = function () {
    axios({
      method: "GET",
      url: `${API_URL}/api/articles/`,
      header: { Authorization: `Token ${token.value}` },
    })
      .then((res) => {
        console.log(res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return {
    getAritleList,
  };
});
