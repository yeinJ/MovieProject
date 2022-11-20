<template>
  <div>
    <ReviewList
    v-for='review in reviews'
    v-bind:key='review.id'
    v-bind:review='review'/>
  </div>
</template>

<script>
import ReviewList from '@/components/Review/ReviewList.vue'



export default {
  components: {
    ReviewList,
  },
  props: ['reviews', ],

}
</script>

<style>

</style>