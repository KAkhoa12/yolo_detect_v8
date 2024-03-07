from django.shortcuts import render,redirect
# from .models import library
import shutil
from cloudinary.uploader import upload
# from .forms import PictureForm
from cloudinary.api import resources
from cloudinary.forms import cl_init_js_callbacks
from ultralytics import YOLO
from django.conf import settings
import os
def index(request):
    # cloudinary_folder = 'YOLO_Detect/'
    # images_info = resources(type='upload', prefix=cloudinary_folder)


    # images = [
    #     {
    #         'public_id': image['public_id'],
    #         'url': image['url'],
    #     }
    #     for image in images_info['resources']
    # ]

    # ctx = {'pictures': images}
    return render(request, 'myapp/index.html')

def loadImage(request):
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

        return render(request, 'myapp/load.html', context={'image_files_input': predict_folder_content()})
    return render(request, 'myapp/load.html')



def predict_folder_content():
    input_folder_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')
    return [f for f in os.listdir(input_folder_path) if os.path.isfile(os.path.join(input_folder_path, f))]


def predict_image_view(request):
    if request.method == 'POST':
        result = predictImage()
        ctx = {"image_files":result,'image_files_input': predict_folder_content()}
        return render(request, 'myapp/load.html',ctx)
    return render(request, 'myapp/load.html')

def predictImage():
    predict_folder_path = os.path.join(settings.BASE_DIR, 'static/image/predict')
    best_pt_path = os.path.join(settings.BASE_DIR, 'static/datasets/best.pt')
    best_yaml_path = os.path.join(settings.BASE_DIR, 'static/datasets/data.yaml')
    best_img_path = os.path.join(settings.BASE_DIR, 'static/image/inputs')
    if os.path.exists(predict_folder_path):
        shutil.rmtree(predict_folder_path)
    model = YOLO(best_pt_path,best_yaml_path)
    model.predict(save=True,source=best_img_path,project="static/image",name="predict")
    image_files = [f for f in os.listdir(predict_folder_path) if os.path.isfile(os.path.join(predict_folder_path, f))]

  
    return image_files
    

