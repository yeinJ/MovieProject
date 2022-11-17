<template>
  <div class="movie-total-list">
    <!-- <h1>{{movies}}</h1> -->
    <MovieList
    v-for='movie in movies'
    v-bind:key='movie.id'
    v-bind:movie='movie'
    />
   
  </div>
</template>

<script>
import MovieList from '@/components/MovieList';

export default {
  name:'MovieTotalView',
  components: {
    MovieList,
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
    }
  }

}
</script>

<style>

</style>