"""twitterclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from authentication import views
from tweet.views import tweet_detail
from twitteruser.views import index, profile, follower, unfollow
from notification.views import notification_view, delete_notification

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),
    path('profile/<int:id>/', profile, name="profile"),
    path('profile/<int:id>/follow/add/', follower, name="follower"), 
    path('profile/<int:id>/follower/delete/', unfollow, name="unfollow"),  
    path('tweet/<int:id>/', tweet_detail, name="tweet_detail"),  
    path('notification/', notification_view),  
    path('notification/delete/<int:id>', delete_notification),
    path('login/', views.login_view, name="login"),
    path('signup/', views.signup_view, name="signup"),
    path('logout/', views.logout_view, name="logout"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
