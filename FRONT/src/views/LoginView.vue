<template>
  <div>
    <h1>LogIn Page</h1>
    <!-- <form v-on:submit.prevent="logIn">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password"> password : </label>
      <input type="password" id="password" v-model="password"><br>

      <input type="submit" value="logIn">
    </form> -->
    <b-form  v-on:submit.prevent="logIn">
      <label for="username">User ID</label>
        <b-form-input type="text" id="username" v-model="username" v-bind:state="validation"></b-form-input>
        <b-form-invalid-feedback v-bind:state="validation">
          Your user ID must be 5-12 characters long.
        </b-form-invalid-feedback>
        <b-form-valid-feedback v-bind:state="validation">
          Looks Good.
        </b-form-valid-feedback>
      <label for="password" >Password</label>
        <b-form-input type="password" id="password" v-model="password" aria-describedby="password-help-block"></b-form-input>
        <b-form-text id="password-help-block">
         Your password must be 8-20 characters long, contain letters and numbers, and must not
         contain spaces, special characters, or emoji.
        </b-form-text>
      <input type="submit" value="logIn">
    </b-form>
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
  computed: {
      validation() {
        return this.username.length > 4 && this.username.length < 13
      }
  },
  methods : {
    logIn() {
      const username = this.username
      const password = this.password

      const payload = {
        username: username,
        password: password,
      }
      this.$store.dispatch('logIn',payload)
    }
  }

}
</script>

<style>

</style>