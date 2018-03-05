<template>
  <div class="container">
    <gmaps-wiki></gmaps-wiki>
    <div class="gen_number">
      <h4>{{ messages.title }}</h4>
      <p>{{ messages.subtitle }} {{ randomNumber }}</p>
      <button class="btn" @click="getRandom">{{ messages.button }}</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import GmapsWiki from './GmapsWiki'

var rdmNumsMsgsFr = {
  title: 'EN BONUS',
  subtitle: 'Générateur de nombres aléatoires :',
  button: 'Nouveau nombre aléatoire'
}

export default {
  data () {
    return {
      randomNumber: 0,
      title: 'Grandpy bot',
      messages: rdmNumsMsgsFr
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

<style scoped>
  .container {
    max-width: 960px;
  }

  .gen_number {
    text-align: center;
  }

</style>
