<!-- Home component (container) -->
<!--  Quentin Lathiere - synkx@hotmail.fr -->

<template>
  <div class="container">
    <gmaps-wiki></gmaps-wiki>
    <rand-num :test="test" @testWasReset="test = $event"></rand-num>
  </div>
</template>

<script>
import GmapsWiki from './GmapsWiki'
import RandNum from './randNum'

export default {
  data () {
    return {
      test: 'txt'
    }
  },
  components: {
    'gmaps-wiki': GmapsWiki,
    'rand-num': RandNum
  }
}
</script>

<style scoped>
  .container {
    max-width: 960px;
  }
</style>
