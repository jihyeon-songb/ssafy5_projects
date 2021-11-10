<template>
  <div class="top">
    <div class="title"><UserInfo :username="username"/>님의 profile</div>
    <div class="follow">
      <div class="nums">
      <div class="follower">
        {{ followers.length }}
      </div>
      <div class="following">
        {{ followings.length }}
        </div>
      </div>
     팔로워  팔로잉 
    <Follow :isFollow="isFollow" :isSamePerson="isSamePerson" @follow="follow" @unfollow="unfollow"/>
    </div>
    <div class="changeBtn">
      <button v-if="now === true" @click="changeMode" class="snip1535">Review</button>
      <button v-else @click="changeMode" class="snip1535">Collection</button>
    </div>
    <hr>
      <div v-if="now === true" class='collection' >
          <div class="title">컬렉션</div>
            <CollectionNew :isSamePerson="isSamePerson"/>
          <CollectionList :collections="collections" />
      </div>
    <div v-else class="review">
        <div class="title">리뷰 목록</div>
          <UserReviewList :reviews="reviews"/>
    </div>
    </div>
</template>

<script>
import axios from 'axios'
import CollectionList from '@/components/Profile/CollectionList.vue'
import UserInfo from '@/components/Profile/UserInfo.vue'
import UserReviewList from '@/components/Profile/UserReviewList.vue'
import Follow from '@/components/Profile/Follow.vue'
import CollectionNew from '@/components/Profile/CollectionNew.vue'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Profile',
  components: {
    CollectionList,
    UserInfo,
    UserReviewList,
    Follow,
    CollectionNew,
  },
  data: function() {
    return {
      collections : [],
      reviews: [],
      username: '',
      followers: [],
      followings: [],
      myName:'',
      isFollow: false,
      isSamePerson: false,
      now: true,
    }
  },
  created: function () {
      const user_id = this.$route.params.user_id
      const token = localStorage.getItem('jwt')
      this.myName = localStorage.getItem('myname')
      const config = {
        headers: {
          Authorization: `JWT ${token}`
        }
      }

      axios.get(`${SERVER_URL}/movies/collection_list/${user_id}/`)
      .then((res) => {
        this.collections = res.data
      })
      .catch((err) => {
        console.log(err)
      })
      
      axios.get(`${SERVER_URL}/accounts/${user_id}/detail/`, config)
      .then((res) => {
        const myId = Number(localStorage.getItem('myId'))
        this.username = res.data.username
        this.followers = res.data.followers
        this.followings = res.data.followings
        this.followingCount = res.data.followingCount
        this.followerCount = res.data.followerCount
        console.log(this.followers, myId)
        if (this.followers.includes(myId)) {
          this.isFollow = true
        }
        if (this.myName === this.username) {
          this.isSamePerson = true
        }
      })
      .catch((err) => {
        console.log(err)
      })

      axios.get(`${SERVER_URL}/community/${user_id}/reviews/`, config)
      .then((res) => {
        this.reviews = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    },
    methods: {
      follow: function() {
        const user_id = this.$route.params.user_id
        const token = localStorage.getItem('jwt')
        axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${user_id}/detail/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.isFollow = true
        this.followers.push(this.myName)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    unfollow: function() {
      const user_id = this.$route.params.user_id
      const token = localStorage.getItem('jwt')
      axios({
        method: 'post',
        url: `${SERVER_URL}/accounts/${user_id}/detail/`,
        headers: {
          Authorization: `JWT ${token}`
        }
      })
      .then((res) => {
        console.log(res)
        this.isFollow = false
        let idx = this.followers.indexOf(this.myName)
        this.followers.splice(idx, 1)
      })
      .catch((err) => {
        console.log(err)
      })
    },
    changeMode: function () {
      if (this.now === true) {
        this.now = false
      } else {
        this.now = true
      }
      
    }
    }
  }
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@900&display=swap');

.top {
   margin-top: 20px;
  }

.title {
    font-weight: 10;
    font-size: 20px;
    color: black;
    font-family: 'Roboto', sans-serif;
}

.collections {
    margin: 30px;
  }

.changeBtn {
  margin-top: 15px;
  margin-left: 10px;
}

.follow {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
  margin-right: 50px;
}

.follower {
  margin-right: 39px;
}

.following {
  margin-right: 21px;
}

.nums {
  display: flex;
}

@import url(https://fonts.googleapis.com/css?family=BenchNine:700);
.snip1535 {
  background-color: #4ca1a3;
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
  border-color: #4ca1a3;
  border-right-width: 2px;
  border-top-width: 2px;
  right: -5px;
  top: -5px;
}
.snip1535:after {
  border-bottom-width: 2px;
  border-color: #4ca1a3;
  border-left-width: 2px;
  bottom: -5px;
  left: -5px;
}
.snip1535:hover,
.snip1535.hover {
  background-color: #4ca1a3;
}
.snip1535:hover:before,
.snip1535.hover:before,
.snip1535:hover:after,
.snip1535.hover:after {
  height: 100%;
  width: 100%;
}
</style>