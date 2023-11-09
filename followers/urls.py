from django.urls import path
from followers import views

urlpatterns = [
    path('followers/', views.FollowerList.as_view(), name='follower_list'),
    path('followers/<int:pk>/', views.FollowerDetails.as_view(), name='follower_details'),
]