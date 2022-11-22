<template>
    <div class="reviewList">
      <p>{{ this.review.review_like_users_count }}</p>
      <p>{{ this.review.title }}</p>
      <!-- <td>{{review?.content}}</td> -->
      <p>{{ created_date }}</p>
      <div
        v-if="this.$store.state.token"
        v-on:click="likeReview"
        v-bind:class="{ 'is-liked': this.isLiked }"
      >
        Like
      </div>
      
      <ReviewDetail 
      class="review_Detail"
      v-bind:review="review" />
      <b-icon class="btn-x h2 mb-2" icon="x" v-on:click="deleteReview"> Delete </b-icon>
    </div>

</template>

<script>
import axios from "axios";
import ReviewDetail from "./ReviewDetail.vue";

const API_URL = "http://127.0.0.1:8000";

export default {
  props: ["review",],
  data() {
    return {
      isLiked: false,
    };
  },
  computed: {
    created_date() {
      return this.review.created_at.substr(0, 10)
    }
  },
  components: {
    ReviewDetail,
  },
  created() {
    this.checkLiked();
  },
  // mounted() {
  //   this.SameUser()
  // },
  methods: {
    checkLiked() {
      if (this.$store.state.token) {
        axios({
          method: "get",
          url: `${API_URL}/mypage/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`,
          },
        })
          .then((res) => {
            for (const like_review of res.data.like_reviews) {
              if (like_review.id == this.review.id) {
                this.isLiked = true;
                break;
              }
            }
          })
          .catch((err) => {
            console.log(err);
          });
      }
    },
    likeReview() {
      axios({
        method: "post",
        url: `${API_URL}/api/v1/reviews/${this.review.id}/like/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          this.isLiked = res.data;
          location.reload();
        })
        .catch((err) => {
          console.log(err);
        });
    },

    deleteReview() {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/reviews/${this.review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`,
        },
      })
        .then((res) => {
          location.reload();
          console.log(res);
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.reviewList{
  padding:1%;
}
.is-liked {
  text-decoration: line-through;
}

/* p:hover {
  background-color: gray;
  opacity: 70%;
} */

.review_Detail{
  display: inline-block;

}

.btn-x {
  background: #000;
  color: #fff;
  border: none;
  transition: all 0.3s linear;
}
.btn-x:hover {
  background: transparent;
  color: #000;
}

</style>