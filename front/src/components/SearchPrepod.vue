<template>
  <div>
    <mt-search v-model="value" placeholder="Имя преп..." autofocus cancel-text="Очистить"
               :result.sync="result">
      <mt-cell
        v-for="item in result2"
        :title="item.name">

          <img slot="icon" v-lazy="item.img_url" width="100%">

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
    computed: {
      // a computed getter
      result() {
        console.log('asd')
        if (this.value.length < 3) {
          this.result2 = []
          return []
        }
        fetch('http://localhost:5000/search?q=' + this.value).then(resp => resp.json())
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
