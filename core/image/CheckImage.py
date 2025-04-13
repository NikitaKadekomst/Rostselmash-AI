from PIL import Image
import cv2
import numpy as np
from utilities.constants import *
import os

class CheckImage:
    def __init__(self, image_path):
        self.image_path = image_path

    def check_all_errors(self):
        self.check_if_exists()
        self.check_permission()
        self.check_integrity()
        self.check_cv2_read()
        print(f"Изображение {self.image_path} открыто корректно!")
        return True

    def check_if_exists(self):
        # Проверка существования файла
        if not os.path.exists(self.image_path):
            raise FileNotFoundError(f"Файл {self.image_path} не существует.")

    def check_permission(self):
        # Проверка прав доступа
        if not os.access(self.image_path, os.R_OK):
            raise PermissionError(f"Нет прав на чтение файла {self.image_path}.")

    def check_integrity(self):
        try:
            img = Image.open(self.image_path)
            img.verify()  # Проверка целостности
        except Exception as e:
            print(f"Файл поврежден: {e}")

    def check_cv2_read(self):
        # Попытка чтения
        image = cv2.imread(self.image_path)
        if image is None:
            raise ValueError(
                f"OpenCV не смог прочитать файл {self.image_path} (возможно, битый или неподдерживаемый формат).")


