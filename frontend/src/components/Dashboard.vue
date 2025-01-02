<template>
  <div class="dashboard">
    <h1>Welcome to the Dashboard</h1>
    <p>You are logged in!</p>
    <button @click="logoutUser">Logout</button>
  </div>
</template>

<script>
export default {
  name: "DashboardView",
  methods: {
    logoutUser() {
      // Clear the tokens from localStorage
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");

      // Redirect to login page after logout
      this.$router.push({ name: "Login" });
    },
  },
};
</script>

<style scoped>
.dashboard {
  padding: 20px;
  text-align: center;
}

button {
  margin-top: 20px;
  padding: 10px;
  background-color: #f44336;
  color: white;
  border: none;
  cursor: pointer;
}

button:hover {
  background-color: #d32f2f;
}
</style>
