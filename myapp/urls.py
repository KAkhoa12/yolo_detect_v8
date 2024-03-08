from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index, name="index"),
   path('models/',views.listModel, name="listModel"),
   path('model/yolo/',views.modalYolo, name="modelYolo"),
   path('upload/',views.loadImage, name="upload"),
   path('predict_image/', views.predict_image_view, name='predict_image'),
]
