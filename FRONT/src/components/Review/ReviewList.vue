<template>
  <span style="width:100%">
    <td>{{ this.review.review_like_users_count }}</td>
    <td>{{ this.review.title }}</td>
    <!-- <td>{{review?.content}}</td> -->
    <td>{{ created_date }}</td>

    <b-button v-on:click="deleteReview"> Delete </b-button>

    <b-button
      v-if="this.$store.state.token"
      v-on:click="likeReview"
      v-bind:class="{ 'is-liked': this.isLiked }"
    >
      Like
    </b-button>

    <ReviewDetail v-bind:review="review" />
  </span>
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

<style>
.is-liked {
  text-decoration: line-through;
}

tr:hover {
  background-color: gray;
  opacity: 70%;
}
</style>