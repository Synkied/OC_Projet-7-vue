<!-- Defines all root elements (header, router-view, footer...) -->
<!--  Quentin Lathiere - synkx@hotmail.fr -->

<template>
  <div>
    <app-header></app-header>
    <router-view/> <!-- https://router.vuejs.org/en/api/router-view.html -->
    <app-footer></app-footer>
  </div>
</template>

<script>
import Header from './components/Shared/Header.vue'
import Footer from './components/Shared/Footer.vue'

export default {
  name: 'App',
  components: {
    'app-header': Header,
    'app-footer': Footer
  }
}

</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
  margin-top: 60px;
}

body {
  background-image: radial-gradient(circle,rgba(58,175,169,.95) 10%,rgba(43,122,120,.95) 130%) !important;
}

</style>
