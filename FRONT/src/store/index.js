import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '@/router'
// import createPersistedState from 'vuex-persistedstate'
// import router from '@/router'

Vue.use(Vuex)

const API_URL = 'http://127.0.0.1:8000' 

export default new Vuex.Store({
  // plugins: [
  //   createPersistedState() // 초기화 방지
  // ], 
  state: {
    movies : [],
    token : '',
  },
  getters: {
  },
  mutations: {
    GET_MOVIES(state, movies) {

      state.movies = movies
    },
    SAVE_TOKEN(state,token) {
      state.token = token
      router.push({name:'HomeView'})
    }
  
  },
  actions: {
    getMovies(context) {
      axios({
        method:'get',
        url : `${API_URL}/api/v1/movies`,
      })
        .then((res) => {
          context.commit('GET_MOVIES', res.data)
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
          console.log('데이터받음')
        })
    }

  },
})
