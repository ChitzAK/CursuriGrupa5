from django.urls import path

from userprofile import views

app_name = 'userprofile'

urlpatterns = [
    path('updateProfile/<int:pk>/', views.UpdateProfile.as_view(), name='modificare'),
    path('new_account/', views.CreateNewAccount.as_view(), name='utilizator_nou'),
]