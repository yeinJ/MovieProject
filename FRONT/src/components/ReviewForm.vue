<template>
  <div>
    <h1>게시글 작성</h1>
    <form v-on:submit.prevent="createMovieReview">
      <label for="title">제목 : </label>
      <input type="text" id="title" v-model.trim="title"><br>
      <label for="content">내용 : </label>
      <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      <input type="submit" id="submit">
    </form>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'
export default {
  data() {
    return {
      title: null,
      content: null,
      movie:null,
    }
  },
  methods : {
    createMovieReview(){
      const title = this.title
      const content = this.content
      const movie = this.$route.params.id
      if(!title){
        alert('제목을 입력해주세요')
      }else if(!content){
        alert('내용을 입력해주세요')
        return
      }
      axios({
        method : 'post',
        url : `${API_URL}/api/v1/movies/${this.$route.params.id}/reviews`,
        data: {
          title:title,
          content:content,
          movie : movie,
        },
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          console.log(res)
        })
        .catch((err)=> {
          console.log(err)
          console.log(this.user)
        })
    
    }

  }
  


}
</script>

<style>

</style>