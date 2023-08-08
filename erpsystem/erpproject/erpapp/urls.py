from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.user_main, name='main'),
    path('login/', views.user_login, name='login'),
    path('newitem/', views.newitem, name='newitem'),
    path('viewitem/<int:item_id>/', views.viewitem, name='viewitem'),
    path('deleteitem/<int:item_id>/', views.delete_item, name='deleteitem'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 