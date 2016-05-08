import os
import pygame as pg
from tools import strip_from_sheet, load_all_gfx, cursor_from_image, \
     load_all_music,load_all_sfx,load_all_fonts


def load_images(sheet, strip_size, num_columns, num_rows,
                                                 sprite_size, sprites_per_row):
    """Load sprite component images into a dict of dicts."""
    d = {}
    strips = strip_from_sheet(sheet, (0, 0), strip_size, num_columns,
                                                    num_rows)
    for i, strip in enumerate(strips):
        d[i] = {}
        imgs = strip_from_sheet(strip, (0, 0), sprite_size, sprites_per_row)
        for j, img in enumerate(imgs):        
            d[i][j] = img
    return d


SCREEN_SIZE = (640, 480)
ORIGINAL_CAPTION = "Sprite Builder"

pg.mixer.pre_init(44100, -16, 1, 512)



pg.init()
os.environ['SDL_VIDEO_CENTERED'] = "TRUE"
pg.display.set_caption(ORIGINAL_CAPTION)
SCREEN = pg.display.set_mode(SCREEN_SIZE)
SCREEN_RECT = SCREEN.get_rect()

FONTS = load_all_fonts(os.path.join("resources", "font"))
MY_FONT=FONTS['Mouse']


MUSIC = load_all_music(os.path.join("resources", "music"))
BG_M = MUSIC['bg']
SHOW_M = MUSIC['show']

SOUND = load_all_sfx(os.path.join("resources", "sound"))
BUTTON_M = SOUND['button']


GFX   = load_all_gfx(os.path.join("resources", "graphics"))
BG_IMAGE = GFX['bg']
HELP_IMAGE = GFX['help']
CURSOR1_IMAGE = GFX['mouse0']
CURSOR2_IMAGE = GFX['mouse3']

cursor_dict={
    'default' : pg.mouse.get_cursor(),
    'hand'    : cursor_from_image(CURSOR1_IMAGE,16,(8,4)),
    'move'    : cursor_from_image(CURSOR2_IMAGE,16,(8,4))}

def change_cursor(name):
    pg.mouse.set_cursor(*cursor_dict[name])
    return name


#Sprite component image loading
HATS = load_images(GFX["hats"], (816, 116), 1, 34, (68, 116), 12)
SPECIAL_HATS = strip_from_sheet(GFX["special-hats"],(0,0),(68,116),5)
HAIR = load_images(GFX["hair"], (1020, 116), 1, 5, (68, 116), 15)                                          
SKIN = strip_from_sheet(GFX["skin"], (0, 0), (68, 112), 12)
EYES = strip_from_sheet(GFX["eyes"], (0, 0), (68, 112), 17)
FACIAL_HAIR = load_images(GFX["facial-hair"], (1088, 116), 1, 5, (68, 116), 16)
TOPS = load_images(GFX["tops"], (1496, 116), 1, 34, (68, 116), 22)
BOTTOMS = load_images(GFX["bottoms"], (544, 116), 1, 34, (68, 116), 8)
SHOES = strip_from_sheet(GFX["shoes"], (0, 0), (68, 114), 17, 2)
MASKS = load_images(GFX["masks"], (408, 116), 1, 34, (68, 116), 6)
SPECIAL_MASKS = strip_from_sheet(GFX["special-masks"], (0, 0), (68, 116), 12, 2)

BUTTON_HELP = pg.Rect(60,420,80,40)
BUTTON_RESET = pg.Rect(150,420,100,40)
BUTTON_SHOW = pg.Rect(270,420,90,40)
BUTTON_SAVE = pg.Rect(380,420,80,40)
BUTTON_QUIT = pg.Rect(480,420,80,40)

BUTTON_DICT ={
    'Help':BUTTON_HELP,
    'Reset':BUTTON_RESET,
    'Show':BUTTON_SHOW,
    'Save':BUTTON_SAVE,
    'Quit':BUTTON_QUIT}

B_HAIR = pg.Rect(140,105,110,35)
B_F_HAIR = pg.Rect(140,185,110,35)
B_SKIN = pg.Rect(140,270,110,35)
B_EYES = pg.Rect(140,355,110,35)
B_BACKGROUND = pg.Rect(260,355,120,35)
B_HAT = pg.Rect(380,105,50,35)
B_S_HAT = pg.Rect(430,105,70,35)
B_MASK = pg.Rect(380,170,60,35)
B_S_MASK = pg.Rect(440,170,70,35)
B_TOPS=pg.Rect(380,230,120,35)
B_BOTTOMS=pg.Rect(380,295,120,35)
B_SHOES=pg.Rect(380,355,120,35)

BACKGROUND =[pg.Color('red'),pg.Color('darkorange'),pg.Color('yellow'),\
             pg.Color('green1'),pg.Color('blue'),pg.Color('purple')]

B_DICT ={
    'hair':B_HAIR,
    'facial_hair':B_F_HAIR,
    'skin':B_SKIN,
    'eyes':B_EYES,
    'background':B_BACKGROUND,
    'hat':B_HAT,
    'special_hat':B_S_HAT,
    'mask':B_MASK,
    'special_mask':B_S_MASK,
    'tops':B_TOPS,
    'bottoms':B_BOTTOMS,
    'shoes':B_SHOES}


SPRITE_POS = pg.Rect(288,150,68,116)







    
