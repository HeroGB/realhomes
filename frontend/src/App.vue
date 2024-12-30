<template>
  <div id="app">
    <!-- Add navigation if necessary -->
    <nav>
      <a href="/login">Login</a>
      <a href="/register">Register</a>
    </nav>

    <!-- The router-view is where the dynamic components will render -->
    <router-view></router-view>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      message: "",
    };
  },
  mounted() {
    // Optional: Fetch data from the backend, if needed for initial load
    axios
      .get("http://127.0.0.1:8000/api/hello/")
      .then((response) => {
        this.message = response.data.message;
      })
      .catch((error) => {
        console.error("There was an error fetching data:", error);
      });
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  margin: 0 10px;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
