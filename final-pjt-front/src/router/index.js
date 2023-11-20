import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
import ArticleView from "@/views/ArticleView.vue";
import SignUpView from "@/views/SignUpView.vue";
import LogInView from "@/views/LogInView.vue";
import ExchangerView from "@/views/ExchangerView.vue";
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
    // {
    //   path: "/articles/:id",
    //   name: "DetailView",
    //   component: DetailView,
    // },
    // {
    //   path: "/articles/create",
    //   name: "CreateView",
    //   component: CreateView,
    // },
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
      path: "/exchange",
      name: "exchanger",
      component: ExchangerView,
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
