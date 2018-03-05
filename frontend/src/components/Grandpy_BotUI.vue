<template>
    <div id="my-botui-app"><bot-ui></bot-ui></div>
</template>

<script>
import Vue from 'vue'
import BotUI from 'botui'

export default {
  components: {
    BotUI
  // added this because without it, vue doesn't recognize the bot-ui element
  },
  mounted () {
    var botui = new BotUI('my-botui-app', {
      vue: Vue
    })

    botui.message.add({
      content: 'Hello World from bot!'
    })

    botui.message.add({
      human: true,
      content: 'Hello World from human!'
    })
  }

}

</script>

<style>

</style>
