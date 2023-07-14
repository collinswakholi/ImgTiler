import cv2
from ImageTiler import *

image = cv2.imread('img.jpg')
grid = (3,4)
overlap = 30
show_image = True
show_rect = False

splitter = SplitImage(image=image, grid=grid, overlap=overlap)
tiles = splitter.split_image(show_rect=show_rect, show_tiles=show_image)

combiner = CombineTiles(tiles=tiles, grid=grid, overlap=overlap)
combined_image = combiner.combine_tiles(show_image=show_image)