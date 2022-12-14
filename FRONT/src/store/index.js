import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'
import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://3.39.173.99:8000' 

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movies : [],
    token : null,
    moreCnt : 0, // 개수 제한 21개
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    }
  },
  mutations: {
    GET_MOVIES(state, movies) {
      state.movies = movies
    },
    SAVE_TOKEN(state,token) {
      state.token = token
      router.push({ name:'HomeView' })
    },
    LOGOUT(state){
      // console.log(state.token) 토큰있음
      state.token=null
      // console.log(state.token) 토큰없음
      localStorage.removeItem('token')
      // location.reload();
      router.push({ name:'HomeView' })
    }
  },
  actions: {
    getMovies(context) {
      axios({
        method:'get',
        url : `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
          this.moreCnt++;
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method : 'post',
        url:`${API_URL}/accounts/signup/`,
        data: {
          username:payload.username,
          password1:payload.password1,
          password2:payload.password2,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN',res.data.key)
        })
        .catch((err) => {
          console.log(err)
          alert('이미 존재하는 ID입니다.')
        })
    },
    logIn(context, payload) {
      axios({
        method : 'post',
        url : `${API_URL}/accounts/login/`,
        data: {
          username:payload.username,
          password:payload.password,
        }
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .catch((err) => {
          if (err.request.status === 400) {
            alert('다시 입력하세요.')
          }
        })
    },
    logOut({commit}){
      commit('LOGOUT')
    },

  },

})
