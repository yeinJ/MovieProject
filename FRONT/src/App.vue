<template>
  <div id="app">
    <nav>
      <div v-if="!cookie">
        <router-link v-bind:to="{name:'HomeView'}">Home</router-link> |
        <router-link v-bind:to="{name:'SignUpView'}">회원가입</router-link> |
        <router-link v-bind:to="{name:'LoginView'}">로그인</router-link>
      </div>
      <div v-else>
        <router-link v-bind:to="{name:'HomeView'}">Home</router-link> |
        예인님! |
        <router-link type="button" class="logoutButton" v-on:click="logout" v-bind:to="{name:'HomeView'}">로그아웃</router-link>
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
    cookie() {
      return document.cookie
    }
  },
  methods : {
    logout() {
      console.log('로그하웃하실?')
    }
  }


}


</script>