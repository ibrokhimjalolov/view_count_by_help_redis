from django.urls import path
from .views import PostDetailView


urlpatterns = [
    path('<int:pk>/', PostDetailView.as_view(), name='post-detail')
]
