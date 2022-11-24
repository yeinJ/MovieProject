<template>
    <div class="reviewList">
      <ReviewDetail 
      class="review_Detail"
      v-bind:review="review" />
      
      <p>{{ this.review.title }}</p>
      <p>{{ created_date }}</p>
      
      <div v-if="this.$store.state.token">
        <b-icon
            v-if="this.isLiked"
            icon="hand-thumbs-up-fill"
            font-scale="1.5"
            v-on:click="likeReview"
            > 
        </b-icon>
        <b-icon
            v-else
            icon="hand-thumbs-up"
            font-scale="1.5"
            v-on:click="likeReview"
            > 
        </b-icon>
        {{ this.review.review_like_users_count }}
        Like
      </div>
    </div>

</template>

<script>
import axios from "axios";
import ReviewDetail from "./ReviewDetail.vue";

const API_URL = "http://3.39.173.99:8000";

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