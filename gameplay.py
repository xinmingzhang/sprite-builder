import pygame as pg
import prepare

from state_engine import GameState


class Gameplay(GameState):
    try:
        pg.mixer.music.load(prepare.BG_M)
        pg.mixer.music.set_volume(0.5)
        pg.mixer.music.play(-1)
    except:
        pass
    def __init__(self):
        super(Gameplay, self).__init__()

        self.hair = None
        self.facial_hair = None
        self.skin = prepare.SKIN[0]
        self.eyes = None
        self.hat= None
        self.mask = None
        self.tops = None
        self.bottoms = None
        self.shoes = None

        self.background = None

        self.cursor = 0

        self.style_change = False
        self.color_change = False
        self.delete_change = False
        self.change_step = 1


    def change_list(self,whole_list,current_state,step):
        for i in range(len(whole_list)):
            if whole_list[i]==current_state:
                return whole_list[(i+step)%len(whole_list)]
        return whole_list[0]

    def change_array(self,whole_list,current_state,change,step):
        for i in range(len(whole_list)):
            for j in range(len(whole_list[i])):
                if whole_list[i][j]==current_state:
                    if change == 'color':
                        return whole_list[(i+step)%len(whole_list)][j]
                    elif change == 'style':
                        return whole_list[i][(j+step)%len(whole_list[i])]
        return whole_list[0][0]

    def get_event(self,event):
        x,y = pg.mouse.get_pos()
        if event.type == pg.QUIT:
            self.quit = True

        elif event.type == pg.MOUSEBUTTONDOWN:
            
            if event.button == 1:
                self.style_change = True
                self.change_step = 1
            elif event.button == 3:
                self.style_change = True  
                self.change_step = -1
            elif event.button == 4:
                self.color_change = True
                self.change_step = 1
            elif event.button == 5:
                self.color_change = True
                self.change_step = -1
            elif event.button == 2:
                self.delete_change = True

            
            if prepare.BUTTON_RESET.collidepoint(x,y):
                self.hair = None
                self.facial_hair = None
                self.skin = prepare.SKIN[0]
                self.eyes = None
                self.hat= None
                self.mask = None
                self.tops = None
                self.bottoms = None
                self.shoes = None
                self.background = None
            elif prepare.BUTTON_SAVE.collidepoint(x,y):
                pg.image.save(self.image,'my_sprite0.png')
            elif prepare.BUTTON_HELP.collidepoint(x,y):
                self.done = True
                self.next_state = "INFO"
            elif prepare.BUTTON_SHOW.collidepoint(x,y):
                self.done = True
                self.next_state = "SHOW"
            elif prepare.BUTTON_QUIT.collidepoint(x,y):
                self.quit = True



        elif event.type == pg.MOUSEBUTTONUP:
            self.style_change = False

            self.delete_change = False
            



        elif event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                self.quit = True
                
    def update(self, dt):

        x,y = pg.mouse.get_pos()

        if self.style_change == True:
            if prepare.B_HAT.collidepoint(x,y):
                if self.hat == None:
                    self.hat = prepare.HATS[0][0]
                else:
                    self.hat = self.change_array(prepare.HATS,self.hat,'style',self.change_step)
                self.style_change = False
            elif prepare.B_S_HAT.collidepoint(x,y):
                if self.hat == None:
                    self.hat = prepare.SPECIAL_HATS[0]
                else:
                    self.hat = self.change_list(prepare.SPECIAL_HATS,self.hat,self.change_step)
                self.style_change = False
            elif prepare.B_MASK.collidepoint(x,y):
                if self.mask == None:
                    self.mask = prepare.MASKS[0][0]
                else:
                    self.mask = self.change_array(prepare.MASKS,self.mask,'style',self.change_step)
                self.style_change = False
            elif prepare.B_S_MASK.collidepoint(x,y):
                if self.mask == None:
                    self.mask = prepare.SPECIAL_MASKS[0]
                else:
                    self.mask = self.change_list(prepare.SPECIAL_MASKS,self.mask,self.change_step)
                self.style_change = False
            elif prepare.B_TOPS.collidepoint(x,y):
                if self.tops == None:
                    self.tops = prepare.TOPS[0][0]
                else:
                    self.tops = self.change_array(prepare.TOPS,self.tops,'style',self.change_step)
                self.style_change = False
            elif prepare.B_BOTTOMS.collidepoint(x,y):
                if self.bottoms == None:
                    self.bottoms = prepare.BOTTOMS[0][0]
                else:
                    self.bottoms = self.change_array(prepare.BOTTOMS,self.bottoms,'style',self.change_step)
                self.style_change = False
            elif prepare.B_BACKGROUND.collidepoint(x,y):
                if self.background == None:
                    self.background = prepare.BACKGROUND[0]
                else:
                    self.background = self.change_list(prepare.BACKGROUND,self.background,self.change_step)
                self.style_change = False
            elif prepare.B_EYES.collidepoint(x,y):
                if self.eyes == None:
                    self.eyes = prepare.EYES[0]
                else:
                    self.eyes = self.change_list(prepare.EYES,self.eyes,self.change_step)
                self.style_change = False
            elif prepare.B_F_HAIR.collidepoint(x,y):
                if self.facial_hair == None:
                    self.facial_hair = prepare.FACIAL_HAIR[0][0]
                else:
                    self.facial_hair = self.change_array(prepare.FACIAL_HAIR,self.facial_hair,'style',self.change_step)
                self.style_change = False
            elif prepare.B_HAIR.collidepoint(x,y):
                if self.hair == None:
                    self.hair = prepare.HAIR[0][0]
                else:
                    self.hair = self.change_array(prepare.HAIR,self.hair,'style',self.change_step)
                self.style_change = False
            elif prepare.B_SKIN.collidepoint(x,y):
                self.skin = self.change_list(prepare.SKIN,self.skin,self.change_step)
                self.style_change = False
            elif prepare.B_SHOES.collidepoint(x,y):
                if self.shoes == None:
                    self.shoes = prepare.SHOES[0]
                else:
                    self.shoes = self.change_list(prepare.SHOES,self.shoes,self.change_step)
                self.style_change = False
            else:
                self.style_change = False

        if self.color_change == True:
            if prepare.B_HAT.collidepoint(x,y):
                if self.hat == None:
                    self.hat = prepare.HATS[0][0]
                    self.color_change = False
                else:
                    self.hat = self.change_array(prepare.HATS,self.hat,'color',self.change_step)
                self.color_change = False
            elif prepare.B_MASK.collidepoint(x,y):
                if self.mask == None:
                    self.mask = prepare.MASKS[0][0]
                    self.color_change = False
                else:
                    self.mask = self.change_array(prepare.MASKS,self.mask,'color',self.change_step)
                    self.color_change = False
            elif prepare.B_TOPS.collidepoint(x,y):
                if self.tops == None:
                    self.tops = prepare.TOPS[0][0]
                    self.color_change = False
                else:
                    self.tops = self.change_array(prepare.TOPS,self.tops,'color',self.change_step)
                self.color_change = False
            elif prepare.B_BOTTOMS.collidepoint(x,y):
                if self.bottoms == None:
                    self.bottoms = prepare.BOTTOMS[0][0]
                    self.color_change = False
                else:
                    self.bottoms = self.change_array(prepare.BOTTOMS,self.bottoms,'color',self.change_step)
                    self.color_change = False
            elif prepare.B_F_HAIR.collidepoint(x,y):
                if self.facial_hair == None:
                    self.facial_hair = prepare.FACIAL_HAIR[0][0]
                    self.color_change = False
                else:
                    self.facial_hair = self.change_array(prepare.FACIAL_HAIR,self.facial_hair,'color',self.change_step)
                self.color_change = False
            elif prepare.B_HAIR.collidepoint(x,y):
                if self.hair == None:
                    self.hair = prepare.HAIR[0][0]
                    self.color_change = False
                else:
                    self.hair = self.change_array(prepare.HAIR,self.hair,'color',self.change_step)
                    self.color_change = False
            else:
                self.color_change = False

        if self.delete_change == True:
            if prepare.B_HAT.collidepoint(x,y):
                self.hat = None

                self.delete_change = False
            elif prepare.B_S_HAT.collidepoint(x,y):
                self.hat = None
                
                self.delete_change = False
            elif prepare.B_MASK.collidepoint(x,y):
                self.mask = None
                    
                self.delete_change = False
            elif prepare.B_S_MASK.collidepoint(x,y):
                self.mask = None
                    
                self.delete_change = False
            elif prepare.B_TOPS.collidepoint(x,y):
                self.tops = None
                   
                self.delete_change = False
            elif prepare.B_BOTTOMS.collidepoint(x,y):
                self.bottoms = None
                   
                self.delete_change = False
            elif prepare.B_BACKGROUND.collidepoint(x,y):
                self.background = None
                    
                self.delete_change = False
            elif prepare.B_EYES.collidepoint(x,y):
                self.eyes = None
                    
                self.delete_change = False
            elif prepare.B_F_HAIR.collidepoint(x,y):
                self.facial_hair = None
                    
                self.delete_change = False
            elif prepare.B_HAIR.collidepoint(x,y):
                self.hair = None
                    
                self.delete_change = False

            elif prepare.B_SHOES.collidepoint(x,y):
                self.shoes = None
                    
                self.delete_change = False
            else:
                self.delete_change = False

    def draw(self, surface):
        surface.blit(prepare.BG_IMAGE,(0,0))
        self.image = pg.Surface((68,116),pg.SRCALPHA)

        if self.cursor == 0:
            prepare.change_cursor('default')
        elif self.cursor == 1:
            prepare.change_cursor('hand')
        elif self.cursor == 2:
            prepare.change_cursor('move')


        for cursor_change_bug in ['It is really a weird bug']:
            self.cursor =0
        x,y = pg.mouse.get_pos()
        for button in prepare.BUTTON_DICT:
            if prepare.BUTTON_DICT[button].collidepoint(x,y):
                self.cursor = 1
                pg.draw.line(surface,(0,0,255),\
                             prepare.BUTTON_DICT[button].bottomleft,\
                             prepare.BUTTON_DICT[button].bottomright,2)

                
        for button in prepare.B_DICT:
            if prepare.B_DICT[button].collidepoint(x,y):
                self.cursor = 2
                pg.draw.rect(surface,(0,0,255),prepare.B_DICT[button],2)



        if self.background != None:
            self.image_bg = self.image.copy()
            self.image_bg.fill(self.background)
            surface.blit(self.image_bg,prepare.SPRITE_POS.topleft)
        self.image.blit(self.skin,(0,0))

        if self.hair != None:
            self.image.blit(self.hair,(0,0))
        if self.facial_hair != None:
            self.image.blit(self.facial_hair,(0,0))
        if self.eyes != None:
            self.image.blit(self.eyes,(0,0))        
        if self.hat != None:
            self.image.blit(self.hat,(0,0))
        if self.mask != None:
            self.image.blit(self.mask,(0,0))
        if self.tops != None:
            self.image.blit(self.tops,(0,0))
        if self.bottoms != None:
            self.image.blit(self.bottoms,(0,0))
        if self.shoes != None:
            self.image.blit(self.shoes,(0,0))



        surface.blit(self.image,prepare.SPRITE_POS.topleft)   

        


class Info(GameState):
    def __init__(self):
        super(Info,self).__init__()


    def get_event(self,event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
            self.next_state = "GAMEPLAY" 
        elif event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                self.quit = True

    def draw(self, surface):
        prepare.change_cursor('default')
        surface.blit(prepare.HELP_IMAGE,(0,0))


class Show(GameState):
    def __init__(self):
        super(Show,self).__init__()
        self.image = None
        self.image_load_error = 'Ooh,please save your own sprite first! ^V^'
        self.timer = 0
        self.bg_color = prepare.BACKGROUND[0]
        
    

    def get_event(self,event):
        if event.type == pg.QUIT:
            self.quit = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.done = True
            self.next_state = "GAMEPLAY" 
        elif event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                self.quit = True

    def print_text(self,surface,centerposition,text,size,colour,bg_colour=None):
        font_layer = pg.font.Font(prepare.MY_FONT,size)
        font_surface = font_layer.render(text,True,colour,bg_colour)
        w,h = font_surface.get_size()
        position = centerposition[0]-w/2,centerposition[1]-h/2
        surface.blit(font_surface,position)

    def draw(self,surface):
        try:
            self.image = pg.image.load('my_sprite0.png').convert_alpha()
            
        except:
            self.image = None
        
        prepare.change_cursor('default')
        surface.fill(self.bg_color)
        if self.image == None:
            w,h = surface.get_size()
            self.print_text(surface,(w/2,h/2),self.image_load_error,16,(0,0,0))
        else:
            w,h = self.image.get_size()
            self.image0 = pg.transform.scale(self.image, (int(w*4), int(h*4)))
            self.image1 = pg.transform.scale(self.image0, (int(w*2), int(h*2)))
            self.image2 = pg.transform.scale(self.image1, (int(w), int(h)))
            self.image3 = pg.transform.scale(self.image2, (int(w/2), int(h/2)))
            self.image4 = pg.transform.scale(self.image3, (int(w/4), int(h/4)))

            surface.blit(self.image0,(0,0))
            surface.blit(self.image1,(4*w,0))
            surface.blit(self.image2,(6*w,0))
            surface.blit(self.image3,(7*w,0))
            surface.blit(self.image4,(int(7.5*w),0))
            

    def update(self,dt):
        self.timer += dt/500
        self.bg_color = prepare.BACKGROUND[int(self.timer)%len(prepare.BACKGROUND)]






