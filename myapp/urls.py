from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index, name="index"),
   path('upload/',views.loadImage, name="upload"),
   path('predict_image/', views.predict_image_view, name='predict_image'),
]
