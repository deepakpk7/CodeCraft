from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
    # path('',views.about),
    path('contact',views.contact),
    path('courses',views.courses),
    path('placement',views.placement),
    
    
]
