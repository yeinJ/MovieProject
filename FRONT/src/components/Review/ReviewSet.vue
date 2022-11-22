<template>
  <div class="board-list">
<<<<<<< HEAD
    <div class="common-buttons">
      
      <!-- <b-button v-bind:to="{name :'ReviewForm'}">후기 작성</b-button> -->
    </div>
    <table id="my-table" class="table">
=======
    <table id="my-table" class="table" style="width:100%">
>>>>>>> 96e9da2f1192e2db2d31a1962d7ee2e6b2daf384
      <thead>
        <th>Review</th>
        <th><ReviewForm /></th> 
      </thead>
      <tbody>
        <tr v-for="review in perReviews" v-bind:key="review.id" style="width:100%">
          <ReviewList
            v-bind:review="review"
          />
        </tr>
      </tbody>

      <b-pagination
        v-model="currentPage"
        v-bind:total-rows="rows"
        v-bind:per-page="perPage"
        aria-controls="my-table"
        align="center"
      ></b-pagination>
    </table>

  </div>
</template>

<script>
import ReviewList from "@/components/Review/ReviewList.vue";
import ReviewForm from "@/components/Review/ReviewForm.vue";

export default {
  data() {
    return {
      currentPage: 1,
      perPage: 15, //페이지 당 보여줄 갯수
      items: this.reviews,
    };
  },
  components: {
    ReviewList,
    ReviewForm,
  },
  props: ["reviews"],
  computed: {
    rows() {
      return this.reviews?.length;
    },
    perReviews() {
      const newReviews = this.reviews?.slice(
        this.perPage * this.currentPage - this.perPage,
        this.perPage * this.currentPage
      );
      return newReviews;
    },
  },
};
</script>

<style scoped>
.table {
  color: white;
  margin-top:2%;
}

</style>