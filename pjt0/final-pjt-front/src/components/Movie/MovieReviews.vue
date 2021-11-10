<template>
    <!-- <h1>{{ movieId }}</h1> -->
    <div class="">
      <ul>
        <ReviewListItem v-for="(review, idx) in movieReviews" v-bind:key="idx" :review="review"/>
      </ul>
    </div>
    
</template>

<script>
import axios from 'axios'
import ReviewListItem from '@/components/Review/ReviewListItem'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
 
export default {
  name: 'MovieReviews',
  components:{
    ReviewListItem,
  },
  props: {
    movieId: {
      type: [Number,String],
    }
  },
  data: function () {
    return { 
      movieReviews: null,
    }
  },
  methods: {
   setToken: function( ) {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getMovieReviews: function() {
      const config = this.setToken()
      let sum = 0
      axios.get(`${SERVER_URL}/community/movie/${this.movieId}`,config)
      .then((res) => {
        res.data.forEach((element) => {
          sum += element.star_rating
        })
        console.log(sum)
        this.$emit('reviewLength',res.data.length, sum)
        console.log('리뷰들 나옴')
        console.log(res)
        this.movieReviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
  },
  mounted() {
    this.getMovieReviews()
  }
}
</script>

<style>

</style>