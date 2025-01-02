<template>
  <div class="not-found">
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you're looking for doesn't exist.</p>
    <router-link to="/">Go to Home</router-link>
  </div>
</template>

<script>
export default {
  name: "NotFound",
};
</script>

<style scoped>
.not-found {
  padding: 20px;
  text-align: center;
}

h1 {
  color: #f44336;
}

router-link {
  display: inline-block;
  margin-top: 20px;
  padding: 10px;
  background-color: #42b983;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}

router-link:hover {
  background-color: #388e3c;
}
</style>
