<template>
  <div class="recommend">
    <hr/>
    <div>
      <h3 class='info' v-if="this.info">{{ this.info }}</h3>
      <div v-else class="carousel-wrapper">
        <carousel v-bind="options">
          <LikedMovieList
            v-for="movie in this.movies"
            v-bind:key="movie.id"
            v-bind:movie="movie"
          />
          <slide v-for="i in movies" :key="i.id+10000">
          </slide>
        </carousel>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

import LikedMovieList from "@/components/MyPage/LikedMovieList.vue";
import { Carousel, Slide } from "vue-carousel";

export default {
  components: {
    LikedMovieList,
    Carousel,
    Slide,
  },
  data() {
    return {
      options: {
        loop: true,
        perPage: 7,
      },
      movies: [],
      info: null,
    };
  },
  created() {
    this.getRecommendMovies()
  },
  methods: {
    getRecommendMovies() {
      axios({
          method: 'get',
          url: `${API_URL}/api/v1/movies/recommended/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          console.log(res.data)
          if (res.data) {
            this.movies = res.data
          } else {
            this.info = '영화를 찜하시면, 취향에 맞는 영화를 추천해드리겠습니다.'
          }
        })
        .catch((err) => {
          console.log(err)
        })
    }
  }
};
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
h3{
  font-family: 'Black Han Sans', sans-serif;
  position : absolute;
  left:4%;
  
  padding-top: 3%;

}
.recommend{
  margin-bottom: 200px;
  
}
.carousel-wrapper {
  padding: 50px;
  height: 150px;
}


.info {
  display:flex;
  justify-content:center;
  align-items:center;
}

</style>