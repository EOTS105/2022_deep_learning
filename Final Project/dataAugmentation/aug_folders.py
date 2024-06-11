import os
import shutil

# Define the source folder and the destination folder prefix
old_f = "C:/Users/noy/Downloads/CarsMansReadyForYolo/train/labels"
old_img_f = "C:/Users/noy/Downloads/CarsMansReadyForYolo/train/images"
new_f_prefix = "C:/Users/noy/Downloads/CarsMansReadyForYolo/mini_batch/"
new_aug_f = "C:/Users/noy/Downloads/CarsMansReadyForYolo/new_aug/"

# Get a list of all the files in the source folder
files = os.listdir(old_f)
imgs = os.listdir(old_img_f)

# Divide the files into groups
group_size = len(files) // 100
for i in range(100):
    new_f = new_f_prefix + str(i + 1) + '/labels'
    new_img_f = new_f_prefix + str(i + 1) + '/images'
    new_aug = new_aug_f + str(i + 1) + '/labels'
    new_aug_img = new_aug_f + str(i + 1) + '/images'

    # Create the destination folder if it doesn't exist
    if not os.path.exists(new_f):
        os.makedirs(new_f)
    if not os.path.exists(new_img_f):
        os.makedirs(new_img_f)
    if not os.path.exists(new_aug):
        os.makedirs(new_aug)
    if not os.path.exists(new_aug_img):
        os.makedirs(new_aug_img)

    # Copy the files in the current group to the destination folder
    start = i * group_size
    end = (i + 1) * group_size
    for j in range(start, end):
        src = os.path.join(old_f, files[j])
        dst = os.path.join(new_f, files[j])
        shutil.copy2(src, dst)
        dst_aug = os.path.join(new_aug, files[j])
        shutil.copy2(src, dst_aug)

        # for the first 10 batches only, copy the images
        if i < 10:
            src_img = os.path.join(old_img_f, imgs[j])
            dst_img = os.path.join(new_img_f, imgs[j])
            shutil.copy2(src_img, dst_img)

