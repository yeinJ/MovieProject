<template>
  <div>
    <div>
      <b-card
        overlay
        img-src="https://picsum.photos/900/250/?image=3"
        img-alt="Card Image"
        text-variant="white"
        title="여기영화놓고싶음"
        sub-title="Subtitle"
      >
        <b-card-text>
          S이건 나중에 하은이랑 얘기해봐야징~~
        </b-card-text>
      </b-card>
      <!-- <router-link v-bind:to="{name:'MovieTotalView'}">Total</router-link> | -->
      <router-link v-bind:to="{name:'RecommendView'}">Recommend</router-link>
      <hr>
      <h1>전체영화목록</h1>
      <MovieTotalListView/>
    </div>
  </div>
</template>

<script>
import MovieTotalListView from './MovieTotalListView.vue'

export default {
  components: {
    MovieTotalListView
  }

}
</script>

<style>
body{
  background-color: black;
}

</style>