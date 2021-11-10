<template>
  <li class="d-flex justify-content-between mx-1">
    <div>{{ username }} : </div>
    <div v-if="update"><p class="m-1">{{ comment.content }}</p></div>
    <div v-if="update" class="d-flex">
      <div class="d-flex">
      <div v-if="requestUsername == username">
      <button class="submit" @click="deleteComment(comment,idx)">Delete</button>
      </div>
      <div v-if="requestUsername == username">
      <button class="submit" @click="updateComment">Update</button>
    </div>
    </div>
    </div>
    <div v-if="update == false" >
      <input class="commentInput" type="text" v-model.trim="comment.content">
    </div>
    <div v-if="update == false">
      <button class="submit" @click="updateComplete(comment)">Update완료</button>
    </div>
  </li>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name:'CommentListItem',
  props: {
    comment: {
      type: [Array, Object],
    },
    idx: Number,
    review: {
      type: [Array, Object]
    }
  },
  data: function () {
    return {
      username: '',
      update: true,
      requestUsername: localStorage.getItem('myname'),
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
    deleteComment: function (comment,idx) {
      const config = this.setToken()
      const newComments = this.review.comment_set
      const commentIdx = idx
      axios.delete(`${SERVER_URL}/community/comment/${comment.id}/`,config)
      .then((res) => {
          console.log(res)
          newComments.splice(commentIdx,1)
          })
          .catch((err) => {
          console.log(err)
          })
         this.comments = newComments

    },
    updateComment: function () {
      this.update = false
    },
    updateComplete: function (comment) {
      const config = this.setToken()
      const commentItem = {
        'content': this.comment.content,
      }
      axios.put(`${SERVER_URL}/community/comment/${comment.id}/`,commentItem, config)
      .then((res) => {
          console.log(res)
          this.update = true
          })
          .catch((err) => {
          console.log(err)
          })
    },
    getUsername: function() {
      const config = this.setToken()
      axios.get(`${SERVER_URL}/accounts/${this.comment.user}/detail/`, config)
        .then((res) => {
          console.log("commentusername나옴")
          console.log(res.data)
          this.username = res.data.username
          console.log(localStorage.getItem('myname'))
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  mounted() {
    this.getUsername()
  }
}
</script>

<style scoped>
.commentInput {
  width: 100%;
  /* display: block; */
  margin: 0px auto;
  background-color: white;
  border-bottom: rgb(152, 12, 233) 1px solid;
  border-left: medium none;
  border-right: medium none;
  border-top: medium none;
  outline: none;
}

input::placeholder {
  color: rgb(100, 99, 99);
}
.submit {
  margin-top: 3px;
  margin-bottom: 3px;
  border : 1px solid rgba(255, 255, 255, 0.9);
  background-color: rgba(154, 68, 235, 0.3);
  border-radius: 4px;
  color: white;
  font-weight: bold;
}
</style>