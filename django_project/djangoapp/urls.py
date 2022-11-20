from operator import index
#from _operator import index

from.import views
from django.urls import path

#from .views import index

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('index/',views.index,name=index)
]