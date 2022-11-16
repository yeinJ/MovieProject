<template>
  <div>
    <p>영화제목 : {{movie.title}}</p>
    <p>평점 : {{movie.vote_average}}</p>
    <router-link :to="{ name: 'DetailView', params: { id: article.id } }">
      [DETAIL]
    </router-link>
  </div>
</template>

<script>
export default {
  name:'MovieList',
  props: {
    movie:Object
  }
  
}
</script>

<style>

</style>