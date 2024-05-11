<script>
import axios from 'axios';
export default {
  props: ['candidate', 'open', 'getUsername'],
  methods: {
    
    async vote() {
      try {
        // Fetch post data using candidate endpoint
    
        const postData = this.candidate.post.id;

        // Voter ID is obtained from the logged-in user
        const voterId = 1;

        // Create vote instance
        const voteData = {
          the_candidate: this.candidate.id,
          voter: voterId,
          post: postData
        };

        // Send POST request to create vote
        const response = await axios.post('http://127.0.0.1:8000/api/votes/', voteData, {
          auth: {
            username: 'brandon',
            password: '123',
          },
        });

        console.log('Vote successful:', response.data);
        // You can emit an event here or perform any other action after successful voting

        // Close the modal after voting
        this.$emit('update:open', false);
      } catch (error) {
        console.error('Error voting:', error);
      }
    },
    handleOk() {
        this.$emit('update:open', false);
    }
  }
}
</script>

<template>
    <a-modal :visible="open" @ok="handleOk"  @Cancel="handleOk"  @Close="handleOk" :mask-style="{ backgroundColor: 'rgba(200, 200, 200, 0.1)' }">
      <div class="modal-content">
        <img class="rounded-pill" :src="candidate.photo" alt="">
        <h4><b>{{ getUsername(candidate.user) }}</b></h4> 
        <h4 class="fs-7">Running for: <span>{{ candidate.post.title }}</span></h4>
        <p>Background info: {{ candidate.background_info }}</p>
        <p>Manifesto: {{ candidate.manifesto }}</p>
        <button class="vote-btn"  @click="vote">Vote</button>
      </div>
    </a-modal>
  </template>
  
  <style scoped>
  .modal-content {
    display: flex;
    flex-direction: column;
    justify-content: center; /* Center vertically */
    align-items: center; /* Center horizontally */
  }
  
  .vote-btn {
    background-color: #3490dc;
    color: white;
    padding: 8px 16px;
    margin: 5px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.2s;
  }
  
  .rounded-pill {
    max-width: 100%; /* Set maximum width */
    max-height: 300px; /* Set maximum height */
    object-fit: cover; /* Maintain aspect ratio */
  }
  </style>