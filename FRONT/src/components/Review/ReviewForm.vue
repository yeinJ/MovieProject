<template>
  <div>
    <b-button v-on:click="$bvModal.show('modal-scoped')">리뷰 작성</b-button>
    <div class="modal-content">
      <b-modal id="modal-scoped" 
      bodyBgVariant="dark"
      headerBgVariant="dark"
      footerBgVariant="dark"
      >
        <form v-on:submit.prevent="createMovieReview">
            <label for="title" text-color="black">제목</label>
            <input type="text" class="form-control" id="title" v-model.trim="title" placeholder="Enter Title">
            <br>
            <label for="content">내용</label>
            <textarea class="form-control" v-model.trim="content" id="content" rows="3"></textarea>
            <b-button type="submit" block variant="danger" class="btn btn-danger mt-3" id="submit">Submit</b-button>
        </form>
        <template #modal-footer="{ hide }">
          <b-button size="sm" variant="outline-secondary" @click="hide('forget')">
            Close
          </b-button>
        </template>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://3.39.173.99:8000'
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
        this.$swal({
            text: '제목을 입력해주세요.',
            confirmButtonColor: '#d33',
            confirmButtonText: 'OK',
        })
      } else if(!content){
        this.$swal({
            text: '내용을 입력해주세요.',
            confirmButtonColor: '#d33',
            confirmButtonText: 'OK',
        })
      } else {
        axios({
          method : 'post',
          url : `${API_URL}/api/v1/movies/${this.$route.params.id}/reviews/`,
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
            location.reload()
            // this.$router.push({ name: "DetailView" })
          })
          .catch((err)=> {
            if (err.response.status === 400) {
              this.$swal({
                  text: '제목은 최대 100자까지 입력가능합니다.',
                  confirmButtonColor: '#d33',
                  confirmButtonText: 'OK',
              })
            } else {
              console.log(err)
            }
          })        
      }
    },
    goList: function () {
      this.$router.push({ name: "HomeView" });
    },
    cancle() {
      this.$router.push({name: 'DetailView'})
    }
  }


}
</script>

<style scoped>
div{
  position:relative;
  margin: 0;
  padding: 0;
}

textarea.form-control {
  height: calc(1.5em + 15rem + 2px) !important;
}

</style>