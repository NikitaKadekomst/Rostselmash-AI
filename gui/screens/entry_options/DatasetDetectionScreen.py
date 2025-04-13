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
class DatasetDetectionScreen(ProgramScreen):
    def __init__(self, parent, controller):
        ProgramScreen.__init__(self, parent, controller)
        self.dataset_path = ''
        self.json_path = ''

        self.import_config = [
            ('Папка', 'dataset_to_detect_status', 'Датасет'),
            ('Папка', 'save_path_status', 'Папка'),
        ]

        # Настройка фона
        self.configure(bg=Theme.COLORS['light'])

        # Поле ввода пути к датасету
        self.path_to_detect_label = Theme.create_subtitle_label(self,
            "Путь к датасету для детекции"
        )
        self.path_to_detect_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        self.path_to_detect_import = Theme.create_rounded_button(self,
            "Выберите папку",
            self.process_detection_path
        )
        self.path_to_detect_import.place(relx=0.5, rely=0.3, anchor=CENTER)
        
        # Лейбл с информацией об импорте папки для детекции
        self.dataset_to_detect_status = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['text']
        )
        self.dataset_to_detect_status.place(relx=0.5, rely=0.38, anchor=CENTER)
        self.dataset_to_detect_status.config(text="Датасет: не задан")

        # Поле ввода пути для сохранения
        self.path_to_json_label = Theme.create_subtitle_label(self,
            "Путь для сохранения\nизображений с боксами"
        )
        self.path_to_json_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.path_to_json_import = Theme.create_rounded_button(self,
            "Выберите папку",
            self.process_json_path
        )
        self.path_to_json_import.place(relx=0.5, rely=0.62, anchor=CENTER)
        
        # Лейбл с информацией об импорте папки для сохранения
        self.save_path_status = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['text']
        )
        self.save_path_status.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.save_path_status.config(text="Папка: не задана")

        # Кнопка для запуска детекции
        self.start_image_detection_button = Theme.create_rounded_button(self,
            "Запуск детекции",
            self.start_dataset_detection
        )
        self.start_image_detection_button.place(relx=0.5, rely=0.85, anchor=CENTER)

        # Сообщение пользователю
        self.user_message = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['danger']
        )
        self.user_message.place(relx=0.05, rely=0.95, anchor=W)


    # DatasetDetectionScreen.start_image_detection()
    # ------------------------------------
    # Обработчик по нажатию на кнопку
    # "Запуск детекции изображения"
    # ------------------------------------
    def start_dataset_detection(self, *args):
        if self._validate_paths():
            prediction_instance = Predict(predict_path=self.json_path)
            prediction_instance.image_visualize_dataset(self.dataset_path)

    # DatasetDetectionScreen._validate_paths()
    # --------------------------------------------
    # Вспомогательный метод для валидации
    # переданных путей
    # --------------------------------------------
    def _validate_paths(self):
        if not self.dataset_path and not self.json_path:
            self.user_message.configure(text='Не указано изображение и папка для предсказания!')
            return False
        if not self.dataset_path:
            self.user_message.configure(text='Не указан путь к изображению!')
            return False
        if not self.json_path:
            self.user_message.configure(text='Не указан путь к папке для записи предсказания!')
            return False
        return True

    # DatasetDetectionScreen.process_detection_path()
    # --------------------------------------------------
    # Обработчик импорта файла с изображением
    # --------------------------------------------------
    def process_detection_path(self, *args):
        self.process_dir_path(self.__class__, 'dataset_path', 'Датасет')

    # DatasetDetectionScreen.process_json_path()
    # ---------------------------------------------
    # Обработчик импорта файла для предсказаний
    # ---------------------------------------------
    def process_json_path(self, *args):
        self.process_dir_path(self.__class__, 'json_path', 'Папка')



