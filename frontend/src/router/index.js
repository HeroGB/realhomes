import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import RegisterForm from "@/components/RegisterForm.vue";
import Login from "@/components/Login.vue";
import Dashboard from "@/components/Dashboard.vue";
import NotFound from "@/components/NotFound.vue";

// Helper function to check if the token is expired
function isTokenExpired() {
  const accessToken = localStorage.getItem("access_token");
  if (!accessToken) return true;

  // Decode the JWT token to check the expiration date
  const payload = JSON.parse(atob(accessToken.split(".")[1])); // Decode the token
  const expiry = payload.exp * 1000; // JWT expiration is in seconds, so convert to milliseconds
  return Date.now() > expiry;
}

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
  {
    path: "/register",
    name: "Register",
    component: RegisterForm,
    meta: { requiresGuest: true }, // Only for unauthenticated users
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
    meta: { requiresGuest: true }, // Only for unauthenticated users
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: { requiresAuth: true }, // Requires authentication
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: NotFound,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// Navigation Guards
router.beforeEach((to, from, next) => {
  const isAuthenticated = !isTokenExpired(); // Use the function to check if the token is expired

  if (to.meta.requiresAuth && !isAuthenticated) {
    // Redirect to login if the route requires authentication
    return next({ name: "Login" });
  }

  if (to.meta.requiresGuest && isAuthenticated) {
    // Redirect to dashboard if the user is authenticated
    return next({ name: "Dashboard" });
  }

  next();
});

export default router;
