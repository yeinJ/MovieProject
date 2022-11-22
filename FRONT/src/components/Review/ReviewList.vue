<template>
  <tr>
    <td>{{id}}</td>
    <td>{{title}}</td>
    <!-- <td>{{review?.content}}</td> -->
    <td>{{user}}</td>
    <td>{{created_at}}</td>
    <td>{{review_like_users_count}}</td>

    <b-button v-on:click="deleteReview">
      Delete
    </b-button>
    
    <b-button 
        v-if="this.$store.state.token"
        v-on:click="likeReview" 
        v-bind:class="{ 'is-liked' : this.isLiked }"> 
        Like
    </b-button>

    <!-- <b-button v-on:click="$bvModal.show('modal-detail')">Detail</b-button>
    <div class="modal-detail">
      <b-modal id="modal-detail" 
      bodyBgVariant="dark"
      headerBgVariant="dark"
      footerBgVariant="dark"
      >
        <form>
            <label for="title" text-color="black">제목</label>
            <input type="text" :value=review.title class="form-control" id="title" placeholder="Enter Title">
            
            <br>
            <label for="content">내용</label>
            <textarea class="form-control" id="content" rows="3" :value=review.content></textarea>
            <b-button type="submit" block variant="danger" class="btn btn-danger mt-3" id="submit">Modify</b-button>
        </form>
        <template #modal-footer="{ hide }">
          <b-button size="sm" variant="outline-secondary" @click="hide('forget')">
            Close
          </b-button>
        </template>
      </b-modal>
    </div> -->
  <ReviewDetail
  v-bind:review='review'/>
  </tr>

</template>

<script>
import axios from 'axios'
import ReviewDetail from './ReviewDetail.vue'

const API_URL = 'http://127.0.0.1:8000'

export default {
  props: ['id','title','user','created_at','review_like_users_count','review'],
  data() {
    return {
      isLiked: false,
      // isSameUser: false,
    }
  },
  computed: {
  },
  components : {
    ReviewDetail

  },
  created() {
    this.checkLiked()
  },
  // mounted() {
  //   this.SameUser()
  // },
  methods: {
    checkLiked() {
      if (this.$store.state.token) {
        axios({
          method: 'get',
          url: `${API_URL}/mypage/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          }
        })
        .then((res) => {
          for (const like_review of res.data.like_reviews) {
            if (like_review.id == this.review.id) {
              this.isLiked = true
              break
            }
          }
        })
        .catch((err) => {
          console.log(err)
        })
      }
    },
    likeReview() {
      axios({
        method : 'post',
        url : `${API_URL}/api/v1/reviews/${this.review.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          this.isLiked = res.data
          location.reload()
        })
        .catch((err)=> {
          console.log(err)
        })
    },
    
    deleteReview(){
      axios({
        method : 'delete',
        url : `${API_URL}/api/v1/reviews/${this.review.id}/`,
        headers: {
            Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res)=>{
          location.reload()
          console.log(res)
        })
        .catch((err)=>{
          console.log(err)
        })
    
    },
    // SameUser() {
    //   // console.log('thisid')
    //   // console.log(this.id)
    //   for (const userReview of this.userReviews) {
    //     if (userReview.id === this.id) {
    //       this.isSameUser=true
    //       return
    //     }
    //   }
    // }
    
  }
}
</script>

<style>
.is-liked {
    text-decoration: line-through;
  }

tr:hover{
  background-color:gray;
  opacity: 70%;

}
</style>