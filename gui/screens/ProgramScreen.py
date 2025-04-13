# Модуль интерфейса.
from tkinter import *
from tkinter import filedialog as fd
from gui.styles.theme import Theme

# Начальное окно приложение с выбором опций для работы.
# -----------------------------------------------------
# Наследуется от класса окна Frame библиотеки tkinter
# -----------------------------------------------------
class ProgramScreen(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        # ---------------------------
        #   ОСНОВНОЙ ЗАГОЛОВОК
        # */--------------------------
        self.main_label = Theme.create_title_label(self,
            "Приложение для распознавания\nрастений на поле с помощью ИИ"
        )
        self.main_label.place(relx=0.5, rely=0.1, anchor=CENTER)

        # Кнопка для возвращения на предыдущий экран интерфейса
        self.canvas = Canvas(self, width=20, height=20, cursor="hand2")
        self.canvas.place(anchor=CENTER, relx=0.06, rely=0.07)
        self.backup_img = PhotoImage(file="images/backup-arrow.png")
        self.canvas.create_image(0, 0, anchor=NW, image=self.backup_img)
        self.canvas.bind("<Button-1>", lambda event: self.controller.back(self.__class__))

    # ProgramScreen.process_dir_path()
    # --------------------------------------------
    # Обработчик пути импортируемого изображения
    # --------------------------------------------
    def process_image_path(self, screen_class, status_prop, filetype):
        filetypes = (
            ('JPEG Images', '*.jpg'),
            ('JPEG Images', '*.jpeg'),
            ('PNG Images', '*.png'),
            ('All files', '*.*')
        )
        path = fd.askopenfilename(
            title='',
            initialdir='/',
            filetypes=filetypes)

        screen = self.controller.get_screen(screen_class)
        if screen:
            setattr(screen, status_prop, path)
            self.set_entry_status(screen, path, filetype)

        return path

    # ProgramScreen.process_dir_path()
    # --------------------------------------------------------
    # Обработчик пути импортируемой папки
    # --------------------------------------------------------
    def process_dir_path(self, screen_class, status_prop, filetype):
        path = fd.askdirectory(
            title='',
            initialdir='/'
        )

        # Если передан сам экран, используем его
        if isinstance(screen_class, ProgramScreen):
            screen = screen_class
        else:
            # Иначе получаем экран из контроллера
            screen = self.controller.get_screen(screen_class)

        if screen and path:
            setattr(screen, status_prop, path)
            self.set_entry_status(screen, path, filetype)

        return path

    # ProgramScreen.set_entry_status()
    # ------------------------------------------
    # Вспомогательный метод для вывода сообщений
    # о статусе импортированного файла
    # ------------------------------------------
    @staticmethod
    def set_entry_status(screen, path, filetype):
        filename = path.split("/")[-1]

        for import_type, prop, ftp in getattr(screen, 'import_config'):
            # Проверяем, что тип файла (ftp) соответствует переданному filetype
            if filetype == ftp:
                # Для папок показываем просто "Папка: имя_папки"
                if import_type == 'Папка':
                    file_status = f'Папка: {filename if filename else "не задана"}'
                # Для файлов показываем тип файла и его имя
                else:
                    file_status = f'{ftp}: {filename if filename else "не задан"}'
                
                if len(file_status) > 30:
                    file_status = file_status[:30] + '...'
                getattr(screen, prop).config(text=file_status)
                if file_status != f"{ftp}: не задан":
                    getattr(screen, 'user_message').configure(text="")
