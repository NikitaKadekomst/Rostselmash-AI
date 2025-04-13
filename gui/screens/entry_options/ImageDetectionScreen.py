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
class ImageDetectionScreen(ProgramScreen):
    def __init__(self, parent, controller):
        ProgramScreen.__init__(self, parent, controller)
        self.image_path = ''
        self.box_path = ''

        self.import_config = [
            ('Файл', 'image_file_status', 'Изображение'),
            ('Файл', 'detected_file_status', 'Папка'),
        ]

        # Настройка фона
        self.configure(bg=Theme.COLORS['light'])

        # Поле ввода пути к изображению
        self.path_to_detect_label = Theme.create_subtitle_label(self,
            "Путь к изображению"
        )
        self.path_to_detect_label.place(relx=0.5, rely=0.2, anchor=CENTER)
        
        self.path_to_detect_import = Theme.create_rounded_button(self,
            "Выберите файл",
            self.process_detection_path
        )
        self.path_to_detect_import.place(relx=0.5, rely=0.3, anchor=CENTER)
        
        # Лейбл с информацией об импорте изображения
        self.image_file_status = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['text']
        )
        self.image_file_status.place(relx=0.5, rely=0.38, anchor=CENTER)
        self.image_file_status.config(text="Изображение: не задано")

        # Поле ввода пути для сохранения
        self.path_to_detected_label = Theme.create_subtitle_label(self,
            "Путь для сохранения\nизображения с боксами"
        )
        self.path_to_detected_label.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.path_to_detected_import = Theme.create_rounded_button(self,
            "Выберите файл",
            self.process_box_path
        )
        self.path_to_detected_import.place(relx=0.5, rely=0.62, anchor=CENTER)
        
        # Лейбл с информацией об импорте папки для сохранения
        self.detected_file_status = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['text']
        )
        self.detected_file_status.place(relx=0.5, rely=0.7, anchor=CENTER)
        self.detected_file_status.config(text="Папка: не задана")

        # Кнопка для запуска детекции
        self.start_image_detection_button = Theme.create_rounded_button(self,
            "Запуск детекции",
            self.start_image_detection
        )
        self.start_image_detection_button.place(relx=0.5, rely=0.85, anchor=CENTER)

        # Сообщение пользователю
        self.user_message = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['danger']
        )
        self.user_message.place(relx=0.05, rely=0.95, anchor=W)


    # ImageDetectionScreen.start_image_detection()
    # ------------------------------------
    # Обработчик по нажатию на кнопку
    # "Запуск детекции изображения"
    # ------------------------------------
    def start_image_detection(self, *args):
        if self._validate_paths():
            if (not self.image_path.endswith('.jpg') and
                    not self.image_path.endswith('.jpeg') and
                    not self.image_path.endswith('.png')):
                self.user_message.configure(text="Путь должен быть к изображению .jpg/.jpeg или .png!", fg="red")
                return

            prediction_instance = Predict(predict_path=self.box_path)
            prediction_instance.image_visualize_prediction(self.image_path)

    # ImageDetectionScreen._validate_paths()
    # --------------------------------------------
    # Вспомогательный метод для валидации
    # переданных путей
    # --------------------------------------------
    def _validate_paths(self):
        if not self.image_path and not self.box_path:
            self.user_message.configure(text='Не указано изображение и папка для предсказания!')
            return False
        if not self.image_path:
            self.user_message.configure(text='Не указан путь к изображению!')
            return False
        if not self.box_path:
            self.user_message.configure(text='Не указан путь к папке для записи предсказания!')
            return False
        return True

    # ImageDetectionScreen.process_detection_file()
    # ----------------------------------------
    # Обработчик импорта файла с изображением
    # ----------------------------------------
    def process_detection_path(self, *args):
        self.process_image_path(self.__class__, 'image_path', 'Изображение')

    # ImageDetectionScreen.process_json_file()
    # --------------------------------------------
    # Обработчик пути, куда сохранять изображение
    # с предсказанными боксами
    # --------------------------------------------
    def process_box_path(self, *args):
        self.process_dir_path(self.__class__, 'box_path', 'Папка')


