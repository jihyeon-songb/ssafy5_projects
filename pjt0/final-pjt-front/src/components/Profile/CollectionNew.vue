<template>
  <div>
    <div v-if="isSamePerson === true" class="newCollection">
      <button @click="COLLECTION_RESET(); CreateNewCollection();" class="snip1535">
          New
      </button>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'

export default {
  name: 'CollectionNew',
  props: {
    isSamePerson: Boolean,
  },
  methods: {
    CreateNewCollection: function () {
      this.$router.push({ name: 'CreateCollection' })
    },
    ...mapMutations([
      'COLLECTION_RESET',
    ])
  }
}
</script>

<style scpoped>
.newCollection {
  margin-top: 20px;
  margin-bottom: 10px;
  float: right;
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