from rest_framework import viewsets 
from .serializers import CandidateSerializer, PostSerializer , VoterSerializer, VoteSerializer, UserSerializer
from Accounts.models import Candidate, Vote, Voter, Post
from django.contrib.auth.models import User
from rest_framework.pagination import PageNumberPagination 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from rest_framework.permissions import IsAuthenticated 


class CustomPageNumberPagination(PageNumberPagination): 
    page_size = 10
    page_size_query_param = 'page_size' 
    max_page_size = 100 


class PostViewSet(viewsets.ModelViewSet): 
    queryset = Post.objects.all() 
    serializer_class = PostSerializer 
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    
    
class CandidateViewSet(viewsets.ModelViewSet): 
    queryset = Candidate.objects.all() 
    serializer_class = CandidateSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]

class VoterViewSet(viewsets.ModelViewSet):
    queryset = Voter.objects.all()
    serializer_class = VoterSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    pagination_class = CustomPageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication] 
    permission_classes = [IsAuthenticated]
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer