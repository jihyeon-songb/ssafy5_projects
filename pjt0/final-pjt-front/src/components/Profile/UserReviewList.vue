<template>
<div>
  <ul class="list-group">
      <ReviewListItem v-for="(review, idx) in reviews" :key="idx" :review="review" />
    </ul>
</div>
</template>

<script>
import ReviewListItem from '@/components/Profile/ReviewListItem.vue'
export default {
  name: 'UserReviewList',
  props: {
    reviews: Array,
  },
  components: {
    ReviewListItem,
  }
}
</script>

<style>

</style>