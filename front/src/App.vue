<template>
  <div id="app">
    <mt-navbar v-model="selected" @click.native="push">
      <mt-tab-item id="1">Поиск препода</mt-tab-item>
      <mt-tab-item id="2">Расписание</mt-tab-item>
      <mt-tab-item id="3">Поиск препода по фото</mt-tab-item>
    </mt-navbar>
    <router-view/>
  </div>
</template>

<script>
  export default {
    name: 'App',

    data() {
      return {
        selected: '1'
      };
    },
    methods: {
      push() {
        if (this.selected == "1") {
          this.$router.push({name: 'SearchPrepod'})
        } else if (this.selected == "2") {
          this.$router.push({name: 'Schedule'})
        } else {
          this.$router.push({name: 'SearchPrepodByPhoto'})
        }
      }
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
    margin-top: 20px;
  }
</style>
