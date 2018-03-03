<!-- Displays Google Maps and Wikimedia API responses -->

<template>
  <div>
  <h1 class="mb-5 mt-5">Bienvenue jeune personne !</h1>
    <div class="jumbotron text-center">
    <!--   <img src="../assets/landscape.jpeg" width="100%" alt="Un paysage magnifique de montagne et rivière"> -->
    <!--         <button @click="{{ getBrowserLanguage() }}" class="btn btn-primary mb-4">get browser language</button> -->

      <fieldset>
      <input @keyup.enter="lookupGmapsWikiAPI" v-model="user_query" name="user_query" type="text" class="form-control" placeholder="Entrez une adresse">
      <button @click="lookupGmapsWikiAPI" class="btn mt-5 mb-5">Envoyer</button>
      </fieldset>

      <rise-loader :loading="loading"></rise-loader>

      <!-- Map and wikimedia text display -->
      <template v-if="status === 'OK'">
          <div class="card">
              <div class="card-img-top" v-html="gmaps_iframe"></div>
              <div class="card-block"></div>
                  <p class="mt-4"><strong>{{ messages.ok }}</strong></p>
                  <p v-html="wikimedia_txt" class="mt-1 card-text"></p>
              <a v-if="wiki_url.length > 0" :href="wiki_url" target="_blank" class="btn btn-primary">En savoir plus</a>
          </div>
      </template>
      <template v-else-if="status.length == 0">
        <p></p>
      </template>
      <template v-else-if="status === 'GEOLOC_ONLY'">
              <div class="card">
              <div class="card-block"></div>
                  <p class="mt-1 card-text"><strong>{{ messages.geoloc_only }}</strong></p>
                  <div class="card-img-bottom" v-html="gmaps_iframe"></div>
          </div>
      </template>
      <template v-else-if="status === 'NOTHING_FOUND'">
          <p><strong>{{ messages.nothing_found }}</strong></p>
      </template>
      <template v-else>
          <p><strong>{{ messages.no_response }}</strong></p>
      </template>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import RiseLoader from 'vue-spinner/src/RiseLoader.vue'

var messages = {
  ok: 'Écoute mon petit, voici ce que je sais sur cet endroit et ses environs :',
  geoloc_only: 'Je ne me souviens pas d\'anecdote sur cet endroit, mais je me souviens où il se trouve (ou peut-être pas...)',
  nothing_found: 'Hum... il ne me semble pas connaître cet endroit, aurais-tu plus de détails à me fournir (une ville, un code postale) ?',
  no_response: 'Ma mémoire flanche, laisse moi me reposer un peu et reviens me voir plus tard !'
}

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
      messages: messages,
      loading: false
    }
  },
  methods: {
    lookupGmapsWikiAPI: function () {
      var thisVm = this
      const path = '/question/' + encodeURI(thisVm.user_query)
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
    }
  },
  components: {
    'rise-loader': RiseLoader
  }
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Ubuntu');

  h1{
    text-align: center;
    font-family: 'Ubuntu', sans-serif !important;
    font-size: 4.5rem !important;

  }
</style>
