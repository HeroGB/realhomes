<template>
  <div id="app">
    <nav>
      <router-link v-if="!isAuthenticated" to="/login">Login</router-link>
      <router-link v-if="!isAuthenticated" to="/register">Register</router-link>
      <router-link v-if="isAuthenticated" to="/dashboard"
        >Dashboard</router-link
      >
      <a v-if="isAuthenticated" href="#" @click.prevent="logout">Logout</a>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  data() {
    return {
      isAuthenticated: false,
    };
  },
  methods: {
    checkAuth() {
      // Check if tokens are present in localStorage
      this.isAuthenticated =
        !!localStorage.getItem("access_token") &&
        !!localStorage.getItem("refresh_token");
    },
    logout() {
      // Clear tokens and redirect to login
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      this.isAuthenticated = false;
      this.$router.push("/login");
    },
  },
  created() {
    this.checkAuth();
  },
  watch: {
    // Watch for route changes to re-check auth state
    $route() {
      this.checkAuth();
    },
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
  text-decoration: none;
}

nav a.router-link-exact-active {
  color: #42b983;
}

nav a:hover {
  color: #42b983;
}
</style>
