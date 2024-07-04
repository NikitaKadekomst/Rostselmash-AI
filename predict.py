from roboflow import Roboflow
import os
import json

# Инициализация модели.
rf = Roboflow(api_key="GWPLfbanlFRrU2iDQm6w")
project = rf.workspace("rostselmash").project("rostselmash")
version = project.version(1)
model = version.model


# Метод для скармливания тестовых данных модели (визуализация результата)
def dataset_predict_visualize(path_to_dataset, predict_path, path_to_save):
    for file in os.listdir(path_to_dataset):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            model.predict(f"{predict_path}{filename}", confidence=40, overlap=30).save(
                f"{path_to_save}/{filename}_processed.jpg")
            continue
        if filename.endswith(".png"):
            model.predict(f"{predict_path}{filename}", confidence=40, overlap=30).save(
                f"{path_to_save}/{filename}_processed.jpg")
            continue
        else:
            continue


# Метод для скармливания тестовых данных модели (запись информации в JSON)
def dataset_predict_json(path_to_dataset, predict_path, path_to_save):
    for file in os.listdir(path_to_dataset):
        filename = os.fsdecode(file)
        if filename.endswith(".jpg"):
            f = open(f"{path_to_save}{filename}.txt", "w+")
            f.write(json.dumps(model.predict(f"{predict_path}{filename}", confidence=50, overlap=20).json(), indent=2))
            continue
        if filename.endswith(".png"):
            f = open(f"{path_to_save}{filename}.txt", "w+")
            f.write(json.dumps(model.predict(f"{predict_path}{filename}", confidence=50, overlap=20).json(), indent=2))
            continue
        else:
            continue


# Вывод JSON в читабельном формате
def print_pretty_json(json_obj):
    print(json.dumps(json_obj, indent=2))


# Запуск
p_dataset = "C:/Own/University/ДГТУ/ВМО/6 семестр/Производственная практика/Проект/dataset/one_hundred_images/"
p_predict = "dataset/one_hundred_images/"
p_to_save = "dataset/dataset_processed_json/"
