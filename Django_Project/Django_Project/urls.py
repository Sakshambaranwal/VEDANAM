"""Django_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.urls import path, include
import Book_store.urls
from User import views as user_views
from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(Book_store.urls, namespace = 'Book_store')),
    path('register/', user_views.register, name = 'register'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name = 'logout'),
    path('profile/', user_views.profile, name = 'profile'),
    path('account/', user_views.account, name = 'account'),
    path('cart/add/<int:id>/', user_views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', user_views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', user_views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', user_views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', user_views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',user_views.cart_detail,name='cart_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)