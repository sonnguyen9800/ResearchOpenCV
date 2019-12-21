import os

from ImageData import ImageObject
from RepositoryManager import RepositoryManagerClass

FOLDER_DIR = 'natural_images/fruit/'

FOLDER_TO_PROCESS = 'new/'

if __name__ == '__main__':
    repo = RepositoryManagerClass()
    count = 0
    for file in os.listdir(FOLDER_DIR):
        print("Count {}".format(count))
        if not file.startswith('.'):
            # image = get_image(os.path.join(IMAGE_DIRECTORY, file))
            # print(" File to be processed: {}/{}".format(FOLDER_DIR, file))

            image = ImageObject(os.path.join(FOLDER_DIR, file))
            image.show_selected_images(repo.COLORS, repo.FOLDER_COLOR)
            # images.append(image)
            count += 1
        if count >= 200:
            break
