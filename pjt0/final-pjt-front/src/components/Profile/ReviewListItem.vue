<template>
  <div class="top">
    <li class="list-group-item list-group-item-action d-flex justify-content-around align-items-center">
      <div>
        {{ review.movie.title }}
      </div>
      <div>
        {{ review.star_rating }}
      </div>
      <div>
        {{ review.title }}
      </div>
      <div>
        {{ review.content }}
      </div>
    </li>
  </div>
</template>

<script>

export default {
  name: 'ReviewListItem',
  props: {
    review: Object,
  }
}
</script>

<style scoped>
.top {
  margin-top: 20px;
}
</style>