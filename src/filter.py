from random import randint


def shades_of_gray(pixels, draw, width, height):
    print("Shades of gray filter.")
    for i in range(width):
        for j in range(height):
            tmp = [pixels[i, j][0], pixels[i, j][1], pixels[i, j][2]]
            bw = int(sum(pixels[i, j]) / 3)
            for k in range(len(tmp)):
                tmp[k] = bw
            draw.point((i, j), tuple(tmp))


def sepia(pixels, draw, width, height):
    print("Sepia")
    for i in range(width):
        for j in range(height):
            tmp = list(pixels[i, j])
            sp = int(sum(tmp) / 3)
            for k in range(len(tmp)):
                tmp[k] = sp
            tmp[2] = int(tmp[2] * 0.65)
            tmp[1] = int(tmp[1] * 0.9)
            draw.point((i, j), tuple(tmp))


def negative(pixels, draw, width, height):
    print("Negative")
    for i in range(width):
        for j in range(height):
            tmp = list(pixels[i, j])
            for k in range(len(tmp)):
                tmp[k] = 255 - tmp[k]
            draw.point((i, j), tuple(tmp))


def black_white(pixels, draw, width, height):
    print("Black & white filter")
    for i in range(width):
        for j in range(height):
            tmp = [pixels[i, j][0], pixels[i, j][1], pixels[i, j][2]]
            bw = int(sum(pixels[i, j]) / 3)
            bw = 0 if bw < 128 else 255
            for k in range(len(tmp)):
                tmp[k] = bw
            draw.point((i, j), tuple(tmp))


def filter_custom(pixels, draw, width, height, r, g, b):
    for i in range(width):
        for j in range(height):
            tmp = list(pixels[i, j])
            tmp[0] = int(tmp[0] * r / 255)
            tmp[1] = int(tmp[1] * g / 255)
            tmp[2] = int(tmp[2] * b / 255)
            draw.point((i, j), tuple(tmp))


def filter_red(pixels, draw, width, height):
    filter_custom(pixels, draw, width, height, 250, 0, 0)


def filter_orange(pixels, draw, width, height):
    filter_custom(pixels, draw, width, height, 250, 110, 0)


def filter_yellow(pixels, draw, width, height):
    filter_custom(pixels, draw, width, height, 250, 250, 0)


def filter_green(pixels, draw, width, height):
    filter_custom(pixels, draw, width, height, 0, 250, 0)


def filter_cyan(pixels, draw, width, height):
    filter_custom(pixels, draw, width, height, 0, 250, 250)


def filter_blue(pixels, draw, width, height):
    filter_custom(pixels, draw, width, height, 0, 0, 250)


def filter_purple(pixels, draw, width, height):
    filter_custom(pixels, draw, width, height, 250, 0, 250)


def filter_random(pixels, draw, width, height):
    print("Random noise.")
    for i in range(width):
        for j in range(height):
            tmp = list(pixels[i, j])
            tmp[0] = int(tmp[0] * randint(0, 255) / 255)
            tmp[1] = int(tmp[1] * randint(0, 255) / 255)
            tmp[2] = int(tmp[2] * randint(0, 255) / 255)
            draw.point((i, j), tuple(tmp))


def filter_color(pixels, draw, width, height, color):
    if color[0] != "#":
        if color != "random":
            print("Color", color + ".")
        try:
            eval("filter_" + color.lower() + "(pixels, draw, width, height)")
        except NameError:
            print("No such color:", color)
    else:
        print("Color", color + ".")
        color = color[1:].lower()
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        filter_custom(pixels, draw, width, height, r, g, b)
