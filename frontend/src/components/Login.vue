<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="loginUser">
      <input
        v-model="username"
        type="text"
        placeholder="Username"
        required
        class="input-field"
      />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        required
        class="input-field"
      />
      <button type="submit" class="btn-primary">
        {{ loading ? "Logging in..." : "Login" }}
      </button>
    </form>
    <p v-if="errorMessage" class="error-text">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "LoginPage", // Component name changed to multi-word to satisfy eslint
  data() {
    return {
      username: "",
      password: "",
      loading: false,
      errorMessage: "",
    };
  },
  methods: {
    async loginUser() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/users/auth/login/",
          {
            username: this.username,
            password: this.password,
          }
        );
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);
        this.$router.push("/dashboard"); // Redirect after login
      } catch (error) {
        this.errorMessage =
          error.response?.data?.message || "An error occurred during login.";
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
