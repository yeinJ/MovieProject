<template>
  <div class="board-list">
    
    <div class="common-buttons">
      <ReviewForm/>
      <!-- <b-button v-bind:to="{name :'ReviewForm'}">후기 작성</b-button> -->
    </div>
      <table id='my-table' class="table ">
      <thead>
      <tr>
        <th>번호</th>
        <th>제목</th>
        <th>작성자</th>
        <th>날짜</th>
        <th>좋아요수</th>
      </tr>   
      </thead>
      <tbody>
        <div v-for='review in perReviews' v-bind:key="review.id">
          <ReviewList
          v-bind:id="review?.id"
          v-bind:title="review?.title"
          v-bind:user="review?.user"
          v-bind:created_at="review?.created_at"
          v-bind:review_like_user_count="review?.review_like_users_count"
          />
        </div>
      </tbody>

      <b-pagination
      v-model="currentPage"
      v-bind:total-rows="rows"
      v-bind:per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>
    </table>
  </div>
</template>

<script>
import ReviewList from '@/components/Review/ReviewList.vue'
import ReviewForm from '@/components/Review/ReviewForm.vue'



export default {
  data() {
    return {
      currentPage : 1,
      perPage: 15, //페이지 당 보여줄 갯수
      items : this.reviews,
    }

  },
  components: {
    ReviewList,
    ReviewForm,
  },
  props: ['reviews', ],
  computed : {
    rows() {
      return this.reviews?.length
  },
  perReviews() {
    const newReviews = this.reviews?.slice(
      this.perPage * this.currentPage - this.perPage,
      this.perPage * this.currentPage
    );
    return newReviews;
  },
  }
}
</script>

<style scoped>
.table{
  color:white;
}
</style>