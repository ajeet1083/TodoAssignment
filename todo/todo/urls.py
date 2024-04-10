from django.contrib import admin
from django.urls import path, include
from todoapp import views as todo_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todoapp.urls')),
    path('registration', todo_views.register, name= 'register'),
    path('login', auth_views.LoginView.as_view(template_name = 'dashboard/login.html'), name = 'login'),
    path('profile', todo_views.profile, name = 'profile'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'dashboard/logout.html'), name='logout')
]