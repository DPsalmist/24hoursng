from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'), 
    path('hypertensiontea/', views.hypertension_tea, name='hypertension_tea'), 
    path('thankyou/', views.thankyou, name='thankyou'),    
]
