from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [path('admin/', admin.site.urls),
    path('store/', include('store.urls')),
    path('', RedirectView.as_view(url='/store/')),]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#bug - had duplicated MEDIA_URL, end var shoudl have been MEDIA_ROOT - as above
#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(),name='logout'),]

