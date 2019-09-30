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
#path('login/', views.login, name='login'),

    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),

path('product_home/', views.product_home, name='product_home'),
#path('product_detail/', views.product_detail, name='product_detail'),



path('product_detail/1', views.product_detail, name='product_detail'),





    #path('product_home/', views.product_home, name='product_home'),
#path('products/', views.products, name='products'),
#path('products_from_db/', views.products_from_db, name='products_from_db'),

    #path('tours/', views.TourListView.as_view(), name='tours'),
    #path('agents/', views.AgentListView.as_view(), name = 'agents'),
    #path('tour/<int:pk>', views.TourDetailView.as_view(), name='tour_detail'),
    #path('agent/<int:pk>', views.AgentDetailView.as_view(), name='agent_detail'),
    #path('tours_by_agent/', views.ToursByAgentListView.as_view(), name='my_tours'),

    #relate to getting agent editing to work
    #path(r'agent/(?P<id>\d+)/$', views.update_agent, name='update_agent'),
    #path(r'^add/agent/$', views.add_agent, name='add_agent'),
    #path('agent/(?P<id>\d+)/$', views.AgentUpdateDetails, name='agent_detail'),

]
