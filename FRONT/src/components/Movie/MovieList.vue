<template>
  <div>
    <div class="movielist">
      <img v-bind:src="posterPath" v-bind:alt="movie?.title">
      <div class="moviemenu">
        <b-card-title class='movietitle'>{{movie.title}}</b-card-title>
        <b-button v-bind:to ="{ name: 'DetailView', params: { id: movie.id } }" href="#" variant="primary">
          Detail
        </b-button>

        <div v-if="this.$store.state.token" v-on:click="likeMovie">
        <b-icon
            v-if="!this.isLiked"
            icon="heart"
            font-scale="2.5"> 
        </b-icon>
        <b-icon
            v-else
            icon="heart-fill"
            font-scale="2.5"> 
        </b-icon>
      </div>


      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name:'MovieList',
  props: {
    movie:Object
  },
  data() {
    return {
      isLiked: false,
    }
  },
  created() {
    this.checkLiked()
  },
  computed : {
    posterPath() {
      return "https://i0.wp.com/image.tmdb.org/t/p/w300"+this.movie.poster_path
    }
  },
  methods: {
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
          for (const movie of res.data.like_movies) {
            if (movie.id == this.movie.id) {
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
        })
        .catch((err)=> {
          console.log(err)
        })
    },
  }
}
</script>

<style scoped>
  img{
    width: 170px;
    height: 234px;
    border-radius: 10px
  }
  .movietitle{
    font-family: Georgia, "Malgun Gothic", serif;
    font-size:12px;
    color:white;
  }
  .movielist{
    padding:10px;
    position:relative;
  }
  .moviemenu{
    display:none;
  }
  .movielist:hover img{
    opacity:0.5;
  }
  .movielist:hover .moviemenu{
    display:block;
    padding: 5px 10px;
    text-align: center;
    position: absolute;
    top: 50%;
    left: 40%;
    transform: translate( -50%, -50% );
  }
  .overview {
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .is-liked {
    text-decoration: line-through;
  }

</style>