import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import MovieTotalListView from '@/views/MovieTotalListView'
import RecommendListView from '@/views/RecommendListView'
import SignUpView from '@/views/SignUpView'
import LoginView from '@/views/LoginView'
import DetailView from '@/views/DetailView'
import ReviewDetail from '@/components/ReviewDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
  },
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
    path: '/movies/:id',
    name: 'DetailView',
    component: DetailView,
  },
  {
    path: 'movies/:id/reviews',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },



]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
