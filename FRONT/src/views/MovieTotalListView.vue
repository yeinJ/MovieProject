<template>
  <div class="movie-total-list">
    <ul>
      <div v-for="movie in perPageMovies" v-bind:key="movie.id">
        <MovieList
          v-bind:movie='movie'
        />
      </div>  
    </ul>
    <div class="MoreButton" v-on:click="MoreList">
      <b-icon icon="caret-down-fill" variant="danger" class="d-flex justify-content-between align-items-center" font-scale="4" shift-v="8"></b-icon>
    </div>
  </div>

</template>

<script>
import MovieList from '@/components/Movie/MovieList';

export default {
  name:'MovieTotalView',
  data() {
    return {
      index: 21,

    };

  },
  components: {
    MovieList,
  },
  computed: {
      movies() {
        return this.$store.state.movies;
      },
      perPageMovies() {
        const newMovies = this.movies.slice(
          0,
          this.index+21
        );
        return newMovies;
      },
    },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    },
    MoreList() {
      this.index = Math.min(this.index+21,this.movies.length)
    }
  },


}
</script>

<style>
.movie-total-list > ul{
  display:grid;
  grid-template-columns: repeat(7,1fr);


}

.MoreButton{
  position: relative;
  left : 50%;
  top : 10%;
  margin-top : 5%;
  margin-bottom: 5%;
}



</style>