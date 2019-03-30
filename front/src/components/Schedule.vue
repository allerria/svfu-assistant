<template>
  <div class="hello">
    <div class="kek">
      <mt-field label="Группа" placeholder="ИМИ-БА-ФИИТ-16" v-model="group">
      </mt-field>
      <mt-button type="default" @click.native="set_schedule" style="margin-right: 15px">ОК</mt-button>
    </div>


    <mt-index-list>
      <mt-index-section :index="day.day + ' ' + day.date" v-for="day in schedule.days">
        <div v-for="pair in day.pairs">
          <mt-cell :title="pair.name"></mt-cell>
          <mt-cell :title="pair.time"></mt-cell>
          <mt-cell :title="pair.prepod"></mt-cell>
          <mt-cell :title="pair.audience"></mt-cell>
        </div>

      </mt-index-section>
    </mt-index-list>
  </div>
</template>

<script>
  export default {
    name: 'Schedule',
    data() {
      return {
        group: "",
        schedule: []
      }
    },
    methods: {
      set_schedule() {
        fetch("http://ricardoflick.ru:5000/schedule2/" + this.group).then(resp => resp.json())
          .then(json => {
            console.log(json)
            this.schedule = json
          })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .kek {
    margin-top: 10px;
    display: flex;
    justify-content: space-between;
    flex-shrink: 0;
  }

  .mint-field {
    width: 100%;
  }

  .mint-indexlist-content {
    height: 100% !important;
    margin-right: 0 !important;
  }

  .mint-indexlist-navlist {
    height: 100% !important;
  }

  .mint-indexlist-nav {
    visibility: hidden;
    position: relative;
    n-bottom: 10px;
  }
</style>
