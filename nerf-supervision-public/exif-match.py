from PIL import Image
import os


og_files = os.listdir('../nerf-supervision-public-old/data/fork/images')
# print(og_files)

current_dir = './images/fork'

files = os.listdir('./data/fork/images/')
# print(files)

# load old image and extract EXIF
image = Image.open('../nerf-supervision-public-old/data/fork/images/IMG_2416.png')
print(image._getexif())
exif = image.info['exif']

# load new image
image_new = Image.open('./images/fork/1.png')
image_new.save('modi_w_EXIF.png', 'png', exif=exif)