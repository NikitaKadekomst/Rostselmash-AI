from core.prediction.Predict import Predict

import matplotlib.colors as mcolors
from gui.screens.ProgramScreen import *
from gui.custom.ColoredButton import *
from gui.custom.Input import *
from utilities.constants import *
from gui.styles.theme import Theme

from tkinter import ttk
from tkinter import filedialog as fd
import os


# Интерфейсный экран для запуска детекции по изображению.
class DatasetPredictionScreen(ProgramScreen):
    def __init__(self, parent, controller):
        ProgramScreen.__init__(self, parent, controller)
        self.import_config = [
            ('Папка', 'image_file_status', 'Датасет'),
            ('Папка', 'json_file_status', 'Папка'),
        ]

        self.dataset_path = ''
        self.json_path = ''

        # Настройка фона
        self.configure(bg=Theme.COLORS['light'])

        # Поле ввода пути к датасету
        self.path_to_dataset_label = Theme.create_subtitle_label(self,
            "Путь к датасету для детекции"
        )
        self.path_to_dataset_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        self.path_to_dataset_import = Theme.create_rounded_button(self,
            "Выберите папку",
            self.process_detection_path
        )
        self.path_to_dataset_import.place(relx=0.5, rely=0.3, anchor=CENTER)
        
        self.image_file_status = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['text']
        )
        self.image_file_status.place(relx=0.5, rely=0.38, anchor=CENTER)
        self.image_file_status.config(text="Датасет: не задан")

        # Поле ввода пути для сохранения
        self.path_to_json_label = Theme.create_subtitle_label(self,
            "Путь для сохранения\nпредсказаний в JSON"
        )
        self.path_to_json_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.path_to_json_export = Theme.create_rounded_button(self,
            "Выберите папку",
            self.process_json_path
        )
        self.path_to_json_export.place(relx=0.5, rely=0.62, anchor=CENTER)
        
        self.json_file_status = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['text']
        )
        self.json_file_status.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.json_file_status.config(text="Папка: не задана")

        # Кнопка для запуска генерации
        self.start_image_detection_button = Theme.create_rounded_button(self,
            "Запустить генерацию",
            self.start_dataset_prediction
        )
        self.start_image_detection_button.place(relx=0.5, rely=0.85, anchor=CENTER)

        # Сообщение пользователю
        self.user_message = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['danger']
        )
        self.user_message.place(relx=0.05, rely=0.95, anchor=W)


    # EntryScreen.start_image_detection()
    # ------------------------------------
    # Обработчик по нажатию на кнопку
    # "Запуск детекции изображения"
    # ------------------------------------
    def start_dataset_prediction(self, *args):
        extension = ''
        dataset_path = os.fsencode(self.dataset_path)
        json_path = os.fsencode(self.json_path)

        if not dataset_path and not json_path:
            self.user_message.configure(text="Пути к датасету или папке сохранения\nнекорректны или не заданы!")
            return
        if not dataset_path and json_path:
            self.user_message.configure(text="Путь к датасету некорректен\nили не задан!")
            return
        if dataset_path and not json_path:
            self.user_message.configure(text="Путь к папке сохранения\nнекорректен или не задан!")
            return

        prediction_instance = Predict()
        prediction_instance.image_generate_dataset_json(dataset_path, json_path)

    # DatasetPredictionScreen.process_detection_path()
    # -----------------------------------------------------
    # Обработчик импорта файла с изображением
    # -----------------------------------------------------
    def process_detection_path(self, *args):
        self.process_dir_path(self.__class__, 'dataset_path', 'Датасет')

    # DatasetPredictionScreen.process_json_path()
    # ------------------------------------------------
    # Обработчик импорта файла для предсказаний
    # ------------------------------------------------
    def process_json_path(self, *args):
        self.process_dir_path(self.__class__, 'json_path', 'Папка')


