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
        <ReviewList
        v-for='review in reviews'
        v-bind:key='review.id'
        v-bind:review='review'/>
      </tbody>

    </table>
    <b-pagination v-model="currentPage"
      v-on:total-rows="rows"
      v-bind:per-page="perPage"
      aria-controls="my-table"></b-pagination>
    
  </div>
</template>

<script>
import ReviewList from '@/components/Review/ReviewList.vue'
import ReviewForm from '@/components/Review/ReviewForm.vue'



export default {
  data() {
    return {
      currentPage : 1,
      perPage: 2, //페이지 당 보여줄 갯수
    }

  },
  components: {
    ReviewList,
    ReviewForm,
  },
  props: ['reviews', ],
  methods : {
    rows() {
      return this.reviews.length
    }
  },
  // computed : {
  //   rows(){
  //     return this.reviews.length
  //   }
  // }

}
</script>

<style scoped>
.table{
  color:white;
}
</style>