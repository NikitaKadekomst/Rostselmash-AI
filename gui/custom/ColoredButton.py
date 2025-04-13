from tkinter import *
from utilities.constants import *
from gui.styles.config import Config
from PIL import Image, ImageDraw, ImageTk


# Класс интерфейса для кастомных кнопок управления.
# -------------------------------------------------
# Наследуется от класса Button модуля tkinter.
# -------------------------------------------------
class ColoredButton(Button):
    def __init__(self, parent, **kwargs):
        Button.__init__(self, parent, **kwargs)
        
        # Применяем стили из темы
        self.configure(
            bg=Config.COLORS['primary'],
            fg=Config.COLORS['text_light'],
            font=Config.FONTS['button'],
            relief='flat',
            padx=20,
            pady=10,
            cursor='hand2',
            borderwidth=0,
            highlightthickness=0
        )
        
        # Добавляем эффект при наведении
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        
    def _on_enter(self, e):
        self.configure(bg=Config.COLORS['accent'])
        
    def _on_leave(self, e):
        self.configure(bg=Config.COLORS['primary'])


class RoundedButton(Button):
    def __init__(self, parent, text, command=None, **kwargs):
        Button.__init__(self, parent, **kwargs)
        
        # Применяем стили из темы
        self.configure(
            text=text,
            command=command,
            bg=Config.COLORS['primary'],
            fg=Config.COLORS['text_light'],
            font=Config.FONTS['button'],
            relief='flat',
            padx=10,
            pady=10,
            cursor='hand2',
            borderwidth=0,
            highlightthickness=0
        )
        
        # Добавляем эффект при наведении
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        
    def _on_enter(self, e):
        self.configure(bg=Config.COLORS['accent'])
        
    def _on_leave(self, e):
        self.configure(bg=Config.COLORS['primary'])
