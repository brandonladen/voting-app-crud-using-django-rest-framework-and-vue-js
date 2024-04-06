<<<<<<< HEAD
import axios from "axios"

const tokenString = sessionStorage.getItem('token')//sessionStorage, localStorage //Json Web Token - 
const baseURL = 'http://localhost:8000'

const axiosInstance = axios.create({
  baseURL: baseURL, // Replace with your Django backend URL
  timeout: 360_000, // 6 mins timeout
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Token ${tokenString}`
  },
})

export default axiosInstance
=======
import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://localhost:8000/api/',  
  timeout: 5000,  
  headers: {
    'Content-Type': 'authentication/json',
  },
});


axiosInstance.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers['Authorization'] = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

export default axiosInstance;
>>>>>>> 962258574be1c30df545ef3633caa89138365b42
