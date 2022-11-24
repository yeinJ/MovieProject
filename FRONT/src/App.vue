<template>
  <div id="app">
      <b-navbar toggleable="md" type="dark" variant="danger">
  
          <router-link v-bind:to="{name:'HomeView'}" class="nav-link">
            <img src="../public/hypy.png" alt="Hypy">
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
      
      <footer class="footer">
        <hr color="gray">
        <b-icon class='footer-icon' icon="suit-club-fill" scale="2" v-on:click="lucky" variant="dark"></b-icon>
        <div class="footer-main">
          <div class="footer-say">본 사이트의 콘텐츠는 저작권법의 보호를 받는 바 무단 전재, 복사, 배포 등을 금합니다.</div>
          <div class="footer-desc">Copyright © HAEUN&YEIN All Rights Reserved.</div>
        </div>
      </footer>
    
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
    },
    lucky() {
      this.$swal({
            text: '행복을 찾으셨군요! 행복하세용 😆',
            confirmButtonColor: '#d33',
            confirmButtonText: '감사합니당',
        })

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

.footer{
  margin : 0 4% 2% 4%;
}

.footer-icon{
  position:absolute;
  margin-top:1%;
  margin-left : 1%;
}

.footer-main{
  margin-left:5%;
}

.footer-desc{
  font-size: 12px;
  color: #fff;
  font-weight: 200;
  margin-bottom:10px;
}

.footer .footer-say {
    padding: 0 0 10px;
    font-size: 12px;
    color: #8c99a8;
}

.swal2-container.swal2-center>.swal2-popup{
  background-color: #121212 !important;
  color:white;
}
</style>