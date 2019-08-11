from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
     path('', views.home, name='home'),
     path('new/neighbourhood/', views.create_neighbourhood, name='createhood'),
     path('join/(?P<neighbourhood_id>\d+)/', views.join_neighbourhood, name='join'),
     path('leave/(?P<neighbourhood_id>\d+)/', views.leave_neighbourhood, name='leave'),
     path('new/business/', views.create_business, name='createbusiness'),
     path('userhood/', views.user_neighbourhood, name='userneighbourhoods'),
     path('new/post/', views.create_post, name='createpost'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)