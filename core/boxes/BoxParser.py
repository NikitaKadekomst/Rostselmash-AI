import json
import numpy as np
from utilities.constants import *
from core.image.CheckImage import CheckImage
import cv2
import os
from PIL import Image

class BoxParser:
    def __init__(self, image_path, gt_path, pred_path):
        self.image_path = image_path
        self.gt_path = gt_path
        self.pred_path = pred_path
        
        # Создаем абсолютный путь к папке логов
        log_dir = os.path.join('C:', 'Own', 'University', 'DonStu', 'VMO', '6', 'WorkingInternship', 'Project', 'dataset', 'test_pred')
        self.log_file = os.path.join(log_dir, 'boxes_log.txt')
        
        # Создаем папку, если она не существует
        try:
            os.makedirs(log_dir, exist_ok=True)
            print(f"Папка для логов создана: {log_dir}")
        except Exception as e:
            print(f"Ошибка при создании папки для логов: {str(e)}")

        if not os.path.exists(self.gt_path):
            raise FileNotFoundError(f"Файл {self.gt_path} не найден.")
        if not os.path.exists(self.pred_path):
            raise FileNotFoundError(f"Файл {self.pred_path} не найден.")

        self.img_width, self.img_height = self._get_image_size()

    def _log_boxes(self, message):
        try:
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"{message}\n")
            print(f"Запись в лог успешна: {self.log_file}")
        except Exception as e:
            print(f"Ошибка при записи в лог: {str(e)}")
            print(f"Путь к лог-файлу: {self.log_file}")

    # Получение размеров текущего изображения
    def _get_image_size(self):
        if CheckImage(self.image_path):
            try:
                with Image.open(self.image_path) as img:
                    width, height = img.size
                    return width, height
            except FileNotFoundError:
                print(f"Ошибка: Файл '{self.image_path}' не найден.")
            except Exception as e:
                print(f"Ошибка при чтении файла: {e}")

    # Подготовка боксов ground truth
    def prepare_ground_truth_boxes(self):
        boxes = {}
        try:
            self._log_boxes(f"\n=== Ground Truth Boxes for {os.path.basename(self.image_path)} ===")
            with open(self.gt_path, 'r', encoding='utf-8') as gt:
                for line in gt:
                    parts = line.strip().split()
                    if len(parts) != 5:
                        continue
                    cls, cx, cy, w, h = parts
                    cx, cy, w, h = map(float, (cx, cy, w, h))

                    if cls == '0':
                        cls = 'plants'

                    x = cx * self.img_width
                    y = cy * self.img_height
                    width = w * self.img_width
                    height = h * self.img_height

                    x0 = x - width / 2
                    y0 = y - height / 2
                    x1 = x + width / 2
                    y1 = y + height / 2

                    if cls not in boxes:
                        boxes[cls] = []
                    boxes[cls].append((x0, y0, x1, y1, 1.0))  # confidence=1 для GT
                    
                    log_message = f"Ground Truth: class={cls}, box=({x0:.2f}, {y0:.2f}, {x1:.2f}, {y1:.2f})"
                    print(log_message)
                    self._log_boxes(log_message)
        except Exception as e:
            error_message = f"Ошибка при чтении ground truth: {str(e)}"
            print(error_message)
            self._log_boxes(error_message)
            return None

        return boxes

    # Подготовка предсказанных боксов
    def prepare_prediction_boxes(self):
        boxes = {}
        try:
            self._log_boxes(f"\n=== Prediction Boxes for {os.path.basename(self.image_path)} ===")
            with open(self.pred_path, 'r', encoding='utf-8') as pred:
                data = json.load(pred)
                
                # Выводим информацию о структуре данных
                print(f"JSON data type: {type(data)}")
                if isinstance(data, dict):
                    print(f"JSON keys: {data.keys()}")
                    if 'predictions' in data:
                        print(f"Number of predictions: {len(data['predictions'])}")
                        if len(data['predictions']) > 0:
                            print(f"First prediction: {data['predictions'][0]}")
                
                # Проверяем формат данных
                if isinstance(data, dict) and 'predictions' in data:
                    predictions = data['predictions']
                    for box in predictions:
                        if isinstance(box, dict):
                            cls = str(box.get('class', '0'))
                            if cls == '0':
                                cls = 'plants'
                            
                            # Получаем координаты в формате (x, y, width, height)
                            x = float(box.get('x', 0))
                            y = float(box.get('y', 0))
                            width = float(box.get('width', 0))
                            height = float(box.get('height', 0))
                            
                            # Преобразуем в формат (x0, y0, x1, y1)
                            x0 = x
                            y0 = y
                            x1 = x + width
                            y1 = y + height
                            
                            conf = float(box.get('confidence', 0.0))
                            
                            if cls not in boxes:
                                boxes[cls] = []
                            boxes[cls].append((x0, y0, x1, y1, conf))
                            
                            log_message = f"Prediction: class={cls}, box=({x0:.2f}, {y0:.2f}, {x1:.2f}, {y1:.2f}), confidence={conf:.4f}"
                            print(log_message)
                            self._log_boxes(log_message)
                else:
                    print(f"Неподдерживаемый формат JSON: {type(data)}")
                    return None
                    
        except Exception as e:
            error_message = f"Ошибка при чтении предсказаний: {str(e)}"
            print(error_message)
            self._log_boxes(error_message)
            return None

        return boxes

    # Получение JSON и заданного файла
    def _get_json(self):
        with open(self.pred_path, "r", encoding="utf-8") as f:
            return json.load(f)