<template>
  <div>
    <img :src="movieImage" alt="title">
  </div>
</template>

<script>
export default {
  name: 'selectedMovieItem',
  props: {
    movie: Object,
  },
  computed: {
    movieImage: function () {
      if (this.movie.poster_path) {
        return `https://image.tmdb.org/t/p/w500/${this.movie.poster_path}`
      }
      return false
      }
  },
}
</script>

<style scoped>
img {
  float: left;
  border-radius: 7px;
  width : 100px; 
  height: 150px;
  margin-bottom: 10px;
}
div {
  display: inline-block;
}
</style>