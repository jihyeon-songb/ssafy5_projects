<template>
  <div  style="margin-top:50px;">
    <h3 class=mb-3>Review</h3>
    <div>
      <label for="title"></label>
      <input type="text" id="title" v-model.trim="review.title" >
    </div>
    <div>
      <label for="content"></label>
      <textarea type="text" id="content" v-model.trim="review.content" ></textarea>
    </div>
    <div>
      <label for="star_rating"></label>
      <input type="number" @keypress.enter="createReview" id="star_rating" v-model="review.star_rating" min="0" max="5">
    </div>
    <button class="btn btn-outline-success mt-3 snip1535" @click="updateReview">Save</button>
  </div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'CreateReview',
  data: function () {
    return {
      review: {
        id: this.$route.params.reviewItem.id,
        title: this.$route.params.reviewItem.title,
        content: this.$route.params.reviewItem.content,
        star_rating: this.$route.params.reviewItem.star_rating,
      },
      movieId: this.$route.params.movieId,
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
    updateReview: function () {
      const config = this.setToken()
      const reviewItem = {
        'title': this.review.title,
        'content': this.review.content,
        'star_rating': this.review.star_rating,
      }
      axios.put(`${SERVER_URL}/community/review/${this.review.id}/`,reviewItem, config)
      .then((res) => {
          console.log(res)
          this.$router.push({ name  :'ReviewDetail', params:{ reviewId:res.data.id , username: localStorage.getItem('myname') }})
          })
          .catch((err) => {
          console.log(err)
          })
    }
  }
}
</script>

<style scoped>

input, textarea {
  width: 350px;
  display: block;
  margin: auto;
  border-bottom: rgb(152, 12, 233) 1.5px solid;
  border-left: medium none;
  border-right: medium none;
  border-top: medium none;
  outline: none;
}
textarea {
  height: 150px;
}

.snip1535 {
  background-color: rgba(123, 18, 221, 0.6);;
  border: none;
  color: #ffffff;
  cursor: pointer;
  display: inline-block;
  font-family: 'BenchNine', Arial, sans-serif;
  font-size: 1em;
  font-size: 22px;
  line-height: 1em;
  margin: 15px 40px;
  outline: none;
  padding: 12px 40px 10px;
  position: relative;
  text-transform: uppercase;
  font-weight: 700;
}
.snip1535:before,
.snip1535:after {
  border-color: transparent;
  -webkit-transition: all 0.25s;
  transition: all 0.25s;
  border-style: solid;
  border-width: 0;
  content: "";
  height: 24px;
  position: absolute;
  width: 24px;
}
.snip1535:before {
  border-color: rgba(123, 18, 221, 0.6);;
  border-right-width: 2px;
  border-top-width: 2px;
  right: -5px;
  top: -5px;
}
.snip1535:after {
  border-bottom-width: 2px;
  border-color: rgba(123, 18, 221, 0.6);;
  border-left-width: 2px;
  bottom: -5px;
  left: -5px;
}
.snip1535:hover,
.snip1535.hover {
  background-color: rgba(123, 18, 221, 0.6);
}
.snip1535:hover:before,
.snip1535.hover:before,
.snip1535:hover:after,
.snip1535.hover:after {
  height: 100%;
  width: 100%;
}
</style>