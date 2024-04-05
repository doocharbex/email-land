from django.urls import path
from .views import *


urlpatterns = [
    path('', bot_status, name='bot_status')
]