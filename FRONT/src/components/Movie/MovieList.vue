<template>
  <div>
    <div class="movielist">
      <img v-bind:src="posterPath" v-bind:alt="movie?.title">
      <div class="moviemenu">
        <!-- <b-card-title class='movietitle'>{{movie.title}}</b-card-title> -->
        <b-button v-bind:to ="{ name: 'DetailView', params: { id: movie.id } }" href="#" variant="danger">
          Detail
        </b-button>
      </div>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'

// const API_URL = 'http://3.39.173.99:8000'

export default {
  name:'MovieList',
  props: {
    movie:Object
  },
  data() {
    return {
    }
  },
  created() {
  },
  computed : {
    posterPath() {
      return "https://i0.wp.com/image.tmdb.org/t/p/w300"+this.movie.poster_path
    }
  },
  methods: {

  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@200&display=swap');

  img{
    width: 170px;
    height: 234px;
    border-radius: 10px
  }
  .movietitle{
    font-family: 'Prompt', sans-serif;
    font-size:12px;
    color:white;
  }
  .movielist{
    /* padding-left:7%; */
    /* padding-right: 15%; */
    padding-top :30%;
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
    padding: 0% 0%;
    margin-top : 10%;
    text-align: center;
    position: absolute;
    top: 55%;
    left: 33%;
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