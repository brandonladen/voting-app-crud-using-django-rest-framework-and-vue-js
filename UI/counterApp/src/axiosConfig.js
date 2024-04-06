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