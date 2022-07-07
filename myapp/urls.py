from django.urls import path
from myapp import views

urlpatterns = [
    path('usrapi/', views.UserAPI.as_view()),   
    path('usrapi/<int:pk>', views.UserAPI.as_view())
]