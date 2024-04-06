// router/index.js

import { createRouter, createWebHistory } from 'vue-router';
import homeview from "../views/homeview.vue";
import results from "../views/results.vue";
import login from "../views/login.vue";
import store from '@/store/modules/index.js';

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/home',
            name: "home",
            component: homeview,
            meta: { requiresAuth: true } // Add meta field to indicate authentication requirement
        },
        {
            path:'/results',
            name: "results",    
            component: results,
            meta: { requiresAuth: true } // Add meta field to indicate authentication requirement
        },
        {
            path:'/login',
            name: "login",    
            component: login
        }
    ]
});

// Navigation guard to check authentication status before each navigation
router.beforeEach((to, from, next) => {
    const isAuthenticated = store.state.auth.isAuthenticated;

    if (to.meta.requiresAuth && !isAuthenticated) {
        // Redirect to login page if authentication is required but user is not authenticated
        next('/login');
    } else {
        // Continue to the requested route
        next();
    }
});

export default router;
