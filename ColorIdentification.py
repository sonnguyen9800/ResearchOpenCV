import os
from collections import Counter

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage.color import rgb2lab, deltaE_cie76
from sklearn.cluster import KMeans


def get_image(image_path):
    image = cv2.imread(image_path)
    return image


def convert_image(img):
    image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return image


def clear_folder(folder_path):
    print("Begin to clear folder: {}".format(folder_path))
    folder = folder_path
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            # elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)


def writeToFolder(image, path, name):
    print("Writing to {}, filename: {}".format(path, name))
    cv2.imwrite(os.path.join(path, name), image)


def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))


def get_colors(image, num_colors, flag_pie):
    image = convert_image(image)
    modified_image = cv2.resize(image, (600, 400), interpolation=cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0] * modified_image.shape[1], 3)

    clf = KMeans(n_clusters=num_colors)
    labels = clf.fit_predict(modified_image)

    counts = Counter(labels)

    center_colors = clf.cluster_centers_
    # We get ordered colors by iterating through the keys
    ordered_colors = [center_colors[i] for i in counts.keys()]
    hex_colors = [RGB2HEX(ordered_colors[i]) for i in counts.keys()]
    rgb_colors = [ordered_colors[i] for i in counts.keys()]

    if (flag_pie):
        plt.figure(figsize=(8, 6))
        plt.pie(counts.values(), labels=hex_colors, colors=hex_colors)

    return rgb_colors


def match_image_by_color(image, color, threshold=60, number_of_colors=10):
    image_colors = get_colors(image, number_of_colors, False)
    selected_color = rgb2lab(np.uint8(np.asarray([[color]])))

    select_image = False
    for i in range(number_of_colors):
        curr_color = rgb2lab(np.uint8(np.asarray([[image_colors[i]]])))
        diff = deltaE_cie76(selected_color, curr_color)
        if (diff < threshold):
            select_image = True

    return select_image


def show_selected_images(images, color, threshold, colors_to_match):
    count = 0
    name = "Image"
    for i in range(len(images)):
        print("Checking image")
        selected = match_image_by_color(images[i],
                                        color,
                                        threshold,
                                        colors_to_match)
        if (selected):
            count += 1
            writeToFolder(images[i], "blue/", name + str(count) + ".jpg")


IMAGE_DIRECTORY = 'natural_images/fruit/'

COLORS = {
    'RED': [255, 0, 0],
    'ORANGE': [255, 165, 0],
    'INDIGO': [75, 0, 130],
    'VIOLET': [127, 0, 255],
    'GREEN': [0, 128, 0],
    'YELLOW': [255, 255, 0],
    'BLUE': [0, 0, 255]
}

FOLDER = {
    'BLUE': "blue/",
    'RED': "red/",
    'ORANGE': "orange/",
    'INDIGO': "indigo/",
    'VIOLET': "violet/",
    'GREEN': "green/",
    'YELLOW': "yellow"
}

clear_folder("blue/")
# clear_folder("green/")
# clear_folder("yellow/")
clear_folder("imageRepository/")

images = []
count = 0
for file in os.listdir(IMAGE_DIRECTORY):
    if not file.startswith('.'):
        image = get_image(os.path.join(IMAGE_DIRECTORY, file))
        writeToFolder(image, "imageRepository", "IMAGE" + str(count) + ".jpg")
        images.append(image)
        count += 1
    if len(images) >= 100:
        break

plt.figure(figsize=(20, 10))
for i in range(len(images)):
    plt.subplot(1, len(images), i + 1)
    plt.imshow(images[i])

# Variable 'selected_color' can be any of COLORS['GREEN'], COLORS['BLUE'] or COLORS['YELLOW']
plt.figure(figsize=(20, 10))
show_selected_images(images, COLORS['BLUE'], 100, 3)
