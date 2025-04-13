from roboflow import Roboflow
from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import json
from utilities.constants import API_TOKEN, PROJECT_ID, WORKSPACE_NAME, PROJECT_VERSION


# Класс Predict
# Генерация предсказаний по переданному списку исходных изображений.
class Predict:
    def __init__(self, path_to_dataset="", predict_path="", path_to_save=""):
        self.model = self._model_init()
        self.path_to_dataset = path_to_dataset
        self.predict_path = predict_path
        self.path_to_save = path_to_save

    # -----------------------------------------
    # Внутренний метод для инициализации модели
    # -----------------------------------------
    @staticmethod
    def _model_init():
        rf = Roboflow(API_TOKEN)
        project = rf.workspace(WORKSPACE_NAME).project(PROJECT_ID)
        version = project.version(PROJECT_VERSION)
        return version.model

    # -----------------------------------------
    # Предсказание модели для изображения file
    # с расширением ext в формате JSON
    # -----------------------------------------
    def image_generate_image_json(self, file, path_to_save):
        filename = os.fsdecode(file)
        path_to_save = os.fsdecode(path_to_save)
        image_name, extension = os.path.splitext(os.path.basename(filename))
        path_to_save = f"{path_to_save}/{image_name}.json"
        prediction_json = self.model.predict(filename, confidence=40, overlap=30).json()
        self.save_json(path_to_save, prediction_json)
        print(f"Предсказание по изображению {image_name}{extension} успешно сохранено в файл {path_to_save}!")

    # -----------------------------------------
    # Предсказание модели для изображения file
    # с расширением ext в формате JSON
    # -----------------------------------------
    def image_generate_dataset_json(self, dataset_path, path_to_save):
        dataset_filename = os.fsdecode(dataset_path)
        save_path = os.fsdecode(path_to_save)
        
        if os.path.exists(save_path):
            for file in os.listdir(save_path):
                file_path = os.path.join(save_path, file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    print(f"Ошибка при удалении файла {file_path}: {e}")
        
        image_paths = [os.path.join(dataset_filename, filename) for filename in os.listdir(dataset_filename)]
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.image_generate_image_json, image_path, path_to_save)
                       for image_path in image_paths]
            for future in as_completed(futures):
                future.result()
        print(f"Предсказания по датасету успешно сгенерированы и сохранены!")

    # -----------------------------------------
    # Визуализация моделью предсказания для
    # изображения filename расширением ext
    # ---------------------------------------
    def image_visualize_prediction(self, file, ext=".jpg"):
        filename = os.fsdecode(file)
        image_name, extension = os.path.splitext(os.path.basename(filename))
        path_to_save = f"{self.predict_path}/{image_name}_processed.{ext}"
        self.model.predict(filename, confidence=40, overlap=30).save(path_to_save)
        print(f"Изображение {image_name}{extension} с предсказанными боксами успешно сохранено!")

    # -----------------------------------------------
    # Расширение метода image_visualize_prediction
    # для детекции всех изображений в заданной папке
    # -----------------------------------------------
    def image_visualize_dataset(self, dataset_path, ext='.jpg'):
        dataset_filename = os.fsdecode(dataset_path)
        image_paths = [os.path.join(dataset_filename, filename) for filename in os.listdir(dataset_filename)]
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(self.image_visualize_prediction, image_path, ext) for image_path in image_paths]
            for future in as_completed(futures):
                future.result()
        print("Детекция по датасету успешно завершена!")

    # --------------------------------
    # Вывод JSON в указанный файл
    # --------------------------------
    @staticmethod
    def save_json(path, content):
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Ошибка записи файла {path}: {str(e)}")
            raise

    # --------------------------------
    # Вывод JSON в читабельном формате
    # --------------------------------
    @staticmethod
    def print_pretty_json(json_obj):
        print(json.dumps(json_obj, indent=2))
