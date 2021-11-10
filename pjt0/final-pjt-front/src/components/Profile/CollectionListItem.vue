<template>
  <div>
    <div class="collection">
        <div class="collectionText">
          <div class="title">{{ collection.title }}</div>
          <div class="info">{{ collection.info }}</div>
      </div>
      <div class="collectionList">
          <CollectionMovieList v-for="(movie, idx) in movies" :key="idx" :movie="movie"/>
      </div>
    <!-- <button @click="updateCollection">수정</button> -->
    </div>
  </div>
</template>

<script>

import CollectionMovieList from '@/components/Profile/CollectionMovieList.vue'

export default {
  name: 'CollctionListItem',
  components: {
    CollectionMovieList,
  },
  data: function() {
    return {
      movies: null,
  }},
  props: {
    collection: {
      type: Object,
    }
  },
  created: function () {
    this.movies = this.collection.movies.length !== 0 ? this.collection.movies : [0]
  },
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans:wght@700&display=swap');

.collection {
  margin-bottom: 55px;
}
.collectionText {
  display: block;
  text-align: start;
  height: 50px;
  margin-left: 20px;
}
.collectionList {
  display: flex;
  justify-content:flex-start;
  margin-top: 20px;
}
.title {
  font-size: 20px;
}
.info {
  font-family: 'Noto Sans', sans-serif;
  font-weight: bold;
  font-size: 28px;
}
</style>