import tkinter as tk

class Input(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        # Привязка событий к горячим клавишам
        self.bind("<Control-v>", self.paste_text)
        self.bind("<Command-v>", self.paste_text)
        self.bind("<Control-c>", self.copy_text)
        self.bind("<Command-c>", self.copy_text)
        self.bind("<Control-x>", self.cut_text)
        self.bind("<Command-x>", self.cut_text)

    # Вставка текста в поле
    def paste_text(self, event=None):
        try:
            clipboard_text = self.clipboard_get()
            self.insert(tk.INSERT, clipboard_text)
        except tk.TclError:
            pass

    # Копирование текста из поля
    def copy_text(self, event=None):
        selected_text = self.selection_get()
        self.clipboard_clear()
        self.clipboard_append(selected_text)

    # Вырезание текста из поля
    def cut_text(self, event=None):
        self.copy_text()
        self.delete("sel.first", "sel.last")

    def clear_text(self):
        self.delete(0, tk.END)
