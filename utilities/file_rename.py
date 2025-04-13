import os

def rename_files_in_folder(folder_path):
    # Перебираем все файлы в заданной папке
    for filename in os.listdir(folder_path):
        # Проверяем, что файл имеет нужный формат
        old_filename = os.path.join(folder_path, filename)
        new_filename = os.path.join(folder_path, filename.replace(" .txt", '.txt'))
        os.rename(old_filename, new_filename)
        # if ".rf." in filename:
        #     # Разделяем имя файла на части
        #     parts = filename.split(".rf.")
        #     if len(parts) == 2:
        #         # Формируем новое имя файла
        #         new_filename = parts[0] + ".jpg"
        #         # Получаем полный путь к старому и новому файлу
        #         old_file = os.path.join(folder_path, filename)
        #         new_file = os.path.join(folder_path, new_filename)
        #         # Переименовываем файл
        #         os.rename(old_file, new_file)
        #         print(f'Renamed: {filename} -> {new_filename}')

# Укажите путь к папке с файлами
folder_path = "/Project/dataset/images/Rostselmash-1/whole/labels"
rename_files_in_folder(folder_path)