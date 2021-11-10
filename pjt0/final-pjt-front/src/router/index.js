import Vue from 'vue'
import VueRouter from 'vue-router'
import Login from '@/views/accounts/Login'
import Signup from '@/views/accounts/Signup'
import Index from '@/views/Index'
import Home from '@/views/Home'
import Profile from '@/views/Profile'
import MovieDetail from '@/components/Movie/MovieDetail'
import ReviewDetail from '@/components/Review/ReviewDetail'
import CreateReview from '@/components/Review/CreateReview'
import UpdateReview from '@/components/Review/UpdateReview'
import CreateCollection from '@/views/CreateCollection'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index,
  },
  {
    path: '/Home/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/accounts/login/',
    name: 'Login',
    component: Login,
  },
  {
    path: '/accounts/signup/',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/:user_id/detail/',
    name: 'Profile',
    component: Profile,
    props: true,
  },
  {
    path: '/movies/:movieId/detail/',
    name: 'MovieDetail',
    component: MovieDetail,
  },
  {
    path: '/review/:reviewId/detail/',
    name: 'ReviewDetail',
    component: ReviewDetail,
  },
  {
    path: '/community/:movieId/review/create/',
    name: 'CreateReview',
    component: CreateReview,
  },
  {
    path: '/collection/create/',
    name: 'CreateCollection',
    component: CreateCollection,
  },
  {
    path: '/collection/update/',
    name: 'UpdateCollection',
    component: CreateCollection,
    props: true,
  },
  {
    path: '/community/:movieId/review/update/',
    name: 'UpdateReview',
    component: UpdateReview,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
