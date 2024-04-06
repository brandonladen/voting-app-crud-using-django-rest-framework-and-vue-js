from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('candidate_register/', register_candidate, name='register_candidate'), #register candidate button
    path('voter_register/', register_voter, name='voter_register'),
    path('login/', login_user, name='login'),
    path('logout/',logout_user,name='logout'),
    
    path('crud/', CrudView.as_view(), name='crud_ajax'),
    path('ajax/crud/delete/', views.DeleteCrudUser.as_view(), name='crud_ajax_delete'),
    path('ajax/crud/create/', views.CreateCrudUser.as_view(), name='crud_ajax_create'),
    path('ajax/crud/update/', views.UpdateCrudUser.as_view(), name='crud_ajax_update'),
]