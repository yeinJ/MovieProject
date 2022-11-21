<template>
  <tr>
    <td>{{id}}</td>
    <td>{{title}}</td>
    <!-- <td>{{review?.content}}</td> -->
    <td>{{user}}</td>
    <td>{{created_at}}</td>
    <td>{{review_like_users_count}}</td>
    <b-button 
        v-if="this.$store.state.token"
        v-on:click="likeReview" 
        v-bind:class="{ 'is-liked' : this.isLiked }"> 
        Like
    </b-button>
  </tr>

</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  props: ['id','title','user','created_at','review_like_users_count' ],
  data() {
    return {
      isLiked: false,
    }
  },
  created() {
    this.checkLiked()
  },
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
  },
}
</script>

<style>
.is-liked {
    text-decoration: line-through;
  }
</style>