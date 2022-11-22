import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '@/views/HomeView'
import MovieTotalListView from '@/views/MovieTotalListView'
import RecommendListView from '@/views/RecommendListView'
import SignUpView from '@/views/Account/SignUpView'
import LoginView from '@/views/Account/LoginView'
import DetailView from '@/views/DetailView'
import ReviewDetail from '@/components/Review/ReviewDetail'
import MyPageView from '@/views/MyPageView'
import ReviewForm from '@/components/Review/ReviewForm'
import NotFound404 from '@/views/NotFound404'

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
    path: '/movies/:id/reviews/:review_id',
    name: 'ReviewDetailView',
    component: ReviewDetail,
  },
  {
    path: '/mypage',
    name: 'MyPageView',
    component: MyPageView,
  },
  {
    path: '/movies/:id/create',
    name:'ReviewForm',
    component : ReviewForm
  },
  {
    path: '/404-not-found',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '*',
    redirect: { name: 'NotFound404' }
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
