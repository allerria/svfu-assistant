<template>
  <div>
    <form action="http://ricardoflick.ru:5001/recognize" method="post" enctype="multipart/form-data">
      <input type="file" name="file" accept="image/*">
      <input type="submit">
    </form>
  </div>
</template>

<script>
  export default {
    name: "SearchPrepodByPhoto"
  }
</script>

<style scoped>

</style>
