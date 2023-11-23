import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";
import { useRouter } from "vue-router";

export const useAccountStore = defineStore(
  "account",
  () => {
    // 스토어 인스턴스 - - - - - - - - - - - - - - - - - - - - - - - - - - -
    const API_URL = import.meta.env.VITE_API_URL;

    const bankList = ref([]);
    const deposits = ref([]);
    const savings = ref([]);
    const loans = ref([]);
    const selectedBank = ref("전체");

    const userInfo = ref(null);
    const token = ref(null);

    const articles = ref([]);
    const article = ref(null);

    // - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    // axios - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    // 예금 목록 조회
    const getDeposits = function () {
      axios({
        method: "GET",
        url: `${API_URL}/api/products/deposits/`,
      })
        .then((res) => {
          // console.log(res.data);
          deposits.value = res.data;
        })
        .then(() => {
          getBankList();
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 회원가입시 사용할 은행 목록
    const getBankList = function () {
      const temp = new Set();
      deposits.value.forEach((product) => temp.add(product.kor_co_nm));
      bankList.value = Array.from(temp).sort();
    };

    // 적금 상품 조회
    const getSavings = function () {
      axios({
        method: "GET",
        url: `${API_URL}/api/products/savings/`,
      })
        .then((res) => {
          // console.log(res)
          savings.value = res.data;
        })
        .then(() => {
          getBankList();
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 전세 대출 상품 조회
    const getLoans = function () {
      axios({
        method: "GET",
        url: `${API_URL}/api/products/loans/`,
      })
        .then((res) => {
          // console.log(res)
          loans.value = res.data;
        })
        .then(() => {
          getBankList();
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 회원가입
    const signUp = function (payload) {
      const {
        username,
        nickname,
        password1,
        password2,
        email,
        mainbank,
        location,
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
          mainbank,
          location,
          age,
          wealth,
          salary,
        },
      })
        .then((res) => {
          console.log(res);
          const password = password1;
          alert("회원가입이 완료되었습니다.");
          logIn({ username, password });
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
          alert("로그인 되었습니다.");
          getAccountInfo();
          router.push({ name: "MainView" });
        })
        .catch(() => {
          alert("아이디 또는 비밀번호가 일치하지 않습니다.");
          router.push({ name: "LogInView" });
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
          logInUser.value = null;
          userInfo.value = null;
          alert("로그아웃 되었습니다.");
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
        url: `${API_URL}/api/products/userinfo/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
          userInfo.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 회원정보 페이지
    const AccountInfo = function () {
      axios({
        method: "GET",
        url: `${API_URL}/api/products/userinfo/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
          userInfo.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 회원정보 페이지
    const AccountInfo = function () {
      axios({
        method: "GET",
        url: `${API_URL}/accounts/user_detail/`,
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
          userInfo.value = res.data;
          router.push({ name: "AccountDetailView" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 회원정보 수정
    const updateAccountInfo = function (payload) {
      const { nickname, email, mainbank, location, age, wealth, salary } =
        payload;
      axios({
        method: "PUT",
        url: `${API_URL}/accounts/user_detail/`,
        data: {
          nickname,
          email,
          mainbank,
          location,
          age,
          wealth,
          salary,
        },
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
          userInfo.value = res.data;
          alert("회원정보가 수정되었습니다.");
          getAccountInfo();
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 비밀번호 변경
    const changePassword = function (payload) {
      const { old_password, new_password } = payload;
      axios({
        method: "POST",
        url: `${API_URL}/accounts/change_password/`,
        data: {
          old_password,
          new_password,
        },
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
          alert(res.data.message);
          logOut();
        })
        .catch((err) => {
          alert(err.data.message);
        });
    };

    // 회원탈퇴store.exchange_data.USD.deal_bas_r
    const deleteAccount = function (payload) {
      const { password } = payload;
      axios({
        method: "POST",
        url: `${API_URL}/accounts/user_delete/`,
        data: {
          password,
        },
        headers: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
          token.value = null;
          router.push({ name: "MainView" });
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 전체 게시글 조회
    const getArticleList = function (token) {
      axios({
        method: "GET",
        url: `${API_URL}/api/articles/`,
        header: { Authorization: `Token ${token.value}` },
      })
        .then((res) => {
          console.log(res.data);
          articles.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 게시글 생성
    const createArticles = function () {
      axios({
        method: "POST",
        url: `${API_URL}/api/articles/`,
      })
        .then((res) => {
          // console.log(res.data)
          article.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 상품 가입
    const subscribe = function (prdt_type, product_id) {
      axios({
        method: "POST",
        url: `${API_URL}/api/products/subscribe/${prdt_type}/${product_id}/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log(res);
          getAccountInfo();
        })
        .catch((err) => {
          console.log(err);
        });
    };

    // 주거래 은행과 같은 은행의 상품 추천
    const filterDeposits = ref(null);
    const filterBank = function (selectedBank) {
      filterDeposits.value = ref(null);
      filterDeposits.value = deposits.value.find(
        (deposit) => deposit.kor_co_nm == selectedBank
      );
    };

    // 예금 상품 높은 금리순으로 정렬
    const sortDepositsBy = ref(null);
    const sortDeposits = function (save_trm) {
      deposits.value = deposits.value.sort((a, b) => {
        const intrRateA =
          a.depositoptions_set.find((option) => option.save_trm == save_trm)
            ?.intr_rate || null;
        const intrRateB =
          b.depositoptions_set.find((option) => option.save_trm == save_trm)
            ?.intr_rate || null;
        return intrRateB - intrRateA;
      });
      sortDepositsBy.value = save_trm;
    };

    // 적금 상품 높은 금리순으로 정렬
    const sortSavingsBy = ref(null);
    const sortSavings = function (save_trm) {
      savings.value = savings.value.sort((a, b) => {
        const intrRateA =
          a.savingoptions_set.find((option) => option.save_trm == save_trm)
            ?.intr_rate || null;
        const intrRateB =
          b.savingoptions_set.find((option) => option.save_trm == save_trm)
            ?.intr_rate || null;
        return intrRateB - intrRateA;
      });
      sortSavingsBy.value = save_trm;
    };

    // 대출 상품 정렬
    const sortLoansBy = ref(null);

    const sortLoans = function () {};

    // - - - - - - - - - -
    return {
      API_URL,
      getDeposits,
      getSavings,
      getLoans,
      bankList,
      deposits,
      savings,
      loans,
      token,
      signUp,
      logIn,
      isLogIn,
      logOut,
      getAccountInfo,
      AccountInfo,
      updateAccountInfo,
      changePassword,
      deleteAccount,
      userInfo,
      getArticleList,
      articles,
      createArticles,
      article,
      subscribe,
      selectedBank,
      filterDeposits,
      filterBank,
      sortDepositsBy,
      sortDeposits,
      sortSavingsBy,
      sortSavings,
      sortLoansBy,
      sortLoans,
    };
  },
  { persist: true }
);
