<template>
  <div>
    <div class="Signupbox">
      <h1>Sign Up</h1>
      <b-form  v-on:submit.prevent="signUp">
        <label for="username">User ID</label>
          <b-form-input type="text" id="username" v-model="username" v-bind:state="validation"></b-form-input>
          <b-form-invalid-feedback v-bind:state="validation">
            Your user ID must be 5-12 characters long.
          </b-form-invalid-feedback>
          <b-form-valid-feedback v-bind:state="validation">
            Looks Good.
          </b-form-valid-feedback>
          
        <label for="password1" >Password1</label>
          <b-form-input type="password" id="password1" v-model="password1" ></b-form-input>

        <label for="password2" >Password2</label>
          <b-form-input type="password" id="password2" v-model="password2" ></b-form-input>
        <!-- <input type="submit" value="SignUp"> -->
        <b-button class='signupbutton' type="submit" value="SignUp" block variant="danger">SignUp</b-button>
      </b-form>
    </div>

  </div>
</template>

<script>
export default {
  name : 'SignUpView',
  data() {
    return {
      username : '',
      password1 : '',
      password2 : '',
    }
  },
  computed: {
      validation() {
        return this.username.length > 4 && this.username.length < 13
      },
      // passwordvalidation1() {
      //   return this.password1.length>7 && this.password1.length<21 
      // }


  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp',payload)
    },
    // passwordvalidation2() {
    //   if (this.password1===this.password2 && this.password2!==''){
    //     return this.password2
    //   }
    // }


  }

}
</script>

<style scoped>
  h1{
    text-align : center;
  }
  .Signupbox {
    margin-top: 40px;
    padding-left : 40%;
    padding-right : 40%
  }
  .signupbutton{
    margin-top : 10%;
  }

</style>