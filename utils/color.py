from colormath.color_objects import sRGBColor, HSLColor, HSVColor, LabColor, XYZColor
from colormath.color_conversions import convert_color


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


def make_interpolations(color_obj, steps=64, ColorClass=None):
    if ColorClass is not None:
        color_obj = convert_color(color_obj, ColorClass)
    color_dict = color_obj.__dict__
    interpolations = {}
    return interpolations
