#!/usr/bin/env python

import colorsys
import itertools
import random
import sys
from PIL import Image, ImageDraw


def prep_seed_color(rgb):
    return colorsys.rgb_to_hsv(*[x / 255.0 for x in rgb])


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


def lines(width, height, seed_colors):
    maxdimension = max(width, height) * 2
    size = (maxdimension, maxdimension)

    image = Image.new('RGB', size)
    draw = ImageDraw.Draw(image)

    num_segments = len(seed_colors)
    segment_width = (width + height) / num_segments
    color_streams = [make_color_stream(c) for c in seed_colors]

    for i in xrange(0, maxdimension):
        quotient, remainder = divmod(i, segment_width)
        color_stream = color_streams[quotient % num_segments]
        x1 = min(i, maxdimension)
        y1 = max(0, i - maxdimension)
        x2 = max(0, i - maxdimension)
        y2 = min(i, maxdimension)
        draw.line((x1, y1, x2, y2), hsv_to_rgb(next(color_stream)))
    return image.crop((0, 0, width, height))


def main(width, height):
    seed_colors = [
        (39, 54, 175), # blue
        (99, 157, 61), # green
    ]
    image = lines(width, height, map(prep_seed_color, seed_colors))
    image.save(sys.stdout, 'PNG')
    return 0


if __name__ == '__main__':
    if len(sys.argv) == 3:
        width, height = map(int, sys.argv[1:])
    else:
        width, height = 600, 400
    sys.exit(main(width, height))
