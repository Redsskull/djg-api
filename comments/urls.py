from django.urls import path
from posts import views

urlpatterns = [
    path('comments/', views.PostList.as_view()),
    path('comments/<int:pk>/', views.PostDetail.as_view()),
]