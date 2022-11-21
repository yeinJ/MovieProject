<template>
  <div>
    <hr />
    <h3>좋아하는 영화</h3>
    <div id="app">
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
  props: ["movies"],
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
};
</script>

<style>
.carousel-wrapper {
  padding: 40px;
  height: 150px;
}
</style>