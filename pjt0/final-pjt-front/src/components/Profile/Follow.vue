<template>
  <div v-if="isSamePerson === false">
    <div v-if="isFollow === false">
      <button @click="follow" class="snip1535">
        FOLLOW
      </button>
    </div>
    <div v-else>
      <button @click="unfollow" class="snip1535">
        UNFOLLOW
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Follow',
  props: {
    isFollow: Boolean,
    isSamePerson: Boolean,
  },
  methods: {
    follow: function() {
      this.$emit('follow')
    },
    unfollow: function() {
      this.$emit('unfollow')
    }
  }
}
</script>

<style scoped>
@import url(https://fonts.googleapis.com/css?family=BenchNine:700);
.snip1535 {
  background-color: #4ca1a3;
  border: none;
  color: #ffffff;
  cursor: pointer;
  display: inline-block;
  font-family: 'BenchNine', Arial, sans-serif;
  font-size: 1em;
  font-size: 15px;
  line-height: 1em;
  margin: 15px 10px;
  outline: none;
  padding: 12px 20px 10px;
  position: relative;
  text-transform: uppercase;
  font-weight: 500;
}
.snip1535:before,
.snip1535:after {
  border-color: transparent;
  -webkit-transition: all 0.25s;
  transition: all 0.25s;
  border-style: solid;
  border-width: 0;
  content: "";
  height: 12px;
  position: absolute;
  width: 12px;
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