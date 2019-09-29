from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from home import views
from store import views
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

]

urlpatterns += [
    path('store/', include('store.urls')),
]


urlpatterns += [
    path('', RedirectView.as_view(url='/store/')),
]






urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    #path('accounts/', include('django.contrib.auth.urls')),
]
