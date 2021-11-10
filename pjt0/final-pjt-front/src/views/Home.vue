<template>
  <div>
    <span>오늘의 인기영화</span>
    <MovieList :movies="movies"/>
    <br>

    <div v-if="following_name">
      <span>{{ following_name }} 님의 컬렉션</span>
      <div class="collection">
        <div class="collectionList">
        <CollectionMovieList v-for="(movie, idx) in following_movies" :key="idx" :movie="movie" />
        </div>
      </div>
    </div>

    <div v-else>

    </div>
  </div>
</template>

<script>
import _ from 'lodash'
import axios from 'axios'
import{ mapActions, mapState } from 'vuex'
import MovieList from '@/components/Movie/MovieList'
import CollectionMovieList from '@/components/Profile/CollectionMovieList.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Home',
  data: function () {
    return {
      followings: null,
      following_movies: [],
      following_name: '',
      randomNum: '',
      idCheck: '',
    }
  },
  components: {
    MovieList,
    CollectionMovieList,
  },
  methods: {
    setToken: function( ) {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    // getCollections: function () {
    //   const config = this.setToken()
    //   axios.get(`${SERVER_URL}/movies/collection_all/`, config)
    //   .then((res) => {
    //     console.log(res)
    //   })
    //   .catch((err) => {
    //     console.log(err)
    //   })
    // },

    getFollow: function() {
    const config = this.setToken()
    const myId = localStorage.getItem('myId')
    this.idCheck = myId
    axios.get(`${SERVER_URL}/accounts/${myId}/detail/`, config)
      .then((res) => {
        this.followings = res.data.followings
        this.randomNum = _.sampleSize(this.followings, 1)

      axios.get(`${SERVER_URL}/movies/collection_list/${this.randomNum}/`)
      .then((res) => {
        const data = res.data
        let randomNum2 = _.sampleSize(_.range(data.length), 1)
        this.following_movies = res.data[randomNum2].movies
        this.following_name = res.data[randomNum2].user.username
      })
      .catch((err) => {
        console.log(err)
      })
      })
      .catch((err) => {
        console.log(err)
      })  
    },
    ...mapActions({
      init: 'getMovies'
    })
  },
  computed:{
    ...mapState([
      'movies',
    ])
  },
  mounted() {
    this.init()
  },
  created() {
    this.getFollow()
  },
  watch :{
    myId: function () {
      this.getFollow()
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@900&display=swap');

span {
  display:flex;
  justify-content: start;
  margin-left: 50px;
  margin-top: 30px;
  font-weight: 10;
  font-size: 20px;
  color: black;
  font-family: 'Roboto', sans-serif;
}

.collectionList {
  display: flex;
  justify-content:flex-start;
  margin-top: 20px;
  margin-left: 30px;
}
</style>