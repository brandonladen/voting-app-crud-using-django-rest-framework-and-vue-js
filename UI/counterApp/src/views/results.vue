<script setup>
import { ref } from 'vue';
import { onMounted } from 'vue';
import axios from 'axios';

const CandidateUrl = ref('http://127.0.0.1:8000/api/candidates/');
const UsereUrl = ref('http://127.0.0.1:8000/api/user/');
const votesUrl = ref('http://127.0.0.1:8000/api/votes/');

const userC = ref([]);
const candidates = ref([]);
const votes = ref([]);

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

    const response3 = await axios.get(votesUrl.value, {
      auth: {
        username: 'brandon',
        password: '123',
      },
    });
    votes.value = response3.data;

  } catch (error) {
    console.error('Error fetching data:', error);
  }
});

const getUsername = (userId) => {
  // Find the corresponding user in the second API data
  const user2 = userC.value.results.find(user => user.id === userId);
  
  // Return the username or handle the case when the user is not found
  return user2 ? user2.first_name + ' ' + user2.last_name  : 'Unknown';
};

const votepercentage = (votes_per_c) => {
    const total_votes = votes.value.results.length - 1;
    const candidate_votes = votes_per_c;

    if (candidate_votes > 0) {
        const percentageV = (candidate_votes / total_votes) * 100;
        return Math.round(percentageV);
    } else {
        return 0;
    }
};
</script>

<template>
    <!-- <h1>>>>>{{ votepercentage   }}<<<</h1> -->
    <!-- Header -->
    <header class="header">
      <router-link to="/home" class="home_btn">Home</router-link>

    </header> 

    <div class="heading">
      <h2>Bengohub 2024 Voting Results</h2>
      <p>Transparent and Accountable polling results</p>
    </div>
    
  <div class="app-container">
     <!-- Main card-->
     <div class="main-card">
        <div v-for="candidate in candidates.results" :key="candidate.id" class="card-content">
          <div class="card-image">
            <img class="rounded-pill max-130 p-2" :src="candidate.photo" alt="">
          </div>
          <div class="card-details">
            <h4>{{ getUsername(candidate.user) }}</h4>
            <p>{{ candidate.votes.length  }} Votes</p>
            <div class="progress">
              <!-- <div class="progress-bar bg-warning" role="progressbar" aria-label="Example with label" style="width: 55%;" aria-valuenow="55" aria-valuemin="0" aria-valuemax="100">55%</div> -->
              <label>{{ votepercentage(candidate.votes.length)  }}% </label>
              <progress max="100" :value="votepercentage(candidate.votes.length)"></progress>
            </div>
          </div>
        </div>
      </div>	
    </div>
    <!-- Footer -->
    <footer class="footer">
      <p>2024 © All Rights Reserved | Designed and Developed by Bengo Hub</p>
    </footer>
 
</template>

<style scoped>
progress{
    width: 250px;
    height: 20px;
}

label {
    color: black;
}
.main-card {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  flex-wrap: wrap; /* Allow cards to wrap onto the next line */
}

.card-content {
  display: flex;
  gap: 20px;
  text-align: center;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  background-color: #fff;
  margin-bottom: 20px; /* Add margin-bottom for spacing between cards */
}

.card-image img {
  height: 150px;
  width: 150px;
  object-fit: cover;
  border-radius: 50%;
}

.card-details {
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: left;
}

.card-details h4 {
  color: black;
  font-weight: bolder;
  font-size: x-large;
  margin: 0;
}

.card-details p {
  color: black;
  font-size: large;
  margin: 5px 0;
}


.progress-bar {
  border-radius: 5px; /* Optional: Add rounded corners to the progress bar */
}



.app-container {
  min-height: 100vh;
  display: flex;
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
  padding: 5px;
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
