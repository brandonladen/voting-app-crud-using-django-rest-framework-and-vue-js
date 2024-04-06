from rest_framework import serializers
from Accounts.models import Candidate, Voter, Vote, Post
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email'] 
        #fields = '__all__'
class PostSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Post 
        fields = '__all__' 
    
class CandidateSerializer(serializers.ModelSerializer): 
    post = PostSerializer() 
    class Meta: 
        model = Candidate 
        fields = '__all__'

class VoterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voter
        fields = '__all__'

class VoteSerializer(serializers.ModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Vote
        fields = '__all__'