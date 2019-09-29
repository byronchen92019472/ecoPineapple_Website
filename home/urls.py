from django.urls import path
from django.conf.urls import url, include


from django.contrib.auth import views as auth_views

from . import views


urlpatterns = [
    path('', views.home, name='home'),




    #relate to getting agent editing to work
    #path(r'agent/(?P<id>\d+)/$', views.update_agent, name='update_agent'),
    #path(r'^add/agent/$', views.add_agent, name='add_agent'),
    #path('agent/(?P<id>\d+)/$', views.AgentUpdateDetails, name='agent_detail'),

]
