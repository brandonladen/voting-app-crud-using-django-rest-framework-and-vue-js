import axios from "axios"

const tokenString = sessionStorage.getItem('token')
const baseURL = 'http://localhost:8000'

const axiosInstance = axios.create({
  baseURL: baseURL, 
  timeout: 360_000,
  headers: {
    'Content-Type': 'application/json',
    Authorization: `Token ${tokenString}`
  },
})

export default axiosInstance