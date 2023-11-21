import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
// Article
import ArticleView from "@/views/articles/ArticleView.vue";
import ArticleDetail from "@/components/articles/ArticleDetail.vue";
// Account
import SignUpView from "@/views/accounts/SignUpView.vue";
import LogInView from "@/views/accounts/LogInView.vue";
import AccountDetailView from "@/views/accounts/AccountDetailView.vue";
import AccountUpdateView from "@/views/accounts/AccountUpdateView.vue";
import AccountChangePasswordView from "@/views/accounts/AccountChangePasswordView.vue";
import AccountDeleteView from "@/views/accounts/AccountDeleteView.vue";
// 부가기능
import SearchBankView from "@/views/SearchBankView.vue";
import ExchangeView from "@/views/ExchangeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "MainView",
      component: MainView,
    },
    {
      path: "/articles",
      name: "ArticleView",
      component: ArticleView,
    },
    {
      path: "/articles/:id",
      name: "ArticleDetail",
      component: ArticleDetail,
    },
    {
      path: "/articles/create",
      name: "ArticleCreate",
      component: ArticleCreate,
    },
    {
      path: "/accounts/signup",
      name: "SignUpView",
      component: SignUpView,
    },
    {
      path: "/accounts/login",
      name: "LogInView",
      component: LogInView,
    },
    {
      path: "/accounts/detail",
      name: "AccountDetailView",
      component: AccountDetailView,
    },
    {
      path: "/accounts/update",
      name: "AccountUpdateView",
      component: AccountUpdateView,
    },
    {
      path: "/accounts/password",
      name: "AccountChangePasswordView",
      component: AccountChangePasswordView,
    },
    {
      path: "/accounts/delete",
      name: "AccountDeleteView",
      component: AccountDeleteView,
    },
    {
      path: "/exchange",
      name: "exchange",
      component: ExchangeView,
    },
    {
      path: "/searchBank",
      name: "searchBank",
      component: SearchBankView,
    },
    {
      path: "/exchange",
      name: "exchange",
      component: ExchangeView,
    },
  ],
});

export default router;
