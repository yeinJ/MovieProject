<template>
  <div class="recommend">
    <hr/>
    <div>
      <div class="carousel-wrapper">
        <carousel v-bind="options">
          <LikedMovieList
            v-for="movie in movies"
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
    };
  },
  computed: {
     movies() {
      return this.$store.state.movies
     }
  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
  }
};
</script>

<style scoped>
.recommend{
  margin-bottom: 150px;
}
.carousel-wrapper {
  padding: 40px;
  height: 150px;
}
</style>