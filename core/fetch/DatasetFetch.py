import roboflow
import requests
import json
import os
from concurrent.futures import ThreadPoolExecutor
from utilities.constants import API_TOKEN, PROJECT_ID, BASE_FOLDER

# Получение информации в JSON обо всех изображениях в датасете
class DatasetFetch:
    def __init__(self, api_token, workspace, project_id, base_folder):
        self.rf = roboflow.Roboflow()
        self.workspace = workspace
        self.project_id = project_id
        self.project = self.rf.project(self.project_id)
        self.api_key = api_token
        self.base_folder = base_folder

    # -------------------------------------
    # Исполнение запроса на получение JSON.
    # -------------------------------------
    @staticmethod
    def get_json(url):
        r = requests.get(url)
        return json.dumps(r.json(), indent=4)

    # --------------------------------------------
    # Запись полученного JSON в файл JSON-формата.
    # --------------------------------------------
    @staticmethod
    def write_to_json(directory, j):
        d = json.loads(j)
        image_name = d['image']['name']
        if not os.path.exists(os.path.join(os.getcwd(), directory)):
            path = os.path.join(os.getcwd(), directory)
            os.mkdir(path)
        with open(f'{directory}/{image_name}.json', 'w', encoding='utf-8') as file:
            file.write(j)

    # ----------------------
    # Удобный вывод словаря
    # ----------------------
    @staticmethod
    def pretty_dict(dic):
        for key, val in dic.items():
            print(f"{key}: {val}")

    # ---------------------
    # Получение ID картинок
    # ---------------------
    def get_images_ids(self):
        records = []

        for page in self.search_all(
            offset=0,
            limit=100,
            class_name="plants",
            in_dataset=True,
            fields=["id", "name"],
        ):
            records.extend(page)

        return [{"id": record["id"], "name": record["name"]} for record in records]

    # ----------------------------------------------
    # Формирование эндпоинта для выполнения запроса.
    # ----------------------------------------------
    def create_url(self, image_id):
        base_url = "https://api.roboflow.com"
        return f'{base_url}/{self.workspace}/{self.project_id}/images/{image_id}?api_key={self.api_key}'

    # -----------------------------------------------
    # Процедура для получения информации о картинках.
    # -----------------------------------------------
    def get_images_json(self, data, directory):
        img_id = data["id"]
        url = self.create_url(img_id)
        js = self.get_json(url)
        d = json.loads(js)
        image_name = d['image']['name']
        self.write_to_json(directory, js)
        print(f"Информации об изображении {image_name}.jpg получена!")

    # -----------------------------------------
    # Параллельные запросы к Roboflow REST API.
    # -----------------------------------------
    def get_json_parallel(self):
        data = self.get_images_ids()
        with ThreadPoolExecutor() as executor:
            results = list(executor.map(lambda b: self.get_images_json(b, self.base_folder), data))
        return results

# Пример запуска.
fetch = DatasetFetch(API_TOKEN, WORKSPACE, PROJECT_ID, BASE_FOLDER)
fetch.get_json_parallel()