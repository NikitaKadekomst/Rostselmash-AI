from tkinter import *

# Экраны приложения.
from gui.screens.EntryScreen import EntryScreen as EntryScreenCLS
from gui.screens.entry_options.ImageDetectionScreen import ImageDetectionScreen as ImageDetectionScreenCLS
from gui.screens.entry_options.DatasetDetectionScreen import DatasetDetectionScreen as DatasetDetectionScreenCLS
from gui.screens.entry_options.DatasetPredictionScreen import DatasetPredictionScreen as DatasetPredictionScreenCLS
from gui.styles.theme import Theme

# Основной класс интерфейса.
# ------------------------------------------------------
# Входная точка в интерфейс.
# Управляет сменой экранов в приложении.
# Наследуется от основного класса Tk библиотеки tkinter.
# ------------------------------------------------------
class GUI(Tk):
    def __init__(self, width, height, bg):
        Tk.__init__(self)
        
        # Сохраняем размеры окна как атрибуты
        self.width = width
        self.height = height
        
        # Настройка темы
        Theme.configure_styles()
        
        # Настройка окна
        self.title("Распознавание растений на поле")
        self.geometry(f"{width}x{height}")
        self.configure(bg=Theme.COLORS['light'])
        
        # Создание контейнера для фреймов
        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        # Словарь для хранения фреймов
        self.frames = {}
        
        # Создание и добавление фреймов
        for F in (EntryScreenCLS, ImageDetectionScreenCLS, DatasetDetectionScreenCLS, 
                 DatasetPredictionScreenCLS):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Показ начального фрейма
        self.show_frame(EntryScreenCLS)

    # GUI.show_frame(cont)
    # --------------------------------------------
    # Отображение заданной страницы интерфейса.
    # -----------------------------------------------
    # АРГУМЕНТЫ
    # --cont = имя класса страницы.
    # -----------------------------------------------
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # GUI.back(current_frame)
    # --------------------------------------------
    # Обработчик нажатия на кнопку возвращения
    # на предыдущий экран интерфейса
    # --------------------------------------------
    # АРГУМЕНТЫ
    # --current_frame = текущий экран.
    # --------------------------------------------
    def back(self, current_frame):
        self.show_frame(EntryScreenCLS)

    # GUI.get_screen(current_frame)
    # --------------------------------------------
    # Получение экземпляра экрана по его классу
    # --------------------------------------------
    # АРГУМЕНТЫ
    # --screen_class = класс экрана.
    # --------------------------------------------
    def get_screen(self, screen_class):
        return self.frames.get(screen_class)

    # Запуск интерфейса.
    # ------------------------------------------------
    # Запускает весь интерфейс в основном классе Main
    # ------------------------------------------------
    def run(self):
        self.mainloop()
