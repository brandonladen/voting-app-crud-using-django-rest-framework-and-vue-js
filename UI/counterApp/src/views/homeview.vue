<script setup>
import { ref } from 'vue';
import { onMounted } from 'vue';
import axios from 'axios';

import { useStore } from 'vuex';
import { useRouter } from 'vue-router';

const store = useStore();
const router = useRouter();

const handleLogout = () => {
  store.dispatch('auth/logout'); // Call logout action from Vuex store
  router.push('/login'); // Redirect to login page or any other page after logout
};

const CandidateUrl = ref('http://127.0.0.1:8000/api/candidates/');
const UsereUrl = ref('http://127.0.0.1:8000/api/user/');

const candidates = ref([]);
const userC = ref([]);

onMounted(async () => {
  try {
    const response = await axios.get(CandidateUrl.value, {
      auth: {
        username: 'brandon',
        password: '123',
      },
    });
    candidates.value = response.data;

    const response2 = await axios.get(UsereUrl.value, {
      auth: {
        username: 'brandon',
        password: '123',
      },
    });
    userC.value = response2.data;

  } catch (error) {
    console.error('Error fetching data:', error);
  }
});

const getPostName = (postCode) => {
  let position = "";
    if (postCode === 'P'){
      position = "President";
    } else if (postCode == 'G'){
      position = "Governor";
    } else if (postCode === 'MP'){
      position = "Member of Parliament";
    } else if (postCode === 'S'){
      position = "Senetor";
    } else {
      position = "Unknown"
    }

    return position;
  
};

const getUsername = (userId) => {
  // Find the corresponding user in the second API data
  const user2 = userC.value.results.find(user => user.id === userId);
  
  // Return the username or handle the case when the user is not found
  return user2 ? user2.first_name + ' ' + user2.last_name  : 'Unknown';
};
</script>

<template>
  <div class="app-container">
    <!-- Header -->
    <header class="header">
    <router-link to="/home" class="home_btn">Home</router-link>
    <router-link to="/results" class="results_btn">View Results</router-link>
      <button class="logout_btn" @click="handleLogout">Logout</button>
    </header>

    <div class="heading">
      <h2>Bengohub Cohort One Voting Portal 2024</h2>
      <p>Transparent and Accountable polling</p>
    </div>

    <!-- Main Content -->
    <div class="main-content">
      <div class="cand">
        <div v-for="candidate in candidates.results" :key="candidate.id" class="votcard shadow-md p-4">
          <img class="rounded-pill" :src="candidate.photo" alt="">
          <h4><b>{{ getUsername(candidate.user) }}</b></h4>
          <h4 class="fs-7">Running for: <span>{{ getPostName(candidate.post.title) }}</span></h4>
          <p>{{ candidate.background_info }}</p>
          <button class="vote-btn">Vote</button>
          <button class="view-btn">View</button>
        </div>
      </div>
    </div>

    <!-- Footer -->
    <footer class="footer">
      <p>2024 © All Rights Reserved | Designed and Developed by Bengo Hub</p>
    </footer>
  </div>
</template>

<style scoped>
.app-container {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

.cand {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content:  space-evenly;
}

.votcard {
  text-align: center;
  padding: 20px;
  border-radius: 10px;
  color: black;
}

.votcard:hover {
  transform: translateY(-5px);
}

img {
  height: 150px;
  width: 150px;
  object-fit: cover;
  border-radius: 50%;
  margin-bottom: 10px;
}

.vote-btn,
.view-btn, .logout_btn, .results_btn, .home_btn {
  background-color: #3490dc;
  color: white;
  padding: 8px 16px;
  margin: 5px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.vote-btn:hover,
.view-btn:hover {
  background-color: #2779bd;
}

.footer {
  text-align: center;
  padding: 10px;
  background-color: darkslategray;
  color: white;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #f0f0f0;
}

.main-content {
  flex-grow: 1;
}

.heading {
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 50px;
}

.heading h2 {
  color: black;
  font-weight: bolder;
  font-size: xx-large;
  font-family: 'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
  margin: 0;
}

.heading p {
  color: black;
  font-size: x-large;
}
</style>
