<template>
  <div>
    <div class="wrapper">
      <div class="typing-demo">
        YOU MUST FIND HAPPINESS      
      </div>
    </div>
    <div>
      <router-link v-bind:to="{name:'RecommendView'}">Recommend</router-link>
      <hr>
      <h1>전체영화목록</h1>
      <MovieTotalListView/>
      <button class="btn danger" v-on:click="morepage" >More</button>
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

<style scoped>

.wrapper {
  height: 100vh;
  display: grid;
  place-items: center;
}

.typing-demo {
  width: 24ch;
  animation: typing 2s steps(23), blink .10s step-end infinite alternate;
  white-space: nowrap;
  overflow: hidden;
  border-right: 3px solid;
  font-family: monospace;
  font-size: 5em;
  color:white;
}

@keyframes typing {
  from {
    width: 0
  }
}
    
/* @keyframes blink {
  50% {
    border-color: transparent
  }
} */

</style>