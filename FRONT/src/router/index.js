import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import MovieTotalListView from '@/views/MovieTotalListView'
import RecommendListView from '@/views/RecommendListView'
import SignUpView from '@/views/Account/SignUpView'
import LoginView from '@/views/Account/LoginView'
import DetailView from '@/views/DetailView'
import ReviewDetail from '@/components/Review/ReviewDetail'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'HomeView',
    component: HomeView,
  },
  {
    path:'/movietotal',
    name:'MovieTotalView',
    component: MovieTotalListView,
  },
  {
    path:'/recommend',
    name:'RecommendView',
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
    name: 'ReviewDetailView',
    component: ReviewDetail,
  },




]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
