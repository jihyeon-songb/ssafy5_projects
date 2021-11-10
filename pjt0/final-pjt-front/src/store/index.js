import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import Dropdown from 'vue-simple-search-dropdown'
import createPersistedState from 'vuex-persistedstate';

Vue.use(Vuex, Dropdown)

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default new Vuex.Store({
  plugins: [
    createPersistedState()
  ],
  state: {
    movieDetail: null,
    movies: null,
    selectedMovies : [],
  },
  mutations: {
    GET_MOVIES: function(state, movies) {
      state.movies = movies
    },
    GET_MOVIE: function(state, movie) {
      state.movieDetail = movie
      console.log(state.movieDetail)
    },
    SELECT_MOVIE : function (state, movieItem) {
      let check = ''
      state.selectedMovies.find((movie, idx) => {
        if (movie.id === movieItem.id) {
          check = idx
      }})
          if (check === '') {
            state.selectedMovies.push(movieItem)
          } else {
            state.selectedMovies.splice(check, 1)
          }
      },
      COLLECTION_RESET : function (state) {
        state.selectedMovies = [];
      }
    },
  actions: {
    getMovies: function ({commit}) {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'get',
        url: `${SERVER_URL}/movies/movie/`,
        headers: {
          Authorization: `JWT ${token}`
          }
        })
      .then((res) => {
        commit('GET_MOVIES', res.data)
        console.log(res.data)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    getMovie: function ({commit}, movie) {
      commit('GET_MOVIE', movie)
    },
    selectMovie: function ({ commit }, movieItem) {
      commit('SELECT_MOVIE', movieItem)
    },
    saveCollection: function ({ commit }, data) {
      const token = localStorage.getItem('jwt')
      let form = new FormData()
      let movies = []
      for (let i = 0; i < this.state.selectedMovies.length; i++ ) {
        movies.push(this.state.selectedMovies[i]['id'])
      }
      form.append('movies', movies)
      form.append('title', data.title)
      form.append('info', data.info)
      axios({
        method: 'post',
        url: `${SERVER_URL}/movies/collections_all/`,
        data: form,
        headers: {
          Authorization: `JWT ${token}`
          }
        })
        .then (() => {
          commit('COLLECTION_RESET')
        })
        .catch((err) => {
          console.log(err)
        })
  },
},
  modules: {
  },
  getters: {

  }
})
