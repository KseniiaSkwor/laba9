from PIL import Image, ImageFilter
import os
if not os.path.exists('blur'):
    os.makedirs('blur')

from pathlib import Path
# Определение расширения файла с использованием pathlib
file_path = Path( 'example.jpg')
if file_path. suffix. lower () == '.png':
    print(f"Файл (file_path.name) может содержать неожиданные данные.")
else:
    print(f"Файл (file_path.name) являются jpg.")

image = Image.open("1.jpg")
image2 = Image.open("2.jpg")
image3 = Image.open("3.jpg")
image4 = Image.open("4.jpg")
image5 = Image.open("5.jpg")

blur_img = image.filter(ImageFilter.BLUR)
blur_img2 = image2.filter(ImageFilter.BLUR)
blur_img3 = image3.filter(ImageFilter.BLUR)
blur_img4 = image4.filter(ImageFilter.BLUR)
blur_img5 = image5.filter(ImageFilter.BLUR)

blur_img.save('blur/11.jpg')
blur_img2.save('blur/12.jpg')
blur_img3.save('blur/13.jpg')
blur_img4.save('blur/14.jpg')
blur_img5.save('blur/15.jpg')