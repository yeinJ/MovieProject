<template>
  <div>
    <h1>Detail</h1>
    <img :src="posterPath" :alt="movie?.title">
    <p>영화 이름 : {{movie?.title}}</p>
    <p>평점 : {{movie?.vote_average}}</p>
    <p>관객수 : {{movie?.popularity}}</p>
    <p>개봉일 : {{movie?.release_date}}</p>
    <p>
      장르 : 
      <span v-for="(genre,index) in movie?.genres" v-bind:key="index">
        {{genre.name}}
      </span>
    </p>
    <p>줄거리 : {{movie?.overview}}</p>
    <hr>
    <ReviewForm/>

  </div>
</template>

<script>
import axios from 'axios'
import ReviewForm from '@/components/ReviewForm.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'DetailView',
  components: {
    ReviewForm
  },
  computed : {
    posterPath() {
      return "https://i0.wp.com/image.tmdb.org/t/p/w300"+this.movie?.poster_path
    }
  },
  data() {
    return {
      movie: null,
    }
  },
  created() {
    this.getMovieDetail()
  },
  methods: {
    getMovieDetail() {
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/movies/${this.$route.params.id}`
      })
       .then((res) => {
        this.movie = res.data
       })
       .catch((err) => {
        console.log(err)
       })
    }
  }


}
</script>

<style>

</style>