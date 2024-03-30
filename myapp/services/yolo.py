import os
import shutil
from ultralytics import YOLO
from django.conf import settings

class CustomYOLO():
    def __init__(self, yaml_path, model_path):
        self.model = YOLO(model_path, yaml_path)

    def predict(self, best_img_path):
        # Tạo thư mục 'predict' nếu nó không tồn tại
        predict_folder_path = os.path.join(os.path.dirname(best_img_path), "predict")
        if os.path.exists(predict_folder_path):
            shutil.rmtree(predict_folder_path)
        
        # Thực hiện dự đoán với model đã khởi tạo
        self.model.predict(save=True,source=best_img_path, project="static/image", name="predict")

        # Trả về danh sách các tệp hình ảnh đã dự đoán
        image_files = [f for f in os.listdir(predict_folder_path) if os.path.isfile(os.path.join(predict_folder_path, f))]
        return image_files
