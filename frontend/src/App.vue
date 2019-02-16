<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Dashboard</router-link> |
      <router-link to="/cashier">Cashier</router-link> |
      <router-link to="/login">Login</router-link> |
      <router-link to="/categories">Category</router-link> |
      <router-link to="/items">Item</router-link> |
      <router-link to="/users">User</router-link> |
    </div>
    <router-view/>
    <footer class="footer">
        <div class="content has-text-centered">
            Siphon ~ Cafe de GAMOYON ~ 
        </div>
    </footer>
  </div>
</template>

<style lang="scss">
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding-top: 10px;
  padding-bottom: 20px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
