<template>
  <div id="backGround">
    <div class="clearfix2">
      <p class="loginbox text-light text-center">
       Sign Up
      <input class="px-1 mt-2" type="text" id="username" placeholder="ID" v-model="credentials.username">
      <input class="px-1" type="password" id="password" placeholder="Password" v-model="credentials.password">
      <input class="px-1" type="password" id="passwordConfirmation" placeholder="PasswordConfirm" v-model="credentials.passwordConfirmation"
      @keypress.enter="signup(credentials)">
      <button class="mt-2 p-0" @click="signup(credentials)"><p class="mb-0">Sign up</p>
        </button>
      </p>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: '',
        password: '',
        passwordConfirmation: '',
      }
    }
  },
  methods: {
    signup: function (credentials) {
      console.log(credentials)
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/user/`,
        data: this.credentials,
      })
      .then((res) => {
        console.log(res)
        this.$router.push({ name: 'Login' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  }
}
</script>

<style scoped>
  #backGround {
  height: 100vh;
  background-repeat:no-repeat;
  background-position: center;
  background-size: cover;
  }
  #backGround {
  /* height: 100%; */
  background: linear-gradient(315deg,#fc00aa,#00dbde);
  overflow: hidden;
  }

.clearfix2 {
  position: absolute;
  width: 250px;
  height: 170px;
  top: 50%;
  left: 50%;
  margin-left: -125px;
  margin-top: -85px;
  background: rgba(255,255,255,0.05);
  backdrop-filter: blur(10px);
  border-top: 1px solid rgba(255,255,255,0.1);
  border-left: 1px solid rgba(255,255,255,0.1);
  box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
  border-radius: 3px;
}

.loginbox button {
  position: relative;
  color: white;
  width: 100%;
  /* border-radius: 8px; */
  background: rgba(255,255,255,0.05);
  border-top: 1px solid rgba(255,255,255,0.1);
  border-left: 1px solid rgba(255,255,255,0.1);
  border-right: 1px solid rgba(2, 2, 2, 0.4);
  border-bottom: 1px solid rgba(2, 2, 2, 0.4);
  box-shadow: 5px 5px 30px rgba(0,0,0,0.2);
  font-size: 13px;
}
.loginbox {
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
}
.loginbox input {
  position: relative;
  /* border-radius: 8px; */
  border: none;
  background: rgba(255,255,255,0.05);
  backdrop-filter: blur(10px);
  border-top: 1px;
  border-left: 1px;
  /* box-shadow: 5px 5px 30px rgba(0,0,0,0.2); */
  color: rgb(255, 255, 255);
  transition: color 0.3s ease-out;
}
input::placeholder {
  color: rgba(255,255,255,0.6);
  font-size: 12px;
}
</style>