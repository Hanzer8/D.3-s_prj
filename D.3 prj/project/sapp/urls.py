from django.urls import path
from .views import PostsList, PostDetail


urlpatterns = [
   path('', PostsList.as_view()),
   path('', PostDetail.as_view(), name='post'),
]