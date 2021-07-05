from os import name
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('login',views.loginPage,name='login'),
    path('register',views.register,name='register'),
    path('honk', views.index,name="honk"),
    path('success', views.success, name = 'success'),
    path('work',views.work,name='work'),
    path('image',views.image,name='image'),
    path('compiler',views.compiler,name='compiler')
    
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)