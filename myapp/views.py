from django.shortcuts import render,redirect
from .services import yolo
from .services import gan
import shutil
import base64
from io import BytesIO
from PIL import Image
from django.views.decorators.csrf import csrf_exempt
# from cloudinary.uploader import upload
# from cloudinary.api import resources
# from cloudinary.forms import cl_init_js_callbacks
from ultralytics import YOLO
from django.conf import settings
import os
from django.http import HttpResponse
import tensorflow as tf
import requests
from django.http import JsonResponse

import uuid
import time

def areUpdate():
    return render(requests,'')
def generate_unique_filename():
    unique_id = str(uuid.uuid4())[:8] 
    timestamp = str(int(time.time())) 
    return f"generated_image_{timestamp}_{unique_id}.jpg"
def index(request):
    return render(request, 'myapp/pages/home/index.html')

#list models page
def listModel(request):
    return render(request, 'myapp/pages/home/listModal.html')

#yolo page
def modalYolo(request):
    return render(request, 'myapp/pages/yolo/index.html')

#gan page
def modalGan(request):
    return render(request, 'myapp/pages/gan/index.html')

def uploadGanFace2Comic(request):
    return render(request, 'myapp/pages/gan/face2comic.html')


def uploadGanComic2Face(request):
    if request.method == 'POST':
        uploaded_images = request.FILES.getlist('images')
        input_folder_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')
        predict_folder_path = os.path.join(settings.BASE_DIR, 'static/image/predict')
        if os.path.exists(predict_folder_path):
            shutil.rmtree(predict_folder_path)
        if os.path.exists(input_folder_path):
            shutil.rmtree(input_folder_path)
        os.makedirs(input_folder_path, exist_ok=True)

        for uploaded_image in uploaded_images:
            image_path = os.path.join(input_folder_path, uploaded_image.name)

            with open(image_path, 'wb') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

        return render(request, 'myapp/pages/gan/comic2face.html', context={'image_files_input': predict_folder_content()})
    return render(request, 'myapp/pages/gan/comic2face.html')

def loadImageYolo(request):
    if request.method == 'POST':
        uploaded_images = request.FILES.getlist('images')
        input_folder_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')
        predict_folder_path = os.path.join(settings.BASE_DIR, 'static/image/predict')
        if os.path.exists(predict_folder_path):
            shutil.rmtree(predict_folder_path)
        if os.path.exists(input_folder_path):
            shutil.rmtree(input_folder_path)
        os.makedirs(input_folder_path, exist_ok=True)

        for uploaded_image in uploaded_images:
            image_path = os.path.join(input_folder_path, uploaded_image.name)

            with open(image_path, 'wb') as destination:
                for chunk in uploaded_image.chunks():
                    destination.write(chunk)

        return render(request, 'myapp/pages/yolo/load.html', context={'image_files_input': predict_folder_content()})
    return render(request, 'myapp/pages/yolo/load.html')

def predict_folder_content():
    input_folder_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')
    input_folder_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')
    return [f for f in os.listdir(input_folder_path) if os.path.isfile(os.path.join(input_folder_path, f))]

def predict_image_viewYolo(request):
    if request.method == 'POST':
        best_pt_path = os.path.join(settings.BASE_DIR, 'static/datasets/best.pt')
        best_yaml_path = os.path.join(settings.BASE_DIR, 'static/datasets/data.yaml')
        best_img_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')

        yolo_detector = yolo.CustomYOLO(best_yaml_path, best_pt_path)
        image_files = yolo_detector.predict(best_img_path)

        ctx = {"image_files": image_files, 'image_files_input': predict_folder_content()}
        return render(request, 'myapp/pages/yolo/load.html', ctx)
    
    return render(request, 'myapp/pages/yolo/load.html')

@csrf_exempt
def predictGanFace2Comic(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_url')
        input_folder_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')
        predict_folder_path = os.path.join(settings.BASE_DIR, 'static/image/predict')
        if os.path.exists(predict_folder_path):
            shutil.rmtree(predict_folder_path)
        if os.path.exists(input_folder_path):
            shutil.rmtree(input_folder_path)
        os.makedirs(input_folder_path, exist_ok=True)
        try:
            image_name = "gan_face2comic_upload.jpg"  
            image_path = os.path.join(input_folder_path, image_name) 
            header, data = image_data.split(',', 1)
            with open(image_path, 'wb') as f:
                f.write(base64.b64decode(data))
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        model = gan.Generator()
        model.load_weights(os.path.join(settings.BASE_DIR, 'static/datasets/gan_model_79_generator.h5'))
        generated_image_paths = []
        input_image_dir = os.path.join(settings.BASE_DIR, 'static/image/inputs')
        output_image_dir = os.path.join(settings.BASE_DIR, 'static/image/predict')
        os.makedirs(output_image_dir, exist_ok=True)
        
        image_files = [f for f in os.listdir(input_image_dir) if os.path.isfile(os.path.join(input_image_dir, f))]
        
        for input_image_file in image_files:
            input_image_path = os.path.join(input_image_dir, input_image_file)
            input_image = gan.load_one_image(input_image_path)
            input_image = gan.resize_one_image(input_image, 256, 256)
            input_image = gan.normalize_one_image(input_image)
            input_image = tf.expand_dims(input_image, axis=0)  # Add batch dimension
            newImage = gan.productImage(model, input_image)

            output_image_path = os.path.join(output_image_dir, generate_unique_filename())
            tf.keras.preprocessing.image.save_img(output_image_path, newImage[0])
            
            generated_image_paths.append(output_image_path)
        ctx = {"image_files": generated_image_paths, 'image_files_input': predict_folder_content()}
        return JsonResponse(ctx)
    return render(request, 'myapp/pages/gan/face2comic.html')

@csrf_exempt
def predictGanComic2Face(request):
    if request.method == 'POST':
        image_data = request.POST.get('image_url')
        input_folder_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')
        predict_folder_path = os.path.join(settings.BASE_DIR, 'static/image/predict')
        if os.path.exists(predict_folder_path):
            shutil.rmtree(predict_folder_path)
        if os.path.exists(input_folder_path):
            shutil.rmtree(input_folder_path)
        os.makedirs(input_folder_path, exist_ok=True)
        try:
            image_name = "gan_face2comic_upload.jpg"  
            image_path = os.path.join(input_folder_path, image_name) 
            header, data = image_data.split(',', 1)
            with open(image_path, 'wb') as f:
                f.write(base64.b64decode(data))
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        model = gan.Generator()
        model.load_weights(os.path.join(settings.BASE_DIR, 'static/datasets/comic2face.h5'))
        generated_image_paths = []
        input_image_dir = os.path.join(settings.BASE_DIR, 'static/image/inputs')
        output_image_dir = os.path.join(settings.BASE_DIR, 'static/image/predict')
        os.makedirs(output_image_dir, exist_ok=True)
        
        image_files = [f for f in os.listdir(input_image_dir) if os.path.isfile(os.path.join(input_image_dir, f))]
        
        for input_image_file in image_files:
            input_image_path = os.path.join(input_image_dir, input_image_file)
            input_image = gan.load_one_image(input_image_path)
            input_image = gan.resize_one_image(input_image, 256, 256)
            input_image = gan.normalize_one_image(input_image)
            input_image = tf.expand_dims(input_image, axis=0)  # Add batch dimension
            newImage = gan.productImage(model, input_image)

            output_image_path = os.path.join(output_image_dir, generate_unique_filename())
            tf.keras.preprocessing.image.save_img(output_image_path, newImage[0])
            
            generated_image_paths.append(output_image_path)
        ctx = {"image_files": generated_image_paths, 'image_files_input': predict_folder_content()}
        return JsonResponse(ctx)
    return render(request, 'myapp/pages/gan/comic2face.html')

    
