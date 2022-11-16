import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieTotalListView from '@/views/MovieTotalListView'
import RecommendListView from '@/views/RecommendListView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import DetailView from '@/views/DetailView'

Vue.use(VueRouter)

const routes = [
  {
    path:'/movietotal',
    name:'movietotal',
    component: MovieTotalListView,
  },
  {
    path:'/recommend',
    name:'recommend',
    component: RecommendListView,
  },
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView,
  },
  {
    path: '/login',
    name: 'LoginView',
    component: LoginView,
  },
  {
    path: '/:id',
    name: 'DetailView',
    component: DetailView,
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
