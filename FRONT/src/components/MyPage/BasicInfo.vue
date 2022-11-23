<template>
  <div>
    <br>
    <h1>{{ username }}의 페이지</h1>
    <br>
    <p class=" h1 mb-2">
      <b-icon class="iconImg"  style="width: 20%; height: 50%;" icon="person-circle"></b-icon>
    </p>
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