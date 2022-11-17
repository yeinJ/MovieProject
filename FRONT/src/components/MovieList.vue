<template>
  <div>
    <div class="movielist">
      <img v-bind:src="posterPath" v-bind:alt="movie?.title">
      <div class="moviemenu">
        <b-card-title class='movietitle'>{{movie.title}}</b-card-title>
        <b-button v-bind:to ="{ name: 'DetailView', params: { id: movie.id } }" href="#" variant="primary">
          Detail
        </b-button>
      </div>
    </div>
    <!-- <p>영화제목 : {{movie.title}}</p>
    <p>평점 : {{movie.vote_average}}</p>
    <router-link :to="{ name: 'DetailView', params: { id: movie.id } }">
      [DETAIL]
    </router-link>-->
  </div>
</template>

<script>
export default {
  name:'MovieList',
  props: {
    movie:Object
  },
  computed : {
    posterPath() {
      return "https://i0.wp.com/image.tmdb.org/t/p/w300"+this.movie.poster_path
    }
  },
  
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
    position: relative;
    top : 30%;
  }
  .overview {
    display: block;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }


</style>