<!-- Defines all root elements (header, router-view, footer...) -->

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
  color: #2c3e50;
  margin-top: 60px;
}
body{
  background-color: #99d3df;
}
</style>
