import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAccountStore = defineStore(
  "account",
  () => {
    const logInUser = ref("");
    const API_URL = import.meta.env.VITE_API_URL;
    // const API_URL = "http://127.0.0.1:8000";
    const token = ref(null);

    // 회원가입
    const signUp = function (payload) {
      const {
        username,
        nickname,
        password1,
        password2,
        email,
        age,
        wealth,
        salary,
      } = payload;
      axios({
        method: "POST",
        url: `${API_URL}/accounts/signup/`,
        data: {
          username,
          nickname,
          password1,
          password2,
          email,
          age,
          wealth,
          salary,
        },
      })
        .then((res) => {
          console.log(res);
          // const password = password1;
          // logIn({ username, password });
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
      })
        .then((res) => {
          console.log(res.data);
          token.value = res.data.key;
          logInUser.value = payload.username;
          router.push({ name: "MainView" });
        })
        .catch((err) => {
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
        url: `${API_URL}/accounts/logout/`,
      })
        .then((res) => {
          token.value = null;
          logInUser.value = "";
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 회원정보 조회
    const getAccountInfo = function () {
      axios({
        method: "GET",
        url: `${API_URL}/accounts/user_info/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 회원정보 수정
    const updateAccountInfo = function () {
      axios({
        method: "PUT",
        url: `${API_URL}/accounts/user_detail/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 비밀번호 변경
    const changePassword = function () {
      axios({
        method: "POST",
        url: `${API_URL}/accounts/changepassword/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 회원탈퇴
    const deleteAccount = function () {
      axios({
        method: "DELETE",
        url: `${API_URL}/accounts/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
        })
        .catch((err) => {
          console.log(err);
        });
    };

    return {
      token,
      signUp,
      logIn,
      isLogIn,
      logOut,
      getAccountInfo,
      updateAccountInfo,
      changePassword,
      deleteAccount,
      logInUser,
    };
  },
  { persist: true }
);
