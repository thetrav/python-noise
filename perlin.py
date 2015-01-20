import random
from numpy import array, dot
from numpy.linalg import norm
from math import pow, floor, ceil


def ease(start, stop):
    dif = stop - start
    return 3 * (pow(dif, 2)) - 2 * (pow(dif, 3))


def interpolate(start, stop, amount):
    return (stop - start) * amount + start


def coord(x, y):
    return array([x, y])


class Perlin:
    def __init__(self, gridSize=50.0, seed=133788135):
        self.gridSize = gridSize
        self.seed = seed
        self.generator = random.Random(seed)
        self.cache = {}

    def snap_left(self, scalar):
        size = self.gridSize
        shift = floor(ceil(scalar / -size) * size) if scalar < 0 else 0
        s = scalar + shift
        return s - s % size - shift

    def gradient(self, vector):
        key = "%s, %s" % (vector[0], vector[1])
        if not (key in self.cache):
            a = coord(self.generator.random(), self.generator.random())
            self.cache[key] = a / norm(a)
        return self.cache[key]

    def value(self, vector):
        size = self.gridSize
        x = vector[0]
        y = vector[1]

        x0 = self.snap_left(x)
        y0 = self.snap_left(y)
        x1 = x0 + size
        y1 = y0 + size

        def difference(p):
            return (vector - p) / size

        def influence(p):
            return dot(self.gradient(p), difference(p))

        i1 = influence(coord(x0, y0))
        i2 = influence(coord(x1, y0))
        i3 = influence(coord(x0, y1))
        i4 = influence(coord(x1, y1))

        sx = ease(x0 / size, x / size)

        a = interpolate(i1, i2, sx)
        b = interpolate(i3, i4, sx)

        sy = ease(y0 / size, y / size)
        z = interpolate(a, b, sy)

        return abs(z)
