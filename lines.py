#!/usr/bin/env python

import colorsys
import itertools
import random
import sys
from PIL import Image, ImageDraw


seed_color = (39, 54, 175)
seed_color = (99, 157, 61)

seed_rgb = tuple(x / 255.0 for x in seed_color)
seed_hsv = colorsys.rgb_to_hsv(*seed_rgb)


def hsv_to_rgb(hsv):
    rgb = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(*hsv))
    assert all(0 <= x < 256 for x in rgb), rgb
    return rgb


def validate_channel(chan, min_val=0.0, max_val=1.0, bounce=1.01):
    if min_val <= chan <= max_val:
        return chan
    if chan > max_val:
        delta = (max_val - chan) * bounce
    else:
        delta = -1 * chan * bounce
    return chan + delta


def get_delta(max_delta):
    delta = random.random() * max_delta
    return delta if random.random() >= 0.5 else -delta


def fudge_color((h, s, v)):
    return (validate_channel(h + get_delta(0.005)),
            validate_channel(s + get_delta(0.01)),
            validate_channel(v + get_delta(0.025)))


def make_color_stream(color):
    while True:
        yield color
        color = fudge_color(color)


def lines(width, height):
    maxdimension = max(width, height) * 2
    size = (maxdimension, maxdimension)

    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)
    color_stream = make_color_stream(seed_hsv)

    for i, color in itertools.izip(xrange(0, maxdimension), color_stream):
        x1 = min(i, maxdimension)
        y1 = max(0, i - maxdimension)
        x2 = max(0, i - maxdimension)
        y2 = min(i, maxdimension)
        draw.line((x1, y1, x2, y2), hsv_to_rgb(color))
    return image.crop((0, 0, width, height))


def main(width, height):
    lines(width, height).save(sys.stdout, 'PNG')
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 3:
        width, height = map(int, sys.argv[1:])
    else:
        width, height = 600, 400
    sys.exit(main(width, height))
