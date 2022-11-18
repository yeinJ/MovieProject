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


</style>