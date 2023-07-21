from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from app.views import *

urlpatterns = [
    path('', views.home, name='home'),
    path('search', views.search, name='search'),    
    path('load-cars', views.load_cars, name='ajax_load_cars'),
    path('searchdd', views.searchdd, name='searchdd'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('allreview', views.allreview, name='allreview'),
    path('terms', views.terms, name='terms'),
    path('contact', views.contact, name='contact'),
    
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
