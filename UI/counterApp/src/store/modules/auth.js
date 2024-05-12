// src/store/auth/auth.js
import axios from '@/axiosConfig';

const state = {
  isAuthenticated: false,
  user: null,
};

const mutations = {
  SET_AUTHENTICATED(state, isAuthenticated) {
    state.isAuthenticated = isAuthenticated;
  },
  SET_USER(state, user) {
    state.user = user;
  },
};

const actions = {
  async login({ commit }, payload) {
    try {
      const response = await axios.post('/api-token/', payload);
      // Extract the access token from the response
      const accessToken = response.data.access;

      // You can decode the access token to get user information if needed
      // For example, if the access token contains user information

      // Set the access token in local storage
      sessionStorage.setItem('accessToken', accessToken);

      commit('SET_AUTHENTICATED', true);
      
      // Set user information if needed
      commit('SET_USER', null); // Update with appropriate user data if available

      return true;

    } catch (error) {
      // Handle login error
      console.error('Login failed:', error.message);
      throw new Error('An error occurred during login.');
    }
  },

  logout({ commit }) {
    // Remove access token from local storage
    sessionStorage.removeItem('accessToken');

    // Clear authentication state
    commit('SET_AUTHENTICATED', false);
    commit('SET_USER', null);
  },

  checkAuthentication({ commit }) {
    const accessToken = localStorage.getItem('accessToken');
    
    // Check if access token exists
    if (accessToken) {
      // Set authentication state
      commit('SET_AUTHENTICATED', true);
      
      // Fetch user information if needed
      commit('SET_USER', null); // Update with appropriate user data if available
    }
  },
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
};
