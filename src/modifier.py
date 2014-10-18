from math import floor


def no_changes(pixels, draw, width, height):
    print("No changes.")
    for i in range(width):
        for j in range(height):
            draw.point((i, j), pixels[i, j])


def scale(pixels, draw, width, height, n):
    print("Scale.")
    for i in range(width):
        for j in range(height):
            p = floor(width * (n - 1) / (2 * n) + i / n)
            q = floor(height * (n - 1) / (2 * n) + j / n)
            if q >= height or q < 0 or p >= width or p < 0:
                draw.point((i, j), (0, 0, 0))
            else:
                draw.point((i, j), pixels[p, q])


def brightness(pixels, draw, width, height, n):
    print("Brightness.")
    for i in range(width):
        for j in range(height):
            tmp = list(pixels[i, j])
            for k in range(3):
                tmp[k] = min(int(tmp[k] * n), 255)
            draw.point((i, j), tuple(tmp))


def blur(pixels, draw, width, height, size):
    print("Blur.")
    progress = 0
    for i in range(width):
        if progress != floor(i / width * 100):
            progress = floor(i / width * 100)
            print("Progress: ", str(progress) + "%")
        for j in range(height):
            c = [[], [], []]
            for p in range(-size, size + 1):
                for q in range(-size, size + 1):
                    if width > i + p >= 0 and height > j + q >= 0:
                        for k in range(3):
                            c[k].append(pixels[i + p, j + q][k])
            tmp = [0, 0, 0]
            for k in range(3):
                tmp[k] = int(sum(c[k]) / len(c[k]))
            draw.point((i, j), tuple(tmp))

