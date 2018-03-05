// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'

/* boostrap's css import, needed for bootstrap to work */
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

/* Importing the favicons.js file to load favicons in the webpack build */
import '../favicons/favicons'

Vue.config.productionTip = false
Vue.use(BootstrapVue)

/* eslint-disable no-new */
new Vue({
  el: '#app',
  render: h => h(App),
  router,
  components: {
    App,
    BootstrapVue
  }
}).$mount('#app')
/* Mounts the scripts to the #app div in ../app.html */
