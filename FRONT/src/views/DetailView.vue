<template>
  <div>
    <h1>Detail</h1>
    <p>영화 이름 : {{movie?.title}}</p>
    <hr>
    <ReviewForm/>

  </div>
</template>

<script>
import axios from 'axios'
import ReviewForm from '@/components/ReviewForm.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name : 'DetailView',
  components: {
    ReviewForm
  },
  data() {
    return {
      movie: null,
    }
  },
  created() {
    this.getMovieDetail()
    
  },
  methods: {
    getMovieDetail() {
      axios({
        method : 'get',
        url : `${API_URL}/api/v1/movies/${this.$route.params.id}`
      })
       .then((res) => {
        this.movie = res.data
       })
       .catch((err) => {
        console.log(err)
       })
    }
  }


}
</script>

<style>

</style>