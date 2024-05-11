<script setup>
import Swal from "sweetalert2"
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useStore } from "vuex"


const form = ref({
  username: "",
  password: "",
})

const store = useStore()

console.log(store)

const router = useRouter()

const handleLogin = async () => {
  try {
    Swal.fire({
      icon: "warning",
      title: "Please Wait!",
      allowOutsideClick: false,
      showConfirmButton: false,
      willOpen: () => {
        Swal.showLoading()
      },
    })

    const { username, password } = form.value // Extract email and password from the form

    console.log(form.value)
    await store.dispatch("auth/login", { username: username, password: password })
      .then(()=>{
        Swal.fire({
          title: "Login successful!",
          html: "Redirecting to  Dashboard...",
          showConfirmButton: false,
          timer: 3000,
        })
        Swal.close()
        router.push("/")
      })

    // Login successful, navigate to another route or do something else
  } catch (error) {
    // Login error, show error message
    console.error("Login error:", error)

    Swal.fire({
      icon: "error",
      title: "Check your username or password!",
      html: error || "An error occurred while logging in.",
    })
  }
}
</script>



<template>
    <div class="login-container">
        <h1>Login Form</h1>
        <form @submit.prevent="handleLogin" class="login-form">
            <label for="username">Username:</label>
            <input type="text" id="username" v-model="form.username" required>
            <label for="password">Password:</label>
            <input type="password" id="password" v-model="form.password" required>
            <button type="submit">Login</button>
        </form>
    </div>
</template>


<style scoped>
h1, label {
    color: black;
}
.login-container {
    text-align: center;
    margin-top: 50px;
}

.login-form {
    display: inline-block;
    border: 1px solid #ccc;
    padding: 20px;
    border-radius: 5px;
    background-color: #f9f9f9;
}

.login-form label {
    display: block;
    margin-bottom: 10px;
    font-weight: bold;
}

.login-form input {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border-radius: 3px;
    border: 1px solid #ccc;
}

.login-form button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 3px;
    cursor: pointer;
}

.login-form button:hover {
    background-color: #0056b3;
}
</style>
