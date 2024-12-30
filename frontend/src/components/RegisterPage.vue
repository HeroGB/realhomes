<template>
  <div>
    <h1>Register</h1>
    <form @submit.prevent="registerUser">
      <input v-model="username" type="text" placeholder="Username" required />
      <input v-model="email" type="email" placeholder="Email" required />
      <input
        v-model="password"
        type="password"
        placeholder="Password"
        required
      />
      <select v-model="role" required>
        <option value="buyer">Buyer</option>
        <option value="seller">Seller</option>
        <option value="agent">Agent</option>
      </select>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "RegisterPage",
  data() {
    return {
      username: "",
      email: "",
      password: "",
      role: "buyer",
    };
  },
  methods: {
    async registerUser() {
      try {
        const response = await axios.post(
          "http://127.0.0.1:8000/api/register/",
          {
            username: this.username,
            email: this.email,
            password: this.password,
            role: this.role,
          }
        );
        alert(response.data.message);
      } catch (error) {
        alert("Error: " + error.response.data.message);
      }
    },
  },
};
</script>
