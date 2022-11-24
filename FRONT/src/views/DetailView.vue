<template>
  <div class="MovieDetail">
    <div>
      <h1>{{movie?.title}}</h1>
      <br>
      <div class='likemovie' v-if="this.$store.state.token" v-on:click="likeMovie">
        <b-icon
            v-if="!this.isLiked"
            icon="suit-heart"
            font-scale="2.5"> 
        </b-icon>
        <b-icon
            v-else
            icon="suit-heart-fill"
            font-scale="2.5"
            variant="danger"
            > 
        </b-icon>
      </div>
      <img :src="posterPath" :alt="movie?.title">
      <!-- <p>영화 이름 : {{movie?.title}}</p> -->
      <br>
      <br>
      <p>평점 : {{movie?.vote_average}}</p>
      <p>관객수 : {{movie?.popularity}}</p>
      <p>개봉일 : {{movie?.release_date}}</p>
      <p>
        장르 : 
        <span v-for="(genre,index) in movie?.genres" v-bind:key="index">
          {{genre.name}}
        </span>
      </p>
      <p class='overview' v-if="movie?.overview">줄거리 : {{movie?.overview}}</p>
      <hr>
  
    </div>
  
    <div class = 'ReviewSet'>
      <ReviewSet
      v-bind:reviews='sortedReviews'/>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewSet from '@/components/Review/ReviewSet.vue'

const API_URL = 'http://3.39.173.99:8000'

export default {
  name : 'DetailView',
  components: {
    ReviewSet,
  },
  computed : {
    posterPath() {
      return "https://i0.wp.com/image.tmdb.org/t/p/w300"+this.movie?.poster_path
    },
    sortedReviews() {
      let movieReviews = this.movie?.reviews
      if(movieReviews){
        return movieReviews.sort(function(a, b) {
          if (a.review_like_users_count < b.review_like_users_count) {
            return 1;
          }
          if (a.review_like_users_count > b.review_like_users_count) {
            return -1;
          }
          return 0;
        })
      }
      return null;
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
            if (like_movie.id === this.movie?.id) {
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
  margin: auto;
  margin-top : 3%;
  margin-left: 10%;
  margin-right:10%;
  margin-bottom : 10%;
  border-radius: 30px;
  border : 1px solid red;
  padding : 3%;
  text-align: center;
}

.is-liked {
    text-decoration: line-through;
  }

.ReviewSet {
  position: relative;
  margin-left : 10%;
  margin-right : 10%;
  margin-bottom : 10%;
}
.likemovie{
  position: absolute;
  left:80%;

}

.overview{
  padding: 0% 10% 0% 10%;
}

</style>