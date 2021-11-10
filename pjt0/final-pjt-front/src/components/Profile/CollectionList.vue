<template>
  <div class="top">
      <div class="list-group">
      <CollectionListItem v-for="(collection, idx) in collections" :key="idx" :collection="collection" />
    </div>
  </div>
</template>

<script>

import CollectionListItem from '@/components/Profile/CollectionListItem.vue'

export default {
  name: 'CollectionList',
  props: {
    collections: Array,
  },
  components: {
    CollectionListItem,
  },
  data: function() {
    return {
    }
  },
  methods: {
  },
}
</script>

<style>
.list-group {
  margin-top: 40px;
  margin-left: 10px;
}
</style>