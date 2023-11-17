import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import SearchBankView from "@/views/SearchBankView.vue";
import ExchangerView from "@/views/ExchangerView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/searchBank',
      name: 'searchBank',
      component: SearchBankView
    },
    {
      path: '/exchanger',
      name: 'exchanger',
      component: ExchangerView
    },
  ]
})

export default router
