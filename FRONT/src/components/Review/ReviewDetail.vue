<template>
  <div>
      <button class="custom-btn btn-7" v-on:click="$bvModal.show(modalId)">Detail</button>
      <div v-bind:class = modalId >
      <b-modal
        v-bind:id = modalId
        bodyBgVariant="dark"
        headerBgVariant="dark"
        footerBgVariant="dark"
        v-on:hide="resetModalData"
        v-on:show="myPage"
      >       
        <form v-on:submit.prevent="createMovieReview">
          <label for="title" text-color="black">제목</label>
          <input
            type="text"
            v-bind:readonly="!isSameUser"
            class="form-control"
            id="title"
            placeholder="Enter Title"
            v-model="title"
          />

          <br />
          <label for="content">내용</label>
          <textarea
            v-bind:readonly="!isSameUser"
            class="form-control"
            id="content"
            rows="3"
            v-model="content"
          ></textarea>
          
          <b-button
            block
            v-if="isSameUser"
            variant="danger"
            class="btn btn-danger mt-3"
            id="submit"
            v-on:click="modifyReview"
            >Modify</b-button
          >
        
          <b-button
            type="submit"
            block
            v-if="isSameUser"
            variant="danger"
            class="btn btn-danger mt-3"
            v-on:click="deleteReview"
            >Delete</b-button
          >
        
        </form>
        <template #modal-footer="{ hide }">
          <b-button
            size="sm"
            variant="outline-secondary"
            v-on:click="hide('forget')"
          >
            Close
          </b-button>
        </template>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'

export default {
  data() {
    return {
      title: '',
      content: '',
      userReviews: [], 
    };
  },
  props: ["review"],
  computed: {
    modalId() {
      return `modal-detail-${this.review.id}`
    },
    isSameUser() {
      for (const userReview of this.userReviews) {
        if (userReview.id === this.review.id) {
          return true
        }
      }
      return false
    }
  },
  created() {
    this.title = this.review.title
    this.content = this.review.content
  },
  methods: {
    modifyReview() {
      axios({
        method: 'put',
        data: {
          'title': this.title,
          'content': this.content,
        },
        url: `${API_URL}/api/v1/reviews/${this.review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
        .then((res) => {
          if (res.status === 200) {
            location.reload()
          }
        })
        .catch((err) => console.log(err))
    },
    deleteReview() {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/reviews/${this.review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.token}`
        }
      })
      .then((res) => {
        if (res.status === 204) {
          location.reload()
        }
      })
      .catch((err) => {console.log(err)})
    },
    resetModalData() {
      this.title = this.review.title;
      this.content = this.review.content;
    },
    myPage() {
      if (this.$store.state.token) {
        axios({
          method: 'get',
          url: `${API_URL}/mypage/`,
          headers: {
            Authorization: `Token ${this.$store.state.token}`
          },
        })
          .then((res) => {this.userReviews = res.data.reviews})
          .catch((err) => console.log(err))
      }
    }
  },
};
</script>

<style scoped>

.btn-7 {
  background: #000;
  color: #fff;
  border: none;
  transition: all 0.3s linear;
}
.btn-7:hover {
  background: transparent;
  color: #000;
}

.btn-7:hover:before,
.btn-7:hover:after {
  background-color: #000;
}
</style>