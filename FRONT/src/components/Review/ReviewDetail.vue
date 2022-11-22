<template>
  <!-- 버려질 수 있어요 -->
  <div>
    <b-button v-on:click="$bvModal.show(modalId)">Detail</b-button>
    <div v-bind:class = modalId >
      <b-modal
        v-bind:id = modalId
        bodyBgVariant="dark"
        headerBgVariant="dark"
        footerBgVariant="dark"
      >
        <form v-on:submit.prevent="createMovieReview">
          <label for="title" text-color="black">제목</label>
          <input
            type="text"
            :value="review.title"
            class="form-control"
            id="title"
            placeholder="Enter Title"
          />

          <br />
          <label for="content">내용</label>
          <textarea
            class="form-control"
            id="content"
            rows="3"
            :value="review.content"
          ></textarea>
          <b-button
            type="submit"
            block
            variant="danger"
            class="btn btn-danger mt-3"
            id="submit"
            >Modify</b-button
          >
        </form>
        <template #modal-footer="{ hide }">
          <b-button
            size="sm"
            variant="outline-secondary"
            @click="hide('forget')"
          >
            Close
          </b-button>
        </template>
      </b-modal>
    </div>
  </div>
</template>

<script>
// import axios from 'axios'
// // 버려질 수 있음
// const API_URL = 'http://127.0.0.1:8000'

export default {
  data() {
    return {};
  },
  props: ["review"],
  created() {
    // this.getReviewDetail()
  },
  computed: {
    modalId() {
      return `modal-detail-${this.review.id}`
    }
  },
  methods: {
    // getReviewDetail() {
    //   axios({
    //     method : 'get',
    //     url : `${API_URL}/api/v1/reviews/${this.$route.params.review_id}/`,
    //     headers: {
    //         Authorization: `Token ${this.$store.state.token}`
    //     }
    //   })
    //    .then((res) => {
    //     this.review = res.data
    //    })
    //    .catch((err) => {
    //     if (err.response.status === 404) {
    //       this.$router.push('/404-not-found')
    //     }
    //    })
    // },
  },
};
</script>

<style>
</style>