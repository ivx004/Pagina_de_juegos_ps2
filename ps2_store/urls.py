from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('juegos.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='juegos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
