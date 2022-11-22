<template>
  <div class="board-list">
    <table class="table">
      <h1>
        Review
      </h1>

      <div >
        <div v-for="review in perReviews" v-bind:key="review.id" style="width:100%">
          <ReviewList
            class="Review_list"
            v-bind:review="review"
          />
        </div>
      </div>

      <br>
      <b-pagination
        v-model="currentPage"
        v-bind:total-rows="rows"
        v-bind:per-page="perPage"
        align="center"
      ></b-pagination>

    </table>
    <div class="writeReiew">
      <ReviewForm />
    </div>

  </div>
</template>

<script>
import ReviewList from "@/components/Review/ReviewList.vue";
import ReviewForm from "@/components/Review/ReviewForm.vue";

export default {
  data() {
    return {
      currentPage: 1,
      perPage: 3, //페이지 당 보여줄 갯수
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
.Review_list{
  border : 1px solid white;
  display:flex;
  justify-content: space-between;
  margin : 3%;
}
.table {
  color: white;
  margin-top:2%;
  border : 1px solid rgb(225, 113, 113);
  opacity: 60%;
  border-radius: 10%;
}

.writeReview{
  position : relative;
}

</style>