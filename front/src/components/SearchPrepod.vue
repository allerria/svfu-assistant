<template>
  <div>
    <mt-search v-model="value" placeholder="Имя преп..." autofocus cancel-text="Очистить"
               :result.sync="result">
      <mt-cell
        v-for="item in result2"
        :title="item.name">
        <a @click="pushTo(item.id)">
          <img slot="icon" :src="item.img_url" style="width: 100%">
        </a>

      </mt-cell>
    </mt-search>
  </div>
</template>

<script>
  export default {
    name: "SearchPrepod",
    data() {
      return {
        value: '',
        result2: []
      };
    },
    methods: {
      pushTo(id) {
        this.$router.push({"name": "Prepod", params: {"id": id}})
      }
    },
    computed: {
      // a computed getter
      result() {
        console.log('asd')
        if (this.value.length < 3) {
          this.result2 = []
          return []
        }
        fetch('http://ricardoflick.ru:5000/search?q=' + this.value).then(resp => resp.json())
          .then(json => {
            this.result2 = json.prepods
            return json.prepods
          })
        this.result2 = []
        return []
      }
    }
  }
</script>

<style>

  .mint-cell-wrapper {
    padding: 0 !important;
  }

  .mint-search-list {
    position: relative !important;
    padding-top: 0 !important;
  }

  .mint-search {
    height: 100% !important;
    margin-bottom: 10px;
  }

</style>
