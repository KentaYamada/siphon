<template>
  <div id="app">
      <navigation/>
      <router-view/>
      <footer class="footer">
          <div class="content has-text-centered">
              Siphon ~ cafe de GAMOYON ~ 
          </div>
      </footer>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import Navigation from '@/components/navigation/Navigation.vue';


export default Vue.extend({
    components: {
        Navigation
    }
});
</script>
