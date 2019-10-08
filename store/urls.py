from django.urls import path
from django.conf.urls import url, include


from django.contrib.auth import views as auth_views



from . import views


urlpatterns = [
    path('', views.home, name='home'),
path('', views.home, name='staff'),

path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),

path('rocket_home/', views.rocket_home, name='rocket_home'),
path('rocket_list/', views.rocket_list, name='rocket_list'),

path('rocket_detail/', views.rocket_list, name='rocket_detail'),


path('profile_list/', views.profile_list, name='profile_list'),
path('staff_detailtest/', views.staff_detailtest, name='staff_detailtest'),

path('product_list/', views.product_list, name='product_list'),


#path('product_detail/<int:pk>', views.product_detail, name='product_detail'),


path('product_detail/<int:pk>', views.ProductDetailView.as_view(), name='product_detail'),
path('profile_detail/<int:pk>', views.ProfileDetailView.as_view(), name='profile_detail'),


#path('agent/<int:pk>', views.AgentDetailView.as_view(), name='agent_detail'),

#path(r'^product_detail/(?P<pk>\d+)$', views.ProductDetailView.as_view(), name='product_detail'),


#path('product_detail/<int:pk>', views.product_detail, name='product_detail'),

#path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),





]
