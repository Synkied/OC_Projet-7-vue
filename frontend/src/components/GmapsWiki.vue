<!-- Displays Google Maps and Wikimedia API responses -->
<!--  Quentin Lathiere - synkx@hotmail.fr -->

<!-- Templates -->
<template>
  <div>
  <h1 class="mb-3 mt-5"> {{ messages.bienvenue }}</h1>
  <h2 class="mb-5">{{ messages.sousTitre }}</h2>
    <div class="text-center">

      <fieldset>
          <input :class="{'bounce animated': animated}" @animationend="animated = false"
            @keyup.esc="user_query=''" @keyup.enter="[lookupGmapsWikiAPI(), animate()]"
            v-model="user_query" name="user_query" type="text" class="form-control" placeholder="Entrer une adresse">
        <button @click="[lookupGmapsWikiAPI(), animate()]" class="btn mt-5 mb-5 query_btn">Envoyer</button>
      </fieldset>

      <rise-loader :loading="loading"></rise-loader>

      <!-- Map and wikimedia text display -->
      <template v-if="status === 'OK'">
          <div class="card">
              <div class="card-img-top" v-html="gmaps_iframe"></div>
              <div class="card-block"></div>
                  <p class="mt-4"><strong>{{ messages.ok }}</strong></p>
                  <p v-html="wikimedia_txt" class="mt-1 card-text text-center"></p>
              <a v-if="wiki_url.length > 0" :href="wiki_url" target="_blank" class="btn btn-primary">En savoir plus</a>
          </div>
      </template>
      <template v-else-if="status.length == 0">
        <p></p>
      </template>
      <template v-else-if="status === 'GEOLOC_ONLY'">
              <div class="card">
              <div class="card-block"></div>
                  <p class="mt-1 card-text text-center"><strong>{{ messages.geoloc_only }}</strong></p>
                  <div class="card-img-bottom" v-html="gmaps_iframe"></div>
          </div>
      </template>
      <template v-else-if="status === 'NOTHING_FOUND'">
          <p><strong>{{ messages.nothing_found }}</strong></p>
      </template>
      <template v-else-if="status === 'NO_QUERY'">
          <p class="white-txt"><strong>{{ messages.no_query }}</strong></p>
      </template>
      <template v-else>
          <p><strong>{{ messages.no_response }}</strong></p>
      </template>
    </div>
  </div>
</template>

<!-- Scripts -->
<script>
/* Imports */
import axios from 'axios'
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'
import { loadProgressBar } from 'axios-progress-bar'
import 'axios-progress-bar/dist/nprogress.css'

/* vars declarations */
var messagesFr = {
  bienvenue: 'Bienvenue jeune personne',
  sousTitre: 'Donne moi une adresse, et je te raconterai des anecdotes !',
  ok: 'Écoute mon petit, voici ce que je sais sur cet endroit et ses environs :',
  geoloc_only: 'Je ne me souviens pas d\'anecdote sur cet endroit, mais je me souviens où il se trouve (ou peut-être pas...)',
  nothing_found: 'Hum... il ne me semble pas connaître cet endroit, aurais-tu plus de détails à me fournir (une ville, un code postale) ?',
  no_response: 'Ma mémoire flanche, laisse moi me reposer un peu et reviens me voir plus tard !',
  no_query: 'Si tu ne me demandes rien, je ne peux pas y réfléchir !'
}

/* data, methods, components... declaration */
export default {
  data () {
    return {
      randomNumber: 0,
      title: 'Grandpy bot',
      user_language: '',
      user_query: '',
      gmaps_iframe: '',
      wikimedia_txt: '',
      wiki_url: '',
      status: '',
      messages: messagesFr,
      loading: false,
      animated: false
    }
  },
  methods: {
    lookupGmapsWikiAPI () {
      var thisVm = this
      /* axios to ajax the query */
      if (thisVm.user_query) {
        const path = '/question/' + encodeURI(thisVm.user_query)
        loadProgressBar()
        axios.get(path).then(response => {
          if (response.data) {
            console.log(response.data) // ex.: { user: 'Your User'}
            thisVm.gmaps_iframe = response.data.iframe_map
            thisVm.wikimedia_txt = response.data.extract
            thisVm.wiki_url = response.data.url
            thisVm.status = response.data.status
          }
        })
          .catch(function (error) {
            console.log(error)
          })
      } else {
        thisVm.status = 'NO_QUERY'
      }
    },
    animate () {
      var thisVm = this
      thisVm.animated = true
    }
  },
  components: {
    'rise-loader': RiseLoader
  }
}
</script>

<!-- scoped styles for this component -->
<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Oxygen');
  @import url('https://fonts.googleapis.com/css?family=Raleway');

  .white-txt {
    color: #fff;
  }

  h1{
    text-align: center;
    font-family: 'Oxygen', sans-serif;
    font-weight: bold;
    font-size: 6vh;
    text-transform: uppercase;
    color: #fff;
  }

  h2{
    text-align: center;
    font-size: 3vh;
    color: #fff;
  }

  .query_btn{
    background-color: #2B7A78;
    color: #fff;
    font-family: 'Raleway', sans-serif;
    font-weight: bold;
  }

  .query_btn:hover{
    background-color: #55c3c0;
  }

  .card {
    color: #000;
    text-align: center;
  }

/*   .jumbotron{
  background-color: #DEF2F1;
  border-radius: 20px;
  -webkit-box-shadow: 0 2px 4px 0 rgba(0,0,0,.3);
  box-shadow: 0 2px 4px 0 rgba(0,0,0,.3);
} */

  .card-text {
    padding: 0 30px;
    text-align: justify;
  }

  .animated {
    -webkit-animation-duration: 1s;
    animation-duration: 1s;
    -webkit-animation-fill-mode: both;
    animation-fill-mode: both;
  }

  .animated.infinite {
    -webkit-animation-iteration-count: infinite;
    animation-iteration-count: infinite;
  }

  .animated.hinge {
    -webkit-animation-duration: 2s;
    animation-duration: 2s;
  }

  .animated.flipOutX,
  .animated.flipOutY,
  .animated.bounceIn,
  .animated.bounceOut {
    -webkit-animation-duration: .75s;
    animation-duration: .75s;
  }

  @-webkit-keyframes bounce {
    from, 20%, 53%, 80%, to {
      -webkit-animation-timing-function: cubic-bezier(0.215, 0.610, 0.355, 1.000);
      animation-timing-function: cubic-bezier(0.215, 0.610, 0.355, 1.000);
      -webkit-transform: translate3d(0,0,0);
      transform: translate3d(0,0,0);
    }

    40%, 43% {
      -webkit-animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
      animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
      -webkit-transform: translate3d(0, -30px, 0);
      transform: translate3d(0, -30px, 0);
    }

    70% {
      -webkit-animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
      animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
      -webkit-transform: translate3d(0, -15px, 0);
      transform: translate3d(0, -15px, 0);
    }

    90% {
      -webkit-transform: translate3d(0,-4px,0);
      transform: translate3d(0,-4px,0);
    }
  }

  @keyframes bounce {
    from, 20%, 53%, 80%, to {
      -webkit-animation-timing-function: cubic-bezier(0.215, 0.610, 0.355, 1.000);
      animation-timing-function: cubic-bezier(0.215, 0.610, 0.355, 1.000);
      -webkit-transform: translate3d(0,0,0);
      transform: translate3d(0,0,0);
    }

    40%, 43% {
      -webkit-animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
      animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
      -webkit-transform: translate3d(0, -30px, 0);
      transform: translate3d(0, -30px, 0);
    }

    70% {
      -webkit-animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
      animation-timing-function: cubic-bezier(0.755, 0.050, 0.855, 0.060);
      -webkit-transform: translate3d(0, -15px, 0);
      transform: translate3d(0, -15px, 0);
    }

    90% {
      -webkit-transform: translate3d(0,-4px,0);
      transform: translate3d(0,-4px,0);
    }
  }

  .bounce {
    -webkit-animation-name: bounce;
    animation-name: bounce;
    -webkit-transform-origin: center bottom;
    transform-origin: center bottom;
  }
</style>
