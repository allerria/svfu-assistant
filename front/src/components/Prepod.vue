<template>
  <div>
    <mt-cell
      :title="prepod.name">
      <img slot="icon" :src="prepod.img_url" width="100%">
    </mt-cell>
    <mt-index-list>
      <mt-index-section :index="subject.day" v-for="subject in subjects">
        <mt-cell :title="subject.time"></mt-cell>
        <mt-cell :title="subject.group"></mt-cell>
        <mt-cell :title="subject.name"></mt-cell>
        <mt-cell :title="subject.audience"></mt-cell>
      </mt-index-section>
    </mt-index-list>
  </div>

</template>

<script>
  export default {
    name: "Prepod",
    data() {
      return {
        prepod: {},
        subjects: {}
      }
    },
    computed: {
      id() {
        // We will see what `params` is shortly
        return this.$route.params.id
      },
    },
    mounted() {
      this.$nextTick(() => {
        fetch("http://ricardoflick.ru:5000/prepod/" + this.id).then(resp => resp.json())
          .then(json => {
              console.log(json)
              this.prepod = json
            }
          )
        fetch("http://ricardoflick.ru:5000/schedule/" + this.id).then(resp => resp.json())
          .then(json => {
              console.log(json)
              this.subjects = json.subjects
            }
          )
      })
    }
  }
</script>

<style>
  .mint-indexlist-content {
    height: 100% !important;
    margin-right: 0 !important;
  }

  .mint-indexlist-navlist {
    height: 100% !important;
  }

  .mint-indexlist-nav {
    position: relative;
    visibility: hidden;

  }
</style>
