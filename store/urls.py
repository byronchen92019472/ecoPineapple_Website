from django.urls import path
from django.conf.urls import url, include


from django.contrib.auth import views as auth_views



from . import views


urlpatterns = [
    path('', views.home, name='home'),
path('', views.home, name='staff'),

path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),
path('rocket/', views.rocket, name='rocket'),

path('staff_list/', views.staff_list, name='staff_list'),

path('product_list/', views.product_list, name='product_list'),


#path('product_detail/<int:pk>', views.product_detail, name='product_detail'),


path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),


#path('agent/<int:pk>', views.AgentDetailView.as_view(), name='agent_detail'),

#path(r'^product_detail/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),


#path('product_detail/<int:pk>', views.product_detail, name='product_detail'),

#path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),





]
