<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="registerUser">
      <input
        v-model="username"
        type="text"
        placeholder="Username"
        required
        class="input-field"
      />
      <input
        v-model="email"
        type="email"
        placeholder="Email"
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
      <select v-model="role" required class="select-field">
        <option disabled value="">Select Role</option>
        <option value="buyer">Buyer</option>
        <option value="seller">Seller</option>
        <option value="agent">Agent</option>
      </select>
      <button type="submit" class="btn-primary" :disabled="loading">
        {{ loading ? "Registering..." : "Register" }}
      </button>
      <p v-if="errorMessage" class="error-text">{{ errorMessage }}</p>
      <p v-if="successMessage" class="success-text">{{ successMessage }}</p>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterForm",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      role: "",
      loading: false,
      errorMessage: "",
      successMessage: "",
    };
  },
  methods: {
    async registerUser() {
      this.loading = true;
      this.errorMessage = "";
      this.successMessage = "";
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/users/auth/register/",
          {
            username: this.username,
            email: this.email,
            password: this.password,
            role: this.role,
          }
        );
        this.successMessage = response.data.message;
        this.username = "";
        this.email = "";
        this.password = "";
        this.role = "";
      } catch (error) {
        this.errorMessage =
          error.response?.data?.message ||
          "An error occurred during registration.";
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>
