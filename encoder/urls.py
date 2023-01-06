from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('encode/',views.encode,name='encode'),
    path('decode/',views.decode,name='decode'),
    path('about/',views.about,name='about'),
    path('encoded/<str:scheme>/',views.results ,name='results'),
]