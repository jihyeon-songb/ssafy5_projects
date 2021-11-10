<template>
<div class="">
  <h3 class="mt-3"><span @click="goUserProfile">{{ username }}</span>님의 리뷰</h3>
  <hr>
  <div v-if="requestUsername == username">
    <button class="noBorderSubmit btn mx-1 px-2 py-1" @click="updateReview">수정</button>
    <button class="noBorderSubmit btn px-2 py-1" @click="deleteReview">삭제</button>
  </div>
  <div id="reviewDetail" class="">
    <div id="border" class="mt-3 p-3">
      <div class="d-flex justify-content-between">
        <div class="mt-2 mb-3 d-flex">
        <h3 class="mx-4 mb-1"> {{ review.star_rating }}점</h3>
        <h4 class="mt-1">: {{ review.title }}</h4>
        </div>
      </div>
    <div class="p-4 fw-bold">
      <p>{{ review.content }}</p>
      <!-- <p>{{ review.updated_at }}</p> -->
    </div>
    <div class="d-flex">
      <div>
        <span v-if="heart">
          <button class="submit btn btn-secondary" @click="unlike">
            <i id="heart" class="fas fa-heart"></i>
          </button>
        </span>
        <span v-else>
          <button class="submit btn btn-secondary" @click="Like">
            <i class="fas fa-heart"></i>
          </button>   
        </span>
          <p class="mb-0" style="font-size:12px;">
            {{ review.like_count }}
          </p>
      </div>
      <div>
        <span v-if="message">
          <button class="submit btn btn-secondary" @click="noCommentView">
          <i class="far fa-comment" ></i>
          </button>
        </span>
        <span v-else>
          <button class="submit btn btn-secondary" @click="commentView">
            <i class="fas fa-comment"></i>
          </button>
        </span>
        <p class="mb-0" style="font-size:12px;">
          {{ review.comment_count }}
        </p>
      </div>
      </div>
    <!-- <p>username: {{ username }}</p> -->
 <!-- <i class="fas fa-heart" style="color:red;"></i> -->
    <CommentList :review="review" :message="message"/>
    </div>
  </div>
  <div>
    <button class="submit" @click="goMovieDetail">back</button>
  </div>
</div>
</template>

<script>
import axios from 'axios'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import CommentList from '@/components/Comment/CommentList'

export default {
  name: 'ReviewDetail',
  components: {
    CommentList,
  },
  data: function () {
    return {
      heart: false,
      message: false,
      requestUsername: localStorage.getItem('myname'),
      reviewId: this.$route.params.reviewId,
      username: '',
      review: [],
    }
  },
  methods: {
    goMovieDetail: function() {
      this.$router.push({ name: 'MovieDetail', params: { movieId: this.$route.params.movieId , starRating: this.review.star_rating }})
    },
    goUserProfile: function () {
      this.$router.push({ name: 'Profile' , params:{ user_id:this.review.user}})
    },
    noCommentView: function() {
      this.message = false
    },
    commentView:function(){
      this.message = true
    },
    unlike: function() {
      this.heart = false
      this.review.like_count -= 1
    },
    Like: function() {
      this.heart = true
      this.review.like_count += 1
    },
    setToken: function( ) {
      const token = localStorage.getItem('jwt')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }
      return config
    },
    getReview: function () {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/community/review/${this.reviewId}/`,config)
      .then((res) => {
          console.log('리뷰나옴')
          console.log(res.data)
          this.review = res.data
          const userId = this.review.user
          this.getUsername(userId)
          })
          .catch((err) => {
          console.log(err)
          })
    },
    deleteReview: function () {
      const config = this.setToken()
      axios.delete(`${SERVER_URL}/community/review/${this.reviewId}/`,config)
      .then((res) => {
          console.log(res)
          this.$router.push({ name: 'MovieDetail', params:{ movieId:this.review.movie }})
          })
          .catch((err) => {
          console.log(err)
          })
    },
    updateReview: function () {
      const reviewItem = {
        'id': this.review.id,
        'title': this.review.title,
        'content': this.review.content,
        'star_rating': this.review.star_rating,
      }
      this.$router.push({ name: 'UpdateReview', params:{ movieId:this.review.movie , reviewItem:reviewItem}})
    },
    getUsername: function(userId) {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/accounts/${userId}/detail/`, config)
        .then((res) => {
          console.log("username나옴")
          console.log(res)
          this.username = res.data.username
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  mounted() {
    this.getReview()
  }
}
</script>

<style scoped>
.back {
  padding-left : 450px;
  margin-top : 8px;
  color: rgb(209, 19, 226, 0.6);
}
#heart {
  color: #ff000093;
}

#reviewDetail {
  display:inline-block;
  height: auto;
  color: rgb(33, 30, 34, 0.9);
}
#reviewDetail > div{
  padding: 10px;
  background-color:rgba(244, 223, 250, 0.2);
  width: 500px;
  border-radius: 6px;
  /* border: 3px solid rgba(103, 180, 144, 0.5); */

}
#border > div{
  border-bottom: 1px solid rgba(134, 91, 155, 0.2);

}
.submit {
  margin-top: 3px;
  margin-bottom: 3px;
  border : 1px solid rgba(255, 255, 255, 0.9);
  background-color: rgba(154, 68, 235, 0.3);
  border-radius: 4px;
  color: white;
}
.noBorderSubmit {
  background-color: rgba(154, 68, 235, 0.3);
  border-radius: 4px;
  color: white;
  font-weight: bold;
}
</style>