from core.prediction.Predict import Predict

import matplotlib.colors as mcolors
from gui.screens.ProgramScreen import *
from gui.custom.ColoredButton import *
from utilities.constants import *
from gui.styles.theme import Theme

from tkinter import ttk
from tkinter import filedialog as fd
from gui.screens.entry_options.ImageDetectionScreen import ImageDetectionScreen as ImageDetectionScreenCLS
from gui.screens.entry_options.DatasetDetectionScreen import DatasetDetectionScreen as DatasetDetectionScreenCLS
from gui.screens.entry_options.DatasetPredictionScreen import DatasetPredictionScreen as DatasetPredictionScreenCLS


# Класс интерфейса настроек аппроксимации.
class EntryScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self._entries_data = ""
        self._current_file = ""
        self.current_file_label = ""

        # Настройка фона
        self.configure(bg=Theme.COLORS['light'])

        # Заголовок
        self.main_label = Theme.create_title_label(self,
            "Приложение для распознавания\nрастений на поле с помощью ИИ"
        )
        self.main_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Кнопки опций
        self.start_image_detection_button = Theme.create_rounded_button(self,
            "Запуск детекции изображения",
            lambda: self.show_option(ImageDetectionScreenCLS),
            width=30
        )
        self.start_image_detection_button.place(relx=0.5, rely=0.3, anchor=CENTER)
        
        self.start_dataset_detection_button = Theme.create_rounded_button(self,
            "Запуск детекции по датасету",
            lambda: self.show_option(DatasetDetectionScreenCLS),
            width=30
        )
        self.start_dataset_detection_button.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        self.start_dataset_prediction = Theme.create_rounded_button(self,
            "Генерация предсказаний по датасету",
            lambda: self.show_option(DatasetPredictionScreenCLS),
            width=30
        )
        self.start_dataset_prediction.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Сообщение пользователю
        self.user_message = Label(self,
            font=Theme.FONTS['body'],
            bg=Theme.COLORS['light'],
            fg=Theme.COLORS['danger']
        )
        self.user_message.place(relx=0.05, rely=0.93, anchor=W)

    # EntryScreen.show_image_detection_screen()
    # ---------------------------------------------
    # Обработчик для открытия экрана с
    # соответствующей опцией
    # ---------------------------------------------
    def show_option(self, option_cls, *args):
        self.controller.show_frame(option_cls)

    # EntryScreen.hide_entries()
    # ---------------------------------------------
    # Метод для сокрытия полей экрана
    # ---------------------------------------------
    def hide_entries(self):
        pass

    # EntryScreen.show_entries()
    # ---------------------------------------------
    # Метод для отображения полей экрана
    # ---------------------------------------------
    def show_entries(self):
        pass

