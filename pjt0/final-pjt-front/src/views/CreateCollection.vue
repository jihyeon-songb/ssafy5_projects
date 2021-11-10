<template>
  <div class="container">
    <div class="search">
      <h3>search</h3>
      <SearchBar @input-search="onInputSearch"/>
      <MovieList :movies="movies" />
    </div>
    <div class="myCollection">
      <h3>collection</h3>
        <selectedMovieItem v-for="(movie, idx) in selectedMovies" :key="idx" :movie="movie" />
          <div>
            <input class="mt-3" type="text" placeholder="컬렉션에 알맞은 제목을 지어주세요." v-model="data.title" >
          </div>
          <div>
            <textarea v-model="data.info" class="mt-5" placeholder="컬렉션에 대해 설명해주세요."></textarea>
          </div>
            <button @click="saveCollection(data); clear();" class="btn btn-outline-success mt-3 snip1535">SAVE</button> 
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { mapState, mapActions } from 'vuex'
import SearchBar from '@/components/Collection/SearchBar'
import MovieList from '@/components/Collection/MovieList'
import selectedMovieItem from '@/components/Collection/selectedMovieItem'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'CreateCollection',
  components: {
    SearchBar,
    MovieList,
    selectedMovieItem,
  },
  data: function () {
    return {
      inputValue: '',
      searchVal: '',
      movies: [],
      data: {
        title: '',
        info: '',
        myId: '',
      },
      updatedMovies: [],
      collection_id: '',
      check: 'create',
    }
  },
  props: {
    collection : Object,
  },
  methods: {
   onInputSearch: function (inputText) {
      this.searchVal = inputText
      const token = localStorage.getItem('jwt')
      let form = new FormData()
      form.append('searchVal', this.searchVal)
      axios({
        method: 'post',
        url: `${SERVER_URL}/movies/search/`,
        data: form,
        headers: {
          Authorization: `JWT ${token}`
          }
        })
        .then((res) => {
          this.movies = res.data
          for (let i = 0; this.movies.length; i++) {

            if (!Object.prototype.hasOwnProperty.call(this.movies[i], 'isSelected')) {
              this.movies[i]['isSelected'] = false
            }
          }
        })
        .catch((err) => {
          console.log(err)
        })
      },
      ...mapActions([
        'saveCollection',
      ]),
      clear: function () {
        this.data.title = ''
        this.data.info = ''
        this.$router.replace('/accounts/'+`${this.myId}`+'/detail')
      },
    },
  computed: {
    ...mapState([
      'selectedMovies',
    ]),
  },
  created: function () {
    const myId = localStorage.getItem('myId')
    this.myId = myId
  }
}
</script>

<style scoped>
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    margin-top: 30px;
  }
.search {
  width: 500px;
}
.myCollection {
  width: 500px;
  display: block;
}
input, textarea {
  width: 350px;
  display: block;
  margin: 0 auto;
  border-bottom: teal 1.5px solid;
  border-left: medium none;
  border-right: medium none;
  border-top: medium none;
  outline: none;
}
textarea {
  height: 150px;
}
input::placeholder {
  color: black;
}
.snip1535 {
  background-color: #4ca1a3;
  border: none;
  color: #ffffff;
  cursor: pointer;
  display: inline-block;
  font-family: 'BenchNine', Arial, sans-serif;
  font-size: 1em;
  font-size: 22px;
  line-height: 1em;
  margin: 15px 40px;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
  text-transform: uppercase;
  font-weight: 700;
}
.snip1535:before,
.snip1535:after {
  border-color: transparent;
  -webkit-transition: all 0.25s;
  transition: all 0.25s;
  border-style: solid;
  border-width: 0;
  content: "";
  height: 24px;
  position: absolute;
  width: 24px;
}
.snip1535:before {
  border-color: #4ca1a3;
  border-right-width: 2px;
  border-top-width: 2px;
  right: -5px;
  top: -5px;
}
.snip1535:after {
  border-bottom-width: 2px;
  border-color: #4ca1a3;
  border-left-width: 2px;
  bottom: -5px;
  left: -5px;
}
.snip1535:hover,
.snip1535.hover {
  background-color: #4ca1a3;
}
.snip1535:hover:before,
.snip1535.hover:before,
.snip1535:hover:after,
.snip1535.hover:after {
  height: 100%;
  width: 100%;
}
</style>