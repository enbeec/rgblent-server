from colormath.color_objects import sRGBColor, HSLColor, HSVColor, LabColor, XYZColor
from colormath.color_conversions import convert_color
from math import sqrt


def rgb_hex__int_tuple(rgb_hex):
    return (int(rgb_hex[1:3], 16), int(rgb_hex[3:5], 16), int(rgb_hex[5:7], 16))


def color_info(rgb_hex):
    srgb = sRGBColor(*rgb_hex__int_tuple(rgb_hex))
    return {
        "rgb": srgb.__dict__,
        "hsl": convert_color(srgb, HSLColor).__dict__,
        "hsv": convert_color(srgb, HSVColor).__dict__,
        "lab": convert_color(srgb, LabColor).__dict__,
        "xyz": convert_color(srgb, XYZColor).__dict__
    }


def average(int1, int2):
    # https://stackoverflow.com/a/29576746
    return sqrt((int1 ** 2 + int2 ** 2)/2)


def color_blend(rgb_hex1, rgb_hex2):
    (r1, g1, b1) = rgb_hex__int_tuple(rgb_hex1)
    (r2, g2, b2) = rgb_hex__int_tuple(rgb_hex2)
    return sRGBColor(average(r1, r2), average(g1, g2), average(b1, b2)).__dict__
