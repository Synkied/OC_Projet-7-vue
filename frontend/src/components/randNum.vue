<!-- Random number from backend component -->
<!--  Quentin Lathiere - synkx@hotmail.fr -->

<template>
  <div class="gen_number">
    <h4>{{ messages.title }}</h4>
    <p>{{ messages.subtitle }} {{ randomNumber }}</p>
    <button class="btn" @click="getRandom">{{ messages.button }}</button>
    <p> {{ test }}</p>
    <button @click="changeTxt">change</button>
    <button @click="resetTxt">reset</button>
  </div>
</template>

<script>
import axios from 'axios'

var rdmNumsMsgsFr = {
  title: 'EN BONUS',
  subtitle: 'Générateur de nombres aléatoires :',
  button: 'Nouveau nombre aléatoire'
}

export default {
  props: {
    test: String
  },
  data () {
    return {
      randomNumber: 0,
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
    },
    changeTxt () {
      this.test = 'youhou'
    },
    resetTxt () {
      this.test = 'test'
      this.$emit('testWasChanged', this.test)
    }
  },
  created () {
    this.getRandom()
  }
}
</script>

<style scoped>
  .gen_number {
    text-align: center;
    color: #fff;
  }

</style>
