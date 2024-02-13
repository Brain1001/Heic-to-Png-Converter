import os
import pyheif
from PIL import Image

def convert_heic_to_png(source_folder, target_folder):
    # Проверяем, существует ли целевая папка, и создаем ее, если нет
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # Перебор всех файлов в исходной папке
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(".heic"):
            # Построение полного пути к файлу исходного изображения
            heic_path = os.path.join(source_folder, filename)
            # Создание пути для сохранения конвертированного файла
            png_path = os.path.join(target_folder, filename[:-5] + ".png")

            try:
                # Чтение HEIC файла
                heif_file = pyheif.read(heic_path)
                
                # Преобразование в изображение Pillow
                image = Image.frombytes(
                    heif_file.mode, 
                    heif_file.size, 
                    heif_file.data,
                    "raw",
                    heif_file.mode,
                    heif_file.stride,
                )
                
                # Сохранение изображения в формате PNG
                image.save(png_path, "PNG")
                print(f"Файл {filename} успешно конвертирован и сохранен как {png_path}")
            except Exception as e:
                print(f"Ошибка при конвертации файла {filename}: {e}")

# Укажите путь к исходной папке и целевой папке
source_folder = 'path/to/source/folder'
target_folder = 'path/to/target/folder'

convert_heic_to_png(source_folder, target_folder)
