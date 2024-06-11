import os
import shutil

# rename and copy labels
src_format = 'C:/Users/noy/Downloads/CarsMansReadyForYolo/new_aug/'
src_labels = []
src_images = []
for i in range(1, 9):
    src_labels.append(os.path.join(src_format, str(i) + "/labels/"))
    src_images.append(os.path.join(src_format, str(i) + "/images/"))
dst_labels = 'C:/Users/noy/Downloads/CarsMansReadyForYolo/new_aug/10/labels/'
dst_images = 'C:/Users/noy/Downloads/CarsMansReadyForYolo/new_aug/10/images/'

i = 0
for j, label_folder in enumerate(src_labels):
    image_folder = src_images[j]
    labels = os.listdir(label_folder)[:]
    images = os.listdir(image_folder)[:]
    for label, image in enumerate(images):
        src_label = os.path.join(label_folder, str(label) + ".txt")
        src_image = os.path.join(image_folder, image)
        dst_label = os.path.join(dst_labels, str(7000 + i) + ".txt")
        dst_image = os.path.join(dst_images, str(7000 + i) + ".jpg")
        shutil.copy(src_label, dst_label)
        shutil.copy(src_image, dst_image)
        i += 1

