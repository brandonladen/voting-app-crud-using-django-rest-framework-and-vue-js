import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import store from '@/store/modules/index.js';
import router from "./router"

import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/reset.css';

const app = createApp(App)

app.use(router)
app.use(Antd)
app.use(store);

app.mount('#app')
