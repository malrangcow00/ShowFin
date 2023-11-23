import { createRouter, createWebHistory } from "vue-router";
import MainView from "@/views/MainView.vue";
// Product
import ProductsView from "@/views/products/ProductsView.vue";
import DepositDetail from "@/components/products/DepositDetail.vue";
// import Deposit from "@/components/products/Deposit.vue";
import SavingList from "@/components/products/SavingList.vue";
import SavingDetail from "@/components/products/SavingDetail.vue";
import LoanList from "@/components/products/LoanList.vue";
import LoanDetail from "@/components/products/LoanDetail.vue";
import UserDeposit from "@/components/products/UserDeposit.vue";
import UserSaving from "@/components/products/UserSaving.vue";
import UserLoan from "@/components/products/UserLoan.vue";
import RecommandDeposit from "@/components/products/RecommandDeposit.vue";
import RecommandSaving from "@/components/products/RecommandSaving.vue";
import RecommandLoan from "@/components/products/RecommandLoan.vue";
// Article
import ArticleView from "@/views/articles/ArticleView.vue";
import ArticleDetail from "@/components/articles/ArticleDetail.vue";
import ArticleCreate from "@/components/articles/ArticleCreate.vue";
// import CommentCreate from "@/components/articles/CommentCreate.vue";
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
    // Product
    {
      path: "/products",
      name: "ProductsView",
      component: ProductsView,
    },
    // {
    //   path: "/products/deposits",
    //   name: "Deposit",
    //   component: Deposit,
    // },
    {
      path: "/products/deposits/:fin_prdt_cd",
      name: "DepositDetail",
      component: DepositDetail,
    },
    {
      path: "/products/savings",
      name: "SavingList",
      component: SavingList,
    },
    {
      path: "/products/savings/:id",
      name: "SavingDetail",
      component: SavingDetail,
    },
    {
      path: "/products/loans",
      name: "LoanList",
      component: LoanList,
    },
    {
      path: "/products/loans/:id",
      name: "LoanDetail",
      component: LoanDetail,
    },
    {
      path: "/user/deposit",
      name: "UserDeposit",
      component: UserDeposit,
    },
    {
      path: "/user/saving",
      name: "UserSaving",
      component: UserSaving,
    },
    {
      path: "/user/loan",
      name: "UserLoan",
      component: UserLoan,
    },

    // Article
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
    // {
    //   path: "/articles/comments/create",
    //   name: "CommentCreate",
    //   component: CommentCreate,
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
      path: "/products/deposits/recommend",
      name: "RecommendDeposit",
      component: RecommandDeposit,
    },
    {
      path: "/products/savings/recommend",
      name: "RecommendSaving",
      component: RecommandSaving,
    },
    {
      path: "/products/loans/recommend",
      name: "RecommendLoan",
      component: RecommandLoan,
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
