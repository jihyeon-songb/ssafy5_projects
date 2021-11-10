<template>
<div>
  <div v-if="flag">
    <Trailer :flag="flag"/>
  </div>
  <div class="card">
  <!-- <div class="card__inner">
    <header class="card__header">
    </header> -->
    
    <main class="card__body d-flex flex-column">
        <div class="d-flex justify-content-between">
          <div class="card__image">
            <img class="" :src="movieImage" alt="movie_image"> 
          </div>
          <div class="card__info">
            <h1 class="card__title">{{ movieDetail.title }}</h1>
        
            <p class="card__slug">{{ overview }}</p>
 
              <div>
              <div v-if="flag">
              <button class="card__btn" value="Watch trailer" @click="closeTrailer">Stop Watch</button>
              </div>
              <div v-else>
              <button class="card__btn" value="Watch trailer" @click="goTrailer">Watch trailer</button>
              </div>
            </div>
            <div class="mt-2">
              <button class="card__btn" @click="goCreateReview">CREATE REVIEW</button>
            </div>
            <div v-if="star_rating_average > 0" class="mb-1 mt-3">
              평점 : {{ star_rating_average }}
            </div>
            <div v-else  class="mb-1 mt-3">
              평점 : -
            </div>
            <div class="mb-1">개봉일 : {{ movieDetail.release_date }}</div>
            <span v-for="(genre, idx) in movieDetail.genres" :key="idx" :genre="genre">
              <span>{{ genre.name }}   </span>
            </span>
          </div>
        </div>
        <div class="text-light reviewList">
          <div>
            <MovieReviews :movieId="movieId" @reviewLength="reviewLength"/>
          </div>
        </div>
    </main>
  </div>
</div>
</template>

<script>
// import axios from 'axios'
import {mapState} from 'vuex'
import MovieReviews from '@/components/Movie/MovieReviews'
import Trailer from '@/components/Movie/Trailer'

export default {
  name: 'MovieDetail',
  components: {
    MovieReviews,
    Trailer,
  },
  data: function () {
    return {
      star_rating_average: 0,
      starRating: null,
      length: 1,
      movieId: this.$route.params.movieId,
      overview: '',
      flag: false,
      sum: 0,
    }
  },
   methods: {
    goTrailer: function() {
      this.flag = true
    },
    closeTrailer: function() {
      this.flag = false
    },
    goCreateReview: function() {
      console.log('클릭')
      this.$router.push({ name: 'CreateReview'})
    },
    ratingAverage: function() {
      console.log('길이나옴')
      console.log(this.length)
      console.log(this.$route.params.starRating)
      this.star_rating_average = (this.sum / this.length).toFixed(2)
      // if (this.$route.params.starRating) {
      // }
    },
    reviewLength: function(length, sum) {
      this.length = length
      this.sum = sum
      this.ratingAverage()
    },
    overviewSplit: function () {
      if (this.movieDetail.overview.length > 125) {
        this.overview = this.movieDetail.overview.substring(0,125)+'....'
      }else {
        this.overview = this.movieDetail.overview
      }
      console.log('오버뷰')
      console.log(this.overview)
    }
  },
  computed: {
    movieImage: function () {
      return `https://image.tmdb.org/t/p/w300/${this.movieDetail.poster_path}`
    },
    ...mapState([
      'movieDetail',
    ]),
  },
  mounted() {
    this.overviewSplit()
  }
}
</script>

<style scoped>
html,
body,
.wrapper {
  width: 100%;
  height: 100%;
}

html {
  font-size: 16px;
}

body {
  font-size: 100%;
  font-family: "Roboto", Arial, Verdana, sans-serif;
  background: #eee;
}

ul {
  padding: 0;
  margin: 0;
  list-style-type: none;
}
.reviewList {
  height: 100% ;
  /* overflow: auto; */
}
.card {
  position: relative;
  margin-top: 2rem;
  margin-right: auto;
  margin-left: auto;
  overflow: auto;
  display: inline-block;
  width: 42rem;
  height: 40rem;
  background: #0a0a0a;
  background-position: -60px 42px, 0;
  background-repeat: no-repeat;
  background-size: 70% 88%;
  border-radius: 0.75rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
  -ms-overflow-style: none;
  scrollbar-width: none;
}
.card::-webkit-scrollbar {
    display: none; /* Chrome, Safari, Opera*/
}
/* .card:after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(10, 10, 10, 0.15);
} */


.list {
  display: flex;
}

.list--nav {
  justify-content: space-around;
}
.list--nav li {
  width: calc(100%/3);
  background: #111;
  transition: all 0.2s cubic-bezier(0.4, 0, 1, 1);
}
.list--nav li:focus, .list--nav li:hover {
  background: #333;
}
.list--nav li:first-of-type {
  background: #292929;
}
.list--nav a {
  display: block;
  padding-top: 0.85rem;
  padding-bottom: 0.85rem;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.125rem;
  text-align: center;
  text-transform: uppercase;
  text-decoration: none;
  color: #fff;
}

.card__body {
  position: absolute;
  display: inline-block;
  width: 100%;
  /* top: 50%; */
  /* transform: translateY(-50%); */
}

.card__info,
.card__footer {
  color: #fff;
}

.card__info {
  position: relative;
  padding-top: 2rem;
  padding-right: 1.7rem;
  float: right;
  width: 50%;
}

.card__title {
  margin-bottom: 1rem;
  font-size: 1.2rem;
  font-weight: 600;
  text-transform: uppercase;
}

.card__slug {
  margin-bottom: 1.25rem;
  color: rgba(255, 255, 255, 0.95);
}

.card__btn {
  display: inline-block;
  padding: 0.65rem 1.5rem;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.0625rem;
  text-transform: uppercase;
  color: #fff;
  background: #c62828;
  border: 0;
  border-radius: 2.1875rem;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23);
  transition: all 0.2s cubic-bezier(0.4, 0, 1, 1);
}
.card__btn:focus, .card__btn:hover {
  color: #fff;
  background: #dc5454;
  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
}

.card__rating {
  display: inline-block;
  position: relative;
  padding: 1rem;
  margin-left: 3rem;
  color: #fff;
  border-radius: 50%;
  border: 3px solid #c62828;
}
.card__rating:before {
  content: "";
  position: absolute;
  z-index: 2;
  top: -5px;
  left: 0;
  width: 50%;
  height: 20px;
  background: #000;
}

footer {
  position: absolute;
  bottom: 0;
  padding-top: 1rem;
  padding-right: 1.25rem;
  padding-bottom: 1rem;
  width: 100%;
}

.list--info {
  padding-left: 1rem;
  float: right;
  justify-content: space-between;
  width: 50%;
}
.list--info li {
  font-size: 0.85rem;
}
.list--info li:nth-of-type(n+2) {
  margin-left: 1rem;
}
</style>