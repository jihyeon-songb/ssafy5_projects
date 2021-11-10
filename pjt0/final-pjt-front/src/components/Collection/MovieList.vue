<template>
  <div>
      <div class="noMovie" v-if="movies.length === 0">
        <img src="../../../public/sorry.png" alt="">
        <br>
        찾는 영화가 없습니다.
      </div>
    <div class="movieList">
      <MovieItem v-for="(movie, idx) in movies" :key="idx" :movie="movie" />
    </div>
  </div>
</template>

<script>
import MovieItem from '@/components/Collection/MovieItem'
export default {
  name: 'MovieList',
  props: {
    movies: Array,
  },
  components: {
    MovieItem,
  },
  watch: {
    movies (newMovies) {
      if (newMovies.length === 100) {
        this.movies = [];
      }
      }
    }
}
</script>

<style scoped>

.noMovie {
  display: block;
  text-align: center;
  font-size: 20px;
  font-weight: bold;
  opacity: 50%;
  word-break: break-all;
  margin: 50px;
}
img {
  width: 200px;
  opacity: 30%;
}
</style>