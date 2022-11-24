<template>
  <div>
    <div class="loginbox">
      <h1>LogIn</h1>
      <b-form  v-on:submit.prevent="logIn">
        <label for="username">User ID</label>
          <b-form-input type="text" id="username" v-model.trim="username"></b-form-input>

        <label for="password" >Password</label>
          <b-form-input type="password" id="password" v-model.trim="password" aria-describedby="password-help-block"></b-form-input>

        <!-- <input type="submit" value="logIn"> -->
        <b-button class='loginbutton' type="submit" value="logIn" block variant="danger">LogIn</b-button>
      </b-form>
      <div class="signup">
      <br>
        <span>Are you New?</span>
        <br> 
        &nbsp;
        <b-button block variant="dark" :to="{ name: 'SignUpView' }">SignUp</b-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name:'LoginView',
  data() {
    return {
      username: '',
      password: '',
    }
  },

  methods : {
    logIn() {
      const username = this.username
      const password = this.password

      if (!username) {
        this.$swal({
            text: 'ID를 입력하세요.',
            confirmButtonColor: '#d33',
            confirmButtonText: '😢',
        })
      } else if (!password) {
        this.$swal({
            text: 'Password를 입력하세요.',
            confirmButtonColor: '#d33',
            confirmButtonText: '😢',
        })
      } else {
        const payload = {
          username: username,
          password: password,
        }
        this.$store.dispatch('logIn',payload)
      }
    }
  }

}
</script>

<style scoped>

h1{
  text-align:center;
}
.loginbox{
  margin-top: 40px;
  padding-left : 40%;
  padding-right : 40%;
  margin-bottom: 30%;
}
.loginbutton{

    margin-top : 10%;
  }

</style>