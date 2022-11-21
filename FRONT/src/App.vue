<template>
  <div id="app">
      <nav class="navbar navbar-expand-sm navbar-light bg-danger">
        <div class="container-fluid">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link v-bind:to="{name:'HomeView'}" class="nav-link">Home</router-link>
            </li>
            <div v-if="!this.$store.state.token">
              <!-- <li class="nav-item">
                <router-link v-bind:to="{name:'SignUpView'}" class="nav-link">SignUp</router-link>
              </li> -->
              <li class="nav-item">
                <router-link v-bind:to="{name:'LoginView'}" class="nav-link">LogIn</router-link>
              </li>
            </div>
            <div v-else>
              <li class="nav-item" type="button" @click="logout">
                <a class="nav-link">Logout</a>
              </li>
              <li class="nav-item">
                <router-link v-bind:to="{name:'MyPageView'}" class="nav-link">MyPage</router-link>
              </li>
            </div>  
          </ul>
        </div>
      </nav>
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
html
body {
  background-color:black;
  color:white;
  font-family: 'Prompt', sans-serif;
}

.nav-item{
  list-style-type:none;
  float:left;
}

</style>