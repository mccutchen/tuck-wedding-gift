#!/usr/bin/env python

import random
import sys
from PIL import Image, ImageDraw


HORIZONTAL = 0
VERTICAL = 1
DIAGONAL = 2


def random_color():
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


def validate_channel(channel, bounciness=2.2):
    if 0 <= channel <= 255:
        return channel
    if channel > 255:
        delta = (255 - channel) * bounciness
    else:
        delta = channel * -bounciness
    return channel + int(delta)


def get_delta(max_delta):
    return random.randint(-max_delta, max_delta)


def fudge_color((r, g, b), max_delta=10):
    return (validate_channel(r + get_delta(max_delta)),
            validate_channel(g + get_delta(max_delta)),
            validate_channel(b + get_delta(max_delta)))


def make_color_stream(color):
    while True:
        yield color
        color = fudge_color(color)


def lines(direction, width, height):
    maxdimension = max(width, height) * 2
    if direction == DIAGONAL:
        # if we're generating a slanted image, we have to make it twice as big
        # as the largest requested dimension and then crop it, so the lines
        # come out right
        size = (maxdimension, maxdimension)
    else:
        size = (width, height)

    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)

    color_stream = make_color_stream(random_color())
    if direction == VERTICAL:
        for i in range(0, width):
            draw.line((i, 0) + (i, height), next(color_stream))
    elif direction == HORIZONTAL:
        for i in range(0, height):
            draw.line((0, i) + (width, i), next(color_stream))
    elif direction == DIAGONAL:
        for i in range(0, maxdimension):
            x1 = min(i, maxdimension)
            y1 = max(0, i - maxdimension)
            x2 = max(0, i - maxdimension)
            y2 = min(i, maxdimension)
            draw.line((x1, y1, x2, y2), next(color_stream))
        image = image.crop((0, 0, width, height))
    return image


def main():
    image = lines(DIAGONAL, 500, 500)
    image.save(sys.stdout, 'PNG')
    return 0


if __name__ == '__main__':
    sys.exit(main())
