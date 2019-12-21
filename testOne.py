from ImageData import ImageObject
from RepositoryManager import RepositoryManagerClass

repo = RepositoryManagerClass()

FOLDER_DIR = 'fruit/'

FOLDER_TO_PROCESS = 'imageRepository/'

image_example = ImageObject("imageRepository/IMAGE3.jpg")
image_example.showImage()
# image_example = ImageObject("natural_images/fruit/fruit_0460.jpg")
image_example.extractForeground(display_image=True)
image_example.get_colors(flag_pie=True, num_colors=3)

# image_example = ImageObject("new/IMAGE2.jpg")
# image_example.show_selected_images(repo.COLORS, repo.FOLDER_COLOR)

#
# for file in os.listdir(FOLDER_DIR):
#     # print("Count {}".format(count))
#     if not file.startswith('.'):
#         # image = get_image(os.path.join(IMAGE_DIRECTORY, file))
#         # print(" File to be processed: {}{}".format(FOLDER_DIR, file))
#         image_example = ImageObject("natural_images/fruit/fruit_0460.jpg")
#         image_example.get_colors()
#
#         # image_example.show_selected_images(repo.COLORS, repo.FOLDER_COLOR)
#         # images.append(image)
#         # count += 1
