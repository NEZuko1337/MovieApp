from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from movieapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('advice', views.advice_film, name = 'advicepage'),
    path('advice/', views.advice_film, name = 'advice'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

