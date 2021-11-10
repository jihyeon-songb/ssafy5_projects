<template>
  <div>
    <iframe
       allowFullScreen
       frameborder="0"
       height="376"
       :src="movieTrailer"
       style="width: 100%; min-width: 536px"
      />
  </div>
</template>

<script>
import {mapState} from 'vuex'


export default {
  name: 'Trailer',
  props: {
    flag: Boolean,
  },
  computed: {
    movieTrailer: function () {
      return `https://www.youtube.com/embed/${this.movieDetail.trailer_path}`
    },
    ...mapState([
      'movieDetail',
    ]),
  },
}
</script>

<style>

</style>