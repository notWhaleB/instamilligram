import sys

from PIL import Image
from PIL import ImageDraw

import filter
import modifier

""" The script uses the selected filter or modifier to the original image and
saves the result in the specified file.
List of filters:
-h : shades of gray (8-bit).
-bw : black & white (1-bit monochrome).
-s : sepia.
-n : negative.
-f C: custom filter with C color argument: red, green, yellow and other rainbow,
or hex code (#AABBCC) of color or random.

List of modifiers:
-br N: multiple brightness on N.
-m N: scale image on N.
-bl k: blur image with k * k tile.
"""


def image_processing(args, img):
    width, height = input_image.size
    pixels = input_image.load()
    output_image = Image.new('RGB', (width, height))
    draw = ImageDraw.Draw(output_image)

    if args[3] == "-h":
        filter.shades_of_gray(pixels, draw, width, height)
    elif args[3] == "-bw":
        filter.black_white(pixels, draw, width, height)
    elif args[3] == "-s":
        filter.sepia(pixels, draw, width, height)
    elif args[3] == "-n":
        filter.negative(pixels, draw, width, height)
    elif args[3] == "-f":
        filter.filter_color(pixels, draw, width, height, args[4])
    elif args[3] == "-br":
        modifier.brightness(pixels, draw, width, height, float(args[4]))
    elif args[3] == "-m":
        modifier.scale(pixels, draw, width, height, float(args[4]))
    elif args[3] == "-bl":
        modifier.blur(pixels, draw, width, height, int(args[4]))
    elif args[3] == "":
        modifier.no_changes(pixels, draw, width, height)

    output_image_filename = args[2]
    output_image.save(output_image_filename, 'JPEG')


if __name__ == "__main__":
    argv = sys.argv

input_image = Image.open(argv[1])

if len(argv) == 3:
    argv.append("")

help("__main__")
image_processing(argv, input_image)

print("Done.")








