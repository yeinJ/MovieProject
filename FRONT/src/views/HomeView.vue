<template>
  <div>
    <div class="wrapper">
      <div class="typing-demo">
        YOU MUST FIND HAPPINESS      
      </div>
  
    </div>
    
    <div v-if="this.$store.state.token">
      <h1>추천영화목록</h1>
      <RecommendListView/>
      <br>
    </div>
      <hr>
      <h1>전체영화목록</h1>
      <MovieTotalListView/>
      <button class="btn danger" v-on:click="morepage" >More</button>
  </div>


</template>

<script>
import MovieTotalListView from './MovieTotalListView.vue'
import RecommendListView from './RecommendListView.vue';

export default {
  components: {
    MovieTotalListView,
    RecommendListView,
  },
  methods : {
    morepage() {
      console.log('이거버튼')
    }
  }

}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Rubik+Microbe&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');

h1{
  margin-left:3%;
  font-family: 'Black Han Sans', sans-serif;

}
.backgroundimg{
  opacity:50%;

}

.wrapper {
  height: 50vh;
  display: grid;
  place-items: center;
}


.typing-demo {
  width: 20ch;
  animation: typing 2s steps(21), blink .10s step-end infinite alternate;
  white-space: nowrap;
  overflow: hidden;
  border-right: 3px solid;
  font-family: monospace;
  font-size: 5em;
  color:white;
  font-family: 'Dancing Script', cursive;
  /* font-family: 'Prompt', sans-serif; */
  
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