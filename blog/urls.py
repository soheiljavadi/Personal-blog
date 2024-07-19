from django.urls import path
from .views import info_list, create_info

urlpatterns = [
    path('infos/', info_list, name='info_list'),
    path('create_info/', create_info, name='create_info'),
 ]