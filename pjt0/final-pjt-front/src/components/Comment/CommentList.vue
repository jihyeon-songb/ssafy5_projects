<template>
  <div id="commentList" v-if="message">
    <div class="p-2">
    <CommentListItem v-for="(comment, idx) in this.review.comment_set" v-bind:key="idx" :idx="idx" :comment="comment" :review="review"/>
    </div>
    <div class="mt-1">
      <label for="content"></label>
      <input class="commentInput" type="text" placeholder="댓글을 입력하시오" id="content" v-model.trim="comment.content" @keypress.enter="createComment">
      <button class="submit" @click="createComment" >작성</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
// import _ from 'lodash'
const SERVER_URL = process.env.VUE_APP_SERVER_URL
import CommentListItem from '@/components/Comment/CommentListItem'

export default {
  name: 'CommentList',
  components: {
    CommentListItem,
  },
  props: {
    review: {
      type: [Array, Object],
    },
    message: Boolean,
  },
  data: function () {
    return {
      update: true,
      comments: this.review.comment_set,
      comment: {
        content: '',
      }
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
    createComment: function() {
      const config = this.setToken()
      const commentItem = {
        content: this.comment.content,
      }
      const newComments = this.review.comment_set
      // console.log(this.comment.content)
      axios.post(`${SERVER_URL}/community/review/${this.review.id}/comment/`,commentItem, config)
      .then((res) => {
        console.log(res.data)
        newComments.push(res.data)
        })
        .catch((err) => {
         console.log(err)
         })
         this.comments = newComments
    },
  },
}
</script>

<style scoped>
.commentInput {
  width: 90%;
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
/* #commentList {
  display:inline-block;
} */
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