<template>
  <div id="app">
      <b-navbar toggleable="md" type="dark" variant="danger">
  
          <router-link v-bind:to="{name:'HomeView'}" class="nav-link">
            <img src="@/../public/hypy.png" alt="Hypy">
          </router-link>
   
          <!-- Right aligned nav items -->
          <b-navbar-nav class="ml-auto">
            <div v-if="!this.$store.state.token">

              <li class="nav-item h5 mb-2">
                <router-link v-bind:to="{name:'LoginView'}" class="nav-link">LogIn</router-link>
              </li>
            </div>
            <div v-else>
              <li class="nav-item" type="button" @click="logout">
                <a class="nav-link h5 mb-2">Logout</a>
              </li>
              <li class="nav-item h5 mb-2">  
                <router-link v-bind:to="{name:'MyPageView'}" class="nav-link">MyPage</router-link>
              </li>
            </div>  
          </b-navbar-nav>
      </b-navbar>
      <router-view/>

    
  </div>
</template>

<script>


export default {
  data() {
    return{
    }
    
  },
  computed : {
    // cookie() {
    //   return document.cookie
    // }
  },
  methods : {
    logout() {
      this.$store.dispatch('logOut')
    }
    
  }


}


</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@200&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300&display=swap');
html
body {
  background-color:rgb(8, 8, 14);
  color:white;
  /* font-family: 'Prompt', sans-serif; */
  font-family: 'Noto Sans KR', sans-serif;
}

.nav-link img{
  width : 90px;
  margin-left:10%;
}

.nav-item{
  list-style-type:none;
  float:left;
}

</style>