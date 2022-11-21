<template>
  <div>
    <div class="MovieDetail">
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
      <p>좋아요 수 : {{movie?.movie_like_users_count}}</p>
      <b-button 
          v-if="this.$store.state.token"
          v-on:click="likeMovie" 
          v-bind:class="{ 'is-liked' : this.isLiked }"> 
          Like
      </b-button>
    </div>
  
    <div class = 'ReviewSet'>
      <ReviewSet
      v-bind:reviews='movie?.reviews'/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewSet from '@/components/Review/ReviewSet.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'DetailView',
  components: {
    ReviewSet,
  },
  computed : {
    posterPath() {
      return "https://i0.wp.com/image.tmdb.org/t/p/w300"+this.movie?.poster_path
    }
  },
  data() {
    return {
      movie: null,
      // posterPath: null,
      isLiked: false,
    }
  },
  created() {
    this.getMovieDetail()
    this.checkLiked()
  },
  methods: {
    getMovieDetail() {
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/movies/${this.$route.params.id}/`
      })
       .then((res) => {
        this.movie = res.data
       })
       .catch((err) => {
        if (err.response.status === 404) {
          this.$router.push('/404-not-found')
        }
       })
    },
    checkLiked() {
      if (this.$store.state.token) {
        axios({
          method: 'get',
          url: `${API_URL}/mypage/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          for (const like_movie of res.data.like_movies) {
            if (like_movie.id == this.movie.id) {
              this.isLiked = true
              break
            }
          }
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    likeMovie() {
      axios({
        method : 'post',
        url : `${API_URL}/api/v1/movies/${this.movie.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.isLiked = res.data
          location.reload()
        })
        .catch((err)=> {
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>
.MovieDetail{
  position: relative;
  float: left;
  margin-left: 10%;
  width:30%;
  /* transform: translate(-50%,-50%); */
}
/* .ReviewWrite{
  position:relative;
  float: right;
  margin-top:10%;
  width:30%;
  margin-left : 50%;
  box-sizing: border-box;

} */

.is-liked {
    text-decoration: line-through;
  }

.ReviewSet {
  position: absolute;
  float: right;
  margin-left: 50%;
}

</style>