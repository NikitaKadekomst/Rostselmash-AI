from tkinter import ttk
import tkinter as tk
from gui.styles.config import Config

class Theme:
    # Цветовая схема
    COLORS = Config.COLORS

    # Шрифты
    FONTS = Config.FONTS

    @staticmethod
    def configure_styles():
        style = ttk.Style()
        
        # Настройка стиля для кнопок
        style.configure('TButton',
            background=Config.COLORS['primary'],
            foreground=Config.COLORS['text_light'],
            font=Config.FONTS['button'],
            padding=10
        )
        
        # Настройка стиля для меток
        style.configure('TLabel',
            background=Config.COLORS['light'],
            foreground=Config.COLORS['text'],
            font=Config.FONTS['body']
        )
        
        # Настройка стиля для фреймов
        style.configure('TFrame',
            background=Config.COLORS['light']
        )

    @staticmethod
    def create_rounded_button(parent, text, command, **kwargs):
        from gui.custom.ColoredButton import RoundedButton
        btn = RoundedButton(parent,
            text=text,
            command=command,
            padx=10,
            pady=10,
            **kwargs
        )
        return btn

    @staticmethod
    def create_title_label(parent, text):
        return tk.Label(parent,
            text=text,
            font=Config.FONTS['title'],
            bg=Config.COLORS['light'],
            fg=Config.COLORS['text']
        )

    @staticmethod
    def create_subtitle_label(parent, text):
        return tk.Label(parent,
            text=text,
            font=Config.FONTS['subtitle'],
            bg=Config.COLORS['light'],
            fg=Config.COLORS['text']
        ) 