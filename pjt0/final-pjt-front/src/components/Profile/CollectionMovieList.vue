<template>
<div>
    <CollectionMovieDetail :title="title" :poster_path="poster_path" />
</div>
</template>

<script>
import axios from 'axios'
import CollectionMovieDetail from '@/components/Profile/CollectionMovieDetail.vue'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name : 'CollectionMovieList',
  components: {
    CollectionMovieDetail,
  },
  data : function () {
    return {
      title : null,
      poster_path : null,
    }
  },
  props: {
    movie: Number,
  },
  created: function () {
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${SERVER_URL}/movies/movie/`,
        data: this.movie,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        if (Object.prototype.hasOwnProperty.call(res.data, 'detail')) {
          this.title = null;
          }
        else {
          this.title = res.data.title
          this.poster_path = res.data.poster_path
          }
      })
      .catch((err) => {
        console.log(err)
      })
  },
}
</script>

<style scoped>
</style>