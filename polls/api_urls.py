from rest_framework.routers import DefaultRouter 
from .api_views import PostViewSet, CandidateViewSet, VoterViewSet, VoteViewSet, UserViewSet
from django.urls import path, include

router = DefaultRouter() 
router.register(r'posts', PostViewSet) 
router.register(r'candidates', CandidateViewSet) 
router.register(r'voters', VoterViewSet)
router.register(r'votes', VoteViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)), 
]