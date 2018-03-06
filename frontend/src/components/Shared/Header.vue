<!-- Header file, used to define the navbar -->
<!--  Quentin Lathiere - synkx@hotmail.fr -->

<template>
  <nav class="navbar navbar-expand-md">
    <a class="navbar-brand text-center center-block" href="/">
        <img src="../../assets/logo.png" height="80" width="80" alt="">
        <p class="logo_txt">Grandpy</p>
        <p class="logo_txt">Bot</p>
    </a>
<!--     <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
</button> -->
    <div class="collapse navbar-collapse" id="navbarCollapse"></div>
  </nav>
</template>

<script>
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Noto+Sans');

  .navbar {
    color: #fff;
  }

  nav a, nav a:hover, nav a:active{
    color: #fff;
  }

  .logo_txt {
    font-family: 'Noto Sans', sans-serif;
    font-weight: bold;
    text-transform: uppercase;
    margin-bottom: -10px;
    text-align: right;
  }

</style>
