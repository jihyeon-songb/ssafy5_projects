<template>
  <div>
    <VueSlickCarousel v-bind="settings">
     <MovieListItem v-for="(movie,idx) in movies.slice(85)" :key="idx" :movie="movie" />
    </VueSlickCarousel>
    <ul>
    </ul>
  </div>
</template>

<script>
// import _ from 'lodash'
import MovieListItem from '@/components/Movie/MovieListItem'
import VueSlickCarousel from 'vue-slick-carousel'
import 'vue-slick-carousel/dist/vue-slick-carousel.css'
import 'vue-slick-carousel/dist/vue-slick-carousel-theme.css'

export default {
  name:'MovieList',
  data: function() {
    return {
      settings: {
        "centerMode": true,
        "centerPadding": "15px",
        "focusOnSelect": true,
        "infinite": true,
        "slidesToShow": 5,
        "speed": 500
      }
    }
  },
  components: {
    MovieListItem,
    VueSlickCarousel
  },
  props: {
    movies: Array,
  },
}

</script>

<style>
</style>