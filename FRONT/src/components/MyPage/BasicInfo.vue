<template>
  <div>
    <br>
    <h1>{{ username }}의 페이지</h1>
    <br>
    <b-img
    src = 'https://t1.daumcdn.net/cfile/tistory/27738433597DCB1312' 
    v-bind="mainProps" rounded="circle" alt="Circle image"></b-img>
  </div>
</template>

<script>
export default {
  props: ['username'],
  data() {
    return {
      mainProps: { blank: false, blankColor: '#777', width: 300, height: 300, class: 'm1' }
    }
  }
}
</script>

<style scoped>
div {
    text-align: center;
    margin-top : 5%;
}

</style>