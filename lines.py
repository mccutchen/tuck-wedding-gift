#!/usr/bin/env python

import random
import sys
from PIL import Image, ImageDraw


HORIZONTAL = 0
VERTICAL = 1
DIAGONAL = 2

# how much can each color vary from the previous?
MAX_DELTA = 10

# how far back does a color bounce when it gets too large or small?
BOUNCINESS = 2.2


def sloppycolor(base=None):
    """
    Produces a random color optionally based on the given base color, supplied
    as a 3-tuple like (red, green, blue) where red green and blue are between 0
    and 255.
    """
    if base is None:
        return (random.randint(0, 255),
                random.randint(0, 255),
                random.randint(0, 255),
                255)
    r, g, b, a = base
    return (validate(r + getdelta(MAX_DELTA)),
            validate(g + getdelta(MAX_DELTA)),
            validate(b + getdelta(MAX_DELTA)),
            a)


def validate(component):
    """
    Ensures that component (which represents the red, green or blue component
    of a color) is between 0 and 255.  If a given component is too large or too
    small, it is 'bounced' back the other way by an amount controlled by the
    bounciness parameter.
    """
    assert isinstance(component, int)

    if 0 <= component < 256:
        return component

    delta = 0
    if component > 255:
        delta = int((255 - component) * BOUNCINESS)
    elif component < 0:
        delta = int(-component * BOUNCINESS)
    return component + delta


def getdelta(max):
    """
    return a random delta value that is between -max and max
    """
    return random.randint(-max, max)


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

    c = sloppycolor()
    if direction == VERTICAL:
        for i in range(0, width):
            c = sloppycolor(c)
            draw.line((i, 0) + (i, height), c)
    elif direction == HORIZONTAL:
        for i in range(0, height):
            c = sloppycolor(c)
            draw.line((0, i) + (width, i), c)
    elif direction == DIAGONAL:
        for i in range(0, maxdimension):
            c = sloppycolor(c)
            x1 = min(i, maxdimension)
            y1 = max(0, i - maxdimension)
            x2 = max(0, i - maxdimension)
            y2 = min(i, maxdimension)
            draw.line((x1, y1, x2, y2), c)
        image = image.crop((0, 0, width, height))
    return image


def main():
    image = lines(DIAGONAL, 500, 500)
    image.save(sys.stdout, 'PNG')
    return 0


if __name__ == '__main__':
    sys.exit(main())
