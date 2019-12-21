import os
import shutil

import cv2 as cv

from ImageData import ImageObject

COLORS = {
    'RED': [255, 0, 0],
    'ORANGE': [255, 165, 0],
    'INDIGO': [75, 0, 130],
    'VIOLET': [127, 0, 255],
    'GREEN': [0, 128, 0],
    'YELLOW': [255, 255, 0],
    'BLUE': [0, 0, 255]
}


class RepositoryManagerClass:
    FOLDER_DIR = 'natural_images/fruit/'

    WORKING_DIR = 'imageRepository/'

    COLORS = {
        'BLUE': [0, 0, 255],
        'RED': [255, 0, 0],
        'ORANGE': [255, 165, 0],
        'INDIGO': [75, 0, 130],

        'VIOLET': [127, 0, 255],
        'GREEN': [0, 128, 0],
        'YELLOW': [255, 255, 0],
    }

    FOLDER_COLOR = {
        'BLUE': "colors/blue/",
        'RED': "colors/red/",
        'ORANGE': "colors/orange/",
        'INDIGO': "colors/indigo/",

        'VIOLET': "colors/violet/",
        'GREEN': "colors/green/",
        'YELLOW': "colors/yellow/",

        'MAIN': "colors/",
    }

    # Constructor, make the necessary folder if they are not exist
    def __init__(self):
        self.clearAllFolder()
        for folder in self.FOLDER_COLOR:
            if not os.path.exists(self.FOLDER_COLOR[folder]):
                os.makedirs(self.FOLDER_COLOR[folder])

    # Clear folder, take folder path to clear the inside contents
    def clear_folder(self, folder_path):
        print("Begin to clear folder: {}".format(folder_path))
        folder = folder_path
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    # Clear all output folder

    # Read Images from sources, flag equals True means save images to second database
    def readImagesFromSource(self, source_database=FOLDER_DIR, dest=WORKING_DIR):
        images = []
        count = 0
        for file in os.listdir(source_database):
            if not file.startswith('.'):
                image = ImageObject(os.path.join(source_database, file))

                self.writeToFolder(image.image, dest, "IMAGE" + str(count) + ".jpg")
                images.append(image)
                count += 1
            if len(images) >= 5:
                break
        return images

    def writeToFolder(self, image, path, name):
        print("Writing to {}, filename: {}".format(path, name))
        cv.imwrite(os.path.join(path, name), image)

    def clearAllFolder(self):
        for folder in self.FOLDER_COLOR:
            self.clear_folder(self.FOLDER_COLOR[folder])
