<template>
  <div id="app">
    <div id="nav">
      <nav class="navbar navbar-expand-lg bg-transparent py-0 ms-2">
        <div class="container-fluid">
          <div>
            <a class="navbar-brand text-decoration-none" href="/home/"><img src="./assets/profile.png" alt="" style="width:80px;"></a>
          </div>
        <Dropdown
            :options="allMovie"
            v-on:selected="validateSelection"
            :disabled="false"
            placeholder="찾고싶은 영화를 검색해보세요"
            >
        </Dropdown>

          <div class="nav-item dropdown">
            <span v-if="login">
              <a class="nav-link dropdown-toggle text-dark" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                MY PAGE
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
                <li><a class="dropdown-item" @click="logout">Logout</a></li>
                <li><a class="dropdown-item" ><span @click="goProfile">Profile</span>
                  <!-- <router-link :to="{ path: '/accounts/'+`${myId}`+'/detail'}" class="text-decoration-none">Profile</router-link> -->
                  </a></li>
                <!-- <li><hr class="dropdown-divider"></li> -->
              </ul>
            </span>
            <span v-else>
              <span class="me-3" v-if="clickLogin" @click="clickSignUpLink">
              <router-link :to="{ name: 'Signup' }" class="text-decoration-none text-dark">Signup</router-link>
              </span>
              <span v-else @click="clickLoginLink">
              <router-link :to="{ name: 'Login' }" class="text-decoration-none text-dark me-3">Login</router-link>
              </span>
            </span>
          </div>
        </div>
      </nav>
    </div>
    <router-view :key="$route.fullpath" @login="login = true"/>
  </div>
</template>

<script>
import Dropdown from 'vue-simple-search-dropdown';
import{ mapActions, mapState, mapMutations } from 'vuex'

export default {
  name: 'App',
  data: function () {
    return {
      clickLogin: false,
      login: false,
      username: '',
      myId: '',
      searchVal: '',
      allMovie: [],
      selected: { name: null, id: null },
    }
  },
  components: {
    Dropdown,
  },
  methods: {
    clickLoginLink: function(){
      this.clickLogin = true
      console.log(this.clickLogin)
    },
    clickSignUpLink: function(){
      this.clickLogin = false
    },
    logout: function () {
      console.log('logout 됨')
      this.login = false
      localStorage.removeItem('jwt')
      this.$router.push({ name: 'Login' })
    },
      ...mapActions({
      init: 'getMovies'
    }),
     validateSelection(selection) {
        this.selected = selection;
        if (selection.id !== undefined) {
          console.log(selection)
          this.GET_MOVIE(selection)
          this.$router.push({ name: 'MovieDetail', params: { movieId: selection.id}})
        }
      },
      ...mapMutations([
        'GET_MOVIE'
      ]),
      goProfile: function() {
        const myId = localStorage.getItem('myId')
        this.$router.replace('/accounts/'+`${myId}`+'/detail')
      }
  },
  created: function () {
    const token = localStorage.getItem('jwt')
    const myId = localStorage.getItem('myId')
    if (token) {
      this.login = true
      this.myId = myId
    }
  },
    computed:{
    ...mapState({
      movies: 'movies',
    })
  },
    mounted() {
    this.init()
    },
    watch: {
      movies (newMovies) {
        this.allMovie = [];
        for (let i = 0; this.movies.length > i; i++){
          this.allMovie.push({id: newMovies[i].id, name: newMovies[i].title, title: newMovies[i].title, release_date: newMovies[i].release_date, poster_path: newMovies[i].poster_path, overview: newMovies[i].overview }
            )
          }
      }
    }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@900&display=swap');

#app {
  font-family: 'Roboto', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.dropdown-input {
  background: url("./assets/loupe.png") no-repeat scroll 7px 7px !important;
  padding-left:30px !important;
  background-color: #F5F5F7 !important;
  margin-right:32px;
}
.dropdown-input::placeholder {
  color: #74747B !important;
}
</style>
