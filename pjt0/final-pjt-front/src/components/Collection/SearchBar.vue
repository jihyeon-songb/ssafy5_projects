<template>
  <div>
    <input class="" @keyup="onInputKeyword" type="text" placeholder="컬렉션에 추가할 영화를 검색해보세요.">
  </div>
</template>

<script>

export default {
  name: 'SearchBar',
  data: function () {
    return {
    }
  },
  methods: {
    onInputKeyword: function (event) {
      this.$emit('input-search', event.target.value)
    }
  }
}
</script>

<style scoped>
input {
  width: 350px;
  display: block;
  margin: 0 auto;
  border-bottom: teal 1.5px solid;
  border-left: medium none;
  border-right: medium none;
  border-top: medium none;
  outline: none;
  background: url("../../assets/loupe.png") no-repeat scroll 7px 7px !important;
  padding-left:30px !important;
}
input::placeholder {
  color: black;
}
div {
  padding-top: 10px;
  padding-bottom: 10px;
}
</style>