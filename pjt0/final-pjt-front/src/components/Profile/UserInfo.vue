<template>
  <div style="display: inline;">
    {{ username }}
  </div>
</template>

<script>
export default {
  name: 'UserInfo',
  props: {
    username: String,
  },
}
</script>

<style>

</style>