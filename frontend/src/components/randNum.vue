<!-- Random number from backend component -->
<!--  Quentin Lathiere - synkx@hotmail.fr -->

<template>
  <div class="gen_number">
    <h4>{{ messages.title }}</h4>
    <p>{{ messages.subtitle }}</p>
    <transition-group name="list-complete" tag="p">
      <span
        v-for="item in items"
        v-bind:key="item"
        class="list-complete-item">
          {{ item }}
      </span>
    </transition-group>
    <button class="btn btn-add" @click="getRandomInt(0, 1000)">{{ messages.addTxt }}</button>
    <button class="btn btn-remove" @click="remove">{{ messages.removeTxt }}</button>
  </div>
</template>

<script>

var rdmNumsMsgsFr = {
  title: 'EN BONUS',
  subtitle: 'Générateur de nombres :',
  button: 'Nouveau nombre aléatoire',
  addTxt: 'Ajouter',
  shuffleTxt: 'Mélanger',
  removeTxt: 'Enlever'
}

export default {
  props: {
    test: String
  },
  data () {
    return {
      messages: rdmNumsMsgsFr,
      items: [],
      nextNum: 1
    }
  },
  methods: {
    getRandomInt (min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      var randInt = Math.floor(Math.random() * (max - min + 1)) + min
      if (!this.items.includes(randInt)) {
        this.items.splice(this.randomIndex(), 0, randInt)
      }
    },
    randomIndex: function () {
      return Math.floor(Math.random() * this.items.length)
    },
    /* add: function () {
      this.items.splice(this.randomIndex(), 0, this.nextNum++)
    }, */
    remove: function () {
      this.items.splice(this.randomIndex(), 1)
    }
  }
}
</script>

<style scoped>
  .gen_number {
    text-align: center;
    color: #fff;
    margin: 70px 0 0 0;
  }

  .btn-add:hover {
    background-color: #fff;
    color: #000;
  }

  .btn-remove:hover {
    background-color: #000;
    color: #fff;
  }

  .list-complete-item {
    transition: all 1s;
    display: inline-block;
    margin-right: 10px;
  }
  .list-complete-enter, .list-complete-leave-to
  /* .list-complete-leave-active below version 2.1.8 */ {
    opacity: 0;
    transform: translateY(30px);
  }
  .list-complete-leave-active {
    position: absolute;
  }

</style>
