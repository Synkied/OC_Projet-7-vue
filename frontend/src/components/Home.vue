<template>
  <div class="container">
    <gmaps-wiki></gmaps-wiki>
    <p>Random number from backend: {{ randomNumber }}</p>
    <button @click="getRandom">New random number</button>
  </div>
</template>

<script>
import axios from 'axios'
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
      const path = '/api/random'
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
    'gmaps-wiki': GmapsWiki
  }
}
</script>
