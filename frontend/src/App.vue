<template>
  <div id="vue">
    <TopNavigation></TopNavigation>
    <Sidebar></Sidebar>
    <div class="content">
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
  import TopNavigation from '@/components/TopNavigation/TopNavigation.vue';
  import Sidebar from '@/components/Sidebar/Sidebar.vue';

  export default {
    name: 'app',
    components: {
      TopNavigation,
      Sidebar,
    }
  }
</script>

<style lang="scss">
  @import '~element-ui/lib/theme-chalk/index.css';

  body {
    margin: 0;
    padding: 0;
    background-color: #EFEFEF;
  }

  #vue {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
  }
  #nav {
    padding: 30px;
    a {
      font-weight: bold;
      color: #2c3e50;
      &.router-link-exact-active {
        color: #42b983;
      }
    }
  }
</style>
