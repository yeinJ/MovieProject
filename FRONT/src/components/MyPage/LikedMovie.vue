<template>
  <div>
    <hr>
    <h3>좋아하는 영화</h3>
    {{ movies }}
    <div id="app">
    <b-container>
      <!-- <a class="carousel-control-prev" href="#carousel" role="button" data-slide="prev">
        <span class="carousel-control-prev-icon"></span>
      </a> -->
      
      <b-row>
        <b-col>
          <carousel :perPage="6">
                <LikedMovieList
                v-for='movie in movies'
                v-bind:key='movie.id'
                v-bind:movie='movie'/>
          </carousel>
        </b-col>
      </b-row>
      
      <!-- <a class="carousel-control-next" href="#carousel" role="button" data-slide="next">
        <span class="carousel-control-next-icon"></span>
      </a> -->
    </b-container>
</div>
</div>



</template>

<script>
import LikedMovieList from '@/components/MyPage/LikedMovieList.vue'
import { Carousel} from 'vue-carousel';

export default {
  props: ['movies'],
  components: { 
    LikedMovieList,
    Carousel,
    // Slide,
  },
  
  data() {
    return {
      slide: 0,
      sliding: null
    }
  },

}
</script>

<style>

</style>