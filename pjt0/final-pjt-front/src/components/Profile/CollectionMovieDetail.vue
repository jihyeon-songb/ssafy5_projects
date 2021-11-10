<template>
<div>
  <div class= "container" v-if="title">
    <div>
      <img :src="movieImage" :alt="title">
    </div>
    <div class="movieTitle">
      {{ title }}
    </div>
  </div>
  <div v-else>
    컬렉션에 저장된 영화가 없습니다.
   </div>
  </div>
</template>

<script>


export default {
  name: 'CollectionMovieDetail',
  props: {
    title: [String, null],
    poster_path: [String, null],
    idx: [Number, null], 
  },
  data: function() {
    return {
    }
  },
  computed: {
    movieImage: function () {
      if (this.poster_path) {
        return `https://image.tmdb.org/t/p/w500/${this.poster_path}`
      }
      return false
      }
  },
}
</script>

<style scoped>
.container {
  display: block;
  margin-top: 10px;
  width : 175px; 
  height: 225px;
  word-break: break-all;
}
img {
  border-radius: 7px;
  display: inline-block;
  width : 150px; 
  height: 200px;
  margin-bottom: 10px;
}
</style>