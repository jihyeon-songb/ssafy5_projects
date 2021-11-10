<template>
  <div id="imageDiv">
    <img class="mt-3 " @click="goMovieDetail(movie.id),getMovie(movie)" :src="movieImage" alt="movie_image">
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'MovieListItem',
  props: {
    movie: Object,
  },
  methods:{
    ...mapActions([
      'getMovie',     
    ]),
    goMovieDetail: function (movieId) {
      this.$router.push({ name: 'MovieDetail', params: { movieId: movieId }})
    }
  },
  computed: {
    movieImage: function () {
      return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
      }
  },
}
</script>

<style scoped>
 #imageDiv {
   margin-top: 10px;
 }
 img {
   border: 1px solid lightgray;
   border-radius: 7px;
   width: 200px;
 }
</style>