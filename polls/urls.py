from django.urls import path, include
from .views import home, result, candidate_delete, vote
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', home, name='home'),
    path('result/', result, name='result'),
    #path('<int:candidate_id>/', candidate_delete, name='candidate_delete'),
    path('vote/<int:cand_id>/<int:post_id>/', vote, name='vote'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)