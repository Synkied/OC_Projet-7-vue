<!-- Home component (container) -->
<!--  Quentin Lathiere - synkx@hotmail.fr -->

<template>
  <div class="container">
    <gmaps-wiki></gmaps-wiki>
    <hr class="mt-5">
    <rand-num></rand-num>
  </div>
</template>

<script>
import GmapsWiki from './GmapsWiki'
import RandNum from './randNum'

export default {
  data () {
    return {
      /* datas */
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

  hr {
    border-top: 2px solid rgba(255, 255, 255, 0.3);
  }
</style>
