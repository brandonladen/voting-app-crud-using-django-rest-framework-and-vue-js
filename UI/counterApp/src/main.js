import '@/@iconify/icons-bundle'
import App from '@/App.vue'
import vuetify from '@/plugins/vuetify'
import { loadFonts } from '@/plugins/webfontloader'
import router from '@/router'
import '@core/scss/template/index.scss'
import '@layouts/styles/index.scss'
import '@styles/styles.scss'
import 'bootstrap/dist/css/bootstrap.css'
import { createPinia } from 'pinia'
import Swal from 'sweetalert2'
import { createApp } from 'vue'
<<<<<<< HEAD
import App from './App.vue'
import store from '@/store/modules/index.js';
import router from "./router"
=======
import store from './store'
>>>>>>> 962258574be1c30df545ef3633caa89138365b42

// Import your Vuex store
//Base Url
window.$http = 'http://localhost:8000/api/'
console.log

loadFonts()


// Create vue app
const app = createApp(App)

<<<<<<< HEAD
app.use(router)
app.use(store);
=======
app.config.globalProperties.$swal = Swal
>>>>>>> 962258574be1c30df545ef3633caa89138365b42

// Use plugins
app.use(vuetify)
app.use(createPinia())
app.use(router)
app.use(store)

// Mount vue app
app.mount('#app')
