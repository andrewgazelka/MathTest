import math

from decimal import Decimal


class RightTriangle:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def hypot2(self):
        return self.dx ** 2 + self.dy ** 2

    def hypot(self):
        return math.sqrt(self.hypot2())


def find_x_force_1(dx, dy, magnitude):
    # dy/dx = F_y / F_x
    # this is essentially saying tan(theta) = dy/dx = F_y / F_x

    # F_x dy/dx = F_y (1)

    # hypot = sqrt(F_y^2 + F_x^2) (2)

    # hypot = sqrt([F_x dy/dx]^2 + F_x^2) (2)
    # hypot = sqrt([F_x^2 [(dy/dx)^2 + 1]) (2)
    # hypot = sqrt([F_x^2 [(dy/dx)^2 + 1]) (2)
    # hypot = F_x * sqrt((dy/dx)^2 + 1) (2)

    # hypot = F_x * sqrt((dy/dx)^2 + 1) (2)
    # F_x = hypot / sqrt((dy/dx)^2 + 1)

    return magnitude / math.sqrt((dy / dx) ** 2 + 1)


def find_x_force_2(dx, dy, magnitude):
    h = math.sqrt(dx ** 2 + dy ** 2)

    # dx / h = F_x / mag
    return dx / h * magnitude


def approximate_sin_maclauren(rad, iterations):
    # sin (rad) = sin(0) + cos(0) x_0 - sin(0) x_0^2/2!

    rad_decimal = Decimal(rad)
    map = {
        0: 0,
        1: 1,
        2: 0,
        3: -1
    }

    sum = 0
    for i in range(iterations):
        cycle_level = i % 4
        val = map[cycle_level]
        if val != 0:
            sum += val * (rad_decimal ** i) / math.factorial(i)
    return sum


def euler_e_val(iterations=1000, dx=0.1, x_i=0, y_i=1):
    """
    let us have the equation dy/dx = y, y(0) = 1

    {a}^10

    :return:
    """

    if iterations == 0:
        return {
            "x": x_i,
            "y": y_i
        }

    x_i += dx
    y_i += y_i * dx

    return euler_e_val(iterations - 1, dx, x_i, y_i)


def calc_e(iterations=500, dx=1E-10):
    val = euler_e_val(iterations, dx)
    e = math.pow(val["y"], 1 / val["x"])
    return e


if __name__ == "__main__":
    print(calc_e())
