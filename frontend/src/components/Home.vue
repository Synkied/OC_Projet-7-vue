<template>
  <div class="container">
    <img src="../assets/logo.png">
    <p>Home page</p>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
    <rise-loader></rise-loader>
    <gmaps-wiki></gmaps-wiki>
  </div>
</template>

<script>
import axios from 'axios'
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
import GmapsWiki from './GmapsWiki'

export default {
  data () {
    return {
      randomNumber: 0,
      title: 'Grandpy bot'
    }
  },
  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom () {
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend () {
      const path = 'http://localhost:5000/api/random'
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getRandom()
  },
  components: {
    'rise-loader': RiseLoader,
    'gmaps-wiki': GmapsWiki
  }
}
</script>
