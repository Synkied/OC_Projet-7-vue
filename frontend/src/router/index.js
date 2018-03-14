import Vue from 'vue'
import Router from 'vue-router'

const routerOptions = [
  /* what to render depending on the url passed */
  { path: '/', component: 'Home' },
  { path: '*', component: 'NotFound' }
]

const routes = routerOptions.map(route => {
  return {
    ...route,
    component: () => import(`@/components/${route.component}.vue`)
    /* searches for the component to render depending on the url passed */
    /* here, our site is a SPA, so every argument passed to the url will render NotFound */
  }
})

Vue.use(Router)

export default new Router({
  routes,
  mode: 'history'
})
