// src/store/index.js
import { createStore } from 'vuex'
import authModule from './auth.js' // Import your 'auth' module


const store = createStore({
  modules: {
    auth: authModule,
  },
})

export default store