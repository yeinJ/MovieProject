<template>
  <div id="app">
      <nav class="navbar navbar-expand-sm navbar-light bg-danger">
        <div class="container-fluid">
          <ul class="navbar-nav">
            <li class="nav-item">
              <router-link v-bind:to="{name:'HomeView'}" class="nav-link">Home</router-link>
            </li>
            <li class="nav-item">
              <router-link v-bind:to="{name:'SignUpView'}" class="nav-link">SignUp</router-link>
            </li>
            <li class="nav-item">
              <router-link v-bind:to="{name:'LoginView'}" class="nav-link">LogIn</router-link>
            </li>
            <li class="nav-item">
              <router-link v-bind:to="{name:'MyPageView'}" class="nav-link">MyPage</router-link>
            </li>
          </ul>
        </div>
      </nav>
      <!-- <div v-if="!cookie">
        <router-link v-bind:to="{name:'HomeView'}">Home</router-link> |
        <router-link v-bind:to="{name:'SignUpView'}">회원가입</router-link> |
        <router-link v-bind:to="{name:'LoginView'}">로그인</router-link>
      </div>
      <div v-else>
        <router-link v-bind:to="{name:'HomeView'}">Home</router-link> |
        예인님! |
        <router-link type="button" class="logoutButton" v-on:click="logout" v-bind:to="{name:'HomeView'}">로그아웃</router-link>
      </div> -->
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
    // logout() {
    //   console.log('로그하웃하실?')
    // }
  }


}


</script>

<style>
html
body {
  background-color:black;
  color:white
}
</style>