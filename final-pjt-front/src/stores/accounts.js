import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAccountStore = defineStore("account", () => {
  const article = ref([]);
  const API_URL = import.meta.env.VITE_API_URL;
  // const API_URL = "http://127.0.0.1:8000";
  const token = ref(null);

  // 회원가입
  const signUp = function (payload) {
    const { username, password1, password2 } = payload;
    axios({
      method: "POST",
      url: `${API_URL}/accounts/signup/`,
      data: {
        username,
        password1,
        password2,
      },
    })
      .then((res) => {
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // 로그인
  const router = useRouter();
  const logIn = function (payload) {
    const { username, password } = payload;
    axios({
      method: "POST",
      url: `${API_URL}/accounts/login/`,
      data: {
        username,
        password,
      },
    }),
      then((res) => {
        console.log(res.data);
        token.value = response.data.API_KEY;
        router.push({ name: "MainView" });
      }).catch((err) => {
        console.log(err);
      });
  };

  // 로그인 상태 확인
  // 로그인 상태를 통해서 전역 네비게이션 가드 처리
  const isLogIn = computed(() => {
    if (token.value === null) {
      return false;
    } else {
      return true;
    }
  });

  // 로그아웃
  const logOut = function () {
    axios({
      method: "POST",
      url: `${API_URL}/accounst/logout/`,
    }).then((res) => {
      token.value = null;
      router.push({ name: "MainView" });
    });
  };

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
    article,
    signUp,
    logIn,
    isLogIn,
    logOut,
    getAritleList,
  };
});
