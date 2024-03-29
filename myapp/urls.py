from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.index, name="index"),
   path('models/',views.listModel, name="listModel"),
   path('model/yolo/',views.modalYolo, name="modelYolo"),
   path('model/gan/',views.modalGan, name="modelGan"),
   path('model/yolo/upload/',views.loadImageYolo, name="uploadYolo"),
   path('model/yolo/predict_image/', views.predict_image_viewYolo, name='predict_image_Yolo'),
   path('model/gan/upload/face2comic',views.uploadGanFace2Comic, name="uploadGanFace2Comic"),
   path('model/gan/upload/comic2face',views.uploadGanComic2Face, name="uploadGanComic2Face"),
   path('model/gan/predict_image/face2comic', views.predictGanFace2Comic, name='predictGanFace2Comic'),
   path('model/gan/predict_image/comic2face', views.predictGanComic2Face, name='predictGanComic2Face'),
]
