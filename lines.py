#!/usr/bin/env python

import itertools
import random
import sys
from PIL import Image, ImageDraw


def random_color():
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


def validate_channel(chan, bounce=2.2):
    if 0 <= chan <= 255:
        return chan
    delta = (255 - chan) * bounce if chan > 255 else chan * -bounce
    return chan + int(delta)


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


def lines(width, height):
    maxdimension = max(width, height) * 2
    size = (maxdimension, maxdimension)

    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    color_stream = make_color_stream(random_color())

    for i, color in itertools.izip(xrange(0, maxdimension), color_stream):
        x1 = min(i, maxdimension)
        y1 = max(0, i - maxdimension)
        x2 = max(0, i - maxdimension)
        y2 = min(i, maxdimension)
        draw.line((x1, y1, x2, y2), color)
    return image.crop((0, 0, width, height))


def main():
    lines(500, 500).save(sys.stdout, 'PNG')
    return 0


if __name__ == '__main__':
    sys.exit(main())
