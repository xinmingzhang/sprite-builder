import os
import copy
import json
import pygame as pg


def load_all_gfx(directory,colorkey=(0,0,0),accept=(".png",".jpg",".bmp")):
    graphics = {}
    for pic in os.listdir(directory):
        name,ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name]=img
    return graphics

def load_all_music(directory, accept=(".wav", ".mp3", ".ogg", ".mdi")):
    songs = {}
    for song in os.listdir(directory):
        name,ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs

def load_all_sfx(directory, accept=(".wav", ".mp3", ".ogg", ".mdi")):
    effects = {}
    for fx in os.listdir(directory):
        name,ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects

def load_all_fonts(directory, accept=(".ttf")):
    return load_all_music(directory, accept)

def load_all_courses(directory, accept=(".json")):
    return load_all_music(directory, accept)

def strip_from_sheet(sheet, start, size, columns, rows=1):
    """
    Strips individual frames from a sprite sheet given a start location,
    sprite size, and number of columns and rows.
    """
    frames = []
    for j in range(rows):
        for i in range(columns):
            location = (start[0]+size[0]*i, start[1]+size[1]*j)
            frames.append(sheet.subsurface(pg.Rect(location, size)))
    return frames

def color_swap(source_image, swap_map):
    """
    Creates a new Surface from the source_image with some or all colors
    swapped for new colors. Colors are swapped according to the
    color pairs in the swap_map dict. The keys and values in swap_map
    can be RGB tuples or pygame color-names. For each key in swap_map,
    all pixels of that color will be replaced by the color that key maps to.
    For example, passing this dict:

    {(0,255,0): (255, 0, 255),
      "black": (255, 0, 0),
      "yellow": "green"}

    would result in green pixels recolored purple, black pixels recolored
    red and yellow pixels recolored green.
    NOTE: This will not work if Pygame's video mode has not been set
    (i.e., you need to call pygame.display.set_mode beforehand).
    """
    img = source_image
    size = img.get_size()
    surf = pg.Surface(size)
    color_surf = pg.Surface(size)
    final = img.copy()
    for original_color, new_color in swap_map.items():
        if isinstance(original_color, str):
            original = pg.Color(original_color)
        else:
            original = original_color
        if isinstance(new_color, str):
            recolor = pg.Color(new_color)
        else:
            recolor = new_color
        color_surf.fill(original)
        surf.set_colorkey(original)
        pg.transform.threshold(surf, img, original, (0,0,0,0),
                               recolor, 1, color_surf, True)
        final.blit(surf, (0,0))
    return final

def lerp(color_1, color_2, lerp_val):
    """
    Return a new color that is a linear interpolation of the two
    argument colors.  lerp_val must be between 0 and 1 (inclusive).
    """
    if not (0 <= lerp_val <= 1):
        raise ValueError("Lerp value must be in the range [0,1] inclusive.")
    new = [int(a*(1-lerp_val)+b*lerp_val) for a, b in  zip(color_1, color_2)]
    return pg.Color(*new)
    
    
class _KwargMixin(object):
    """
    Useful for classes that require a lot of keyword arguments for
    customization.
    """
    def process_kwargs(self, name, defaults, kwargs):
        """
        Arguments are a name string (displayed in case of invalid keyword);
        a dictionary of default values for all valid keywords;
        and the kwarg dict.
        """
        settings = copy.deepcopy(defaults)
        for kwarg in kwargs:
            if kwarg in settings:
                if isinstance(kwargs[kwarg], dict):
                    settings[kwarg].update(kwargs[kwarg])
                else:
                    settings[kwarg] = kwargs[kwarg]
            else:
                message = "{} has no keyword: {}"
                raise AttributeError(message.format(name, kwarg))
        for setting in settings:
            setattr(self, setting, settings[setting])

def cursor_from_image(image,size,hotspot,location=(0,0),flip=False):
    """
    This code I copy from Sean McKiernan,here i thank him very much!

    This function's return value is of the form accepted by
    pg.mouse.set_cursor() (passed using the *args syntax). The argument image
    is an already loaded image surface containing your desired cursor; size is
    a single integer corresponding to the width of the cursor (must be a
    multiple of 8); hotspot is a 2-tuple representing the exact point in your
    cursor that will represent the mouse position; location is a 2-tuple for
    where your cursor is located on the passed in image. Setting flip to True
    will create the cursor with colors opposite to the source image.

    Color in image to color in cursor defaults:
        Black (  0,   0,   0) ---> Black
        White (255, 255, 255) ---> White
        Cyan  (  0, 255, 255) ---> Xor (only available on certain systems)
        Any Other Color ---------> Transparent
    """
    if size%8:
        raise ValueError("Size must be a multiple of 8.")
    compile_args = (".", "X", "o") if flip else ("X", ".", "o")
    colors = {(  0,  0,  0,255) : ".",
              (255,255,255,255) : "X",
              (  0,255,255,255) : "o"}
    cursor_string = []
    for j in range(size):
        this_row = []
        for i in range(size):
            where = (i+location[0], j+location[1])
            pixel = tuple(image.get_at(where))
            this_row.append(colors.get(pixel, " "))
        cursor_string.append("".join(this_row))
    xors,ands = pg.cursors.compile(cursor_string, *compile_args)
    size = size, size
    return size, hotspot, xors, ands

