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
    path('films/', views.topfilms, name='topfilms'),
    path('films/<int:pk_id>', views.more_info_about_film, name='moreinfo'),

    #Loginpaths
    path('login/', views.loginuser, name = 'loginuser'),
    path('signup/', views.signupuser, name = 'signupuser'),
    path('logout/', views.logoutuser, name = 'logoutuser'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

