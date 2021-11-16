from PIL import Image
import os
import numpy as np

file_num = input('Введите номер файла: ')
with Image.open(os.path.join('lunar_images', f'lunar0{file_num}_raw.jpg')) as f:
    data = np.array(f)

min_color = data.min()
max_color = data.max()

new_data = np.interp(data, [min_color, max_color], [0, 255])
res_img = Image.fromarray(new_data).convert('RGB')
res_img.save(os.path.join('new_lunar_images', f'lunar0{file_num}_fresh.jpg'))
