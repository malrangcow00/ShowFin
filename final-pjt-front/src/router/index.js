import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import SearchBankView from "@/views/SearchBankView.vue";

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
  ]
})

export default router
