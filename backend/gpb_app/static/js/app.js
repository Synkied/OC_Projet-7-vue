/*import Vue from 'vue'
import App from './app.vue'

*/
const store = new Vuex.Store({
  state: {
    count: 0,
  },
/*  actions: {
    test: function () {
      axios.get('https://jsonplaceholder.typicode.com/posts/1').then((response => {
        console.log(response)
      })
    }
  }*/
})

/* Messages to display for every case of json response */
var messages = {
      ok: 'Écoute mon petit, voici ce que je sais sur cet endroit et ses environs :',
      geoloc_only: 'Je ne me souviens pas d\'anecdote sur cet endroit, mais je me souviens où il se trouve (ou peut-être pas...)',
      nothing_found: 'Hum... il ne me semble pas connaître cet endroit, aurais-tu plus de détails à me fournir (une ville, un code postale) ?',
      no_response: 'Ma mémoire flanche, laisse moi me reposer un peu et reviens me voir plus tard !',
}

var vm = new Vue({
  el: '#vue_app',
  delimiters: ["[[", "]]"], /* define new delimiters to avoid conflict with Jinja2 */
    data: {
      title: 'Grandpy bot',
      user_language: '',
      user_query: '',
      gmaps_iframe: '',
      wikimedia_txt: '',
      wiki_url: '',
      status: '',
      messages: messages
    },
    methods: {
      sayHello: function(){
        this.title = 'Hello!';
        return this.title;
      },
      getBrowserLanguage: function () {
        this.user_language = navigator.language || navigator.userLanguage;
        alert(this.user_language);
      },
      lookupGmapsWikiAPI: function () {
        var this_vm = this
        axios.get('/question/' + encodeURI(this.user_query))
          .then(function(response){
            console.log(response.data); // ex.: { user: 'Your User'}
            this_vm.gmaps_iframe = response.data.iframe_map;
            this_vm.wikimedia_txt = response.data.extract;
            this_vm.wiki_url = response.data.url;
            this_vm.status = response.data.status;
          })
          .catch(function (error) {
            return
          });
      },
    },
  });

