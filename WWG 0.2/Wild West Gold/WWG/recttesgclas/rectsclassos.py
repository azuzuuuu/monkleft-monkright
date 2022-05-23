from random import randint
import pygame as pg
from sys import exit
from tkinter import Tk
import ctypes as ct
from random import randint
import time


DEBUG = False
FULLSCREEN = False
running = True
screen_width, screen_height = Tk().winfo_screenwidth(), Tk().winfo_screenheight()
res = (screen_width, screen_height) if FULLSCREEN else (1200, 800)
mid_screen = (res[0] // 2, res[1] // 2)



pg.init()
screen = pg.display.set_mode(res, pg.FULLSCREEN) if FULLSCREEN else pg.display.set_mode(res)
pg.display.set_caption('Monkleft or Monkright')
gui_font = pg.font.Font(None,30)
clock = pg.time.Clock()
bet_balance = 100.0
bet_pose = 0.0
bet_win = 0.0
line = -5
haut = 0
bet_on = True
commence = False
canbet = True
pg.display.set_icon(pg.image.load('WWG 0.2\Wild West Gold\WWG\images\logobg.png'))



class Gui():
    def __init__(self):
        self.text_screen = number_font.render(str(bet_balance)+'¥', True, 'white')
        self.text_screenbet = number_font.render(str(bet_pose)+'¥', True, 'white')
        self.text_screenwin = number_font.render(str(bet_win)+'¥', True, 'white')
        self.background_rect = pg.Rect(700,0,500,800)

        self.b1 = Button('      ',100, 50,(100, 650),5,10,self)
        self.b2 = Button('      ',100, 50,(500, 650),5,10, self)
        self.b3 = Button('      ',100, 50,(100, 550),5,11, self)
        self.b4 = Button('      ',100, 50,(500, 550),5,11, self)
        self.b5 = Button('      ',100, 50,(100, 450),5,12, self)
        self.b6 = Button('      ',100, 50,(500, 450),5,12, self)
        self.b7 = Button('      ',100, 50,(100, 350),5,13, self)
        self.b8 = Button('      ',100, 50,(500, 350),5,13, self)
        self.b9 = Button('      ',100, 50,(100, 250),5,14, self)
        self.b10 = Button('      ',100, 50,(500, 250),5,14, self)
        self.b11 = Button('      ',100, 50,(100, 150),5,15, self)
        self.b12 = Button('      ',100, 50,(500, 150),5,15, self)
        self.b13 = Button('      ',100, 50,(100, 50),5,16, self)
        self.b14 = Button('      ',100, 50,(500, 50),5,16, self)
        self.bjouer = Button(' MonkeBet ',400, 80,(750, 300),5,-5,self)
        self.hundred_button = Button('100',50,50,(1070,475),0,3, self)
        self.ten_button = Button('10',50,50,(1000,475),0,2, self)
        self.one_button = Button('1',50,50,(930,475),0,1, self)
        self.cents_button = Button('0.1',50,50,(860,475),0,0, self)
        self.x_button = Button('X',50,50,(790,475),0,-2, self)
        self.ret = Button('  Retirer  ',100, 50,(300, 700),5,150, self)
    def reset_text(self):
        self.text_screen = number_font.render(str(bet_balance)+'¥', True, 'white')
        self.text_screenbet = number_font.render(str(bet_pose)+'¥', True, 'white')
        self.text_screenwin =  number_font.render(str(bet_win)+'¥', True, 'white')

    def update(self):

        pg.draw.rect(screen, (16,16,16), self.background_rect)
        pg.draw.line(screen, (15,15,15), (700, 0), (700,800), 7)
        x = 0
        calc = 2
        for i in range(7):
            calcul = 'x' + str(calc)
            pg.draw.line(screen, '#fdec96', (120, 675-x), (520,675-x), 7)

            screen.blit(small_font.render(calcul, False, 'white'),(50,665-x))
            screen.blit(small_font.render(calcul, False, 'white'),(640,665-x))
            calc = calc*2
            x+=100

        screen.blit(pg.image.load('WWG 0.2\Wild West Gold\WWG\images\logobg2.png').convert_alpha(),(700,-70))
        pg.draw.rect(screen, (20,20,20), pg.Rect(770, 575, 380,60), border_radius=6)
        pg.draw.rect(screen, (20,20,20), pg.Rect(770, 675, 380,60), border_radius=6)
        screen.blit(pg.transform.scale(pg.image.load('WWG 0.2\Wild West Gold\WWG\images\yen.png').convert_alpha(),(50,50)),(850,400))
        screen.blit(self.text_screen,(910,390))
        screen.blit(self.text_screenbet,(965,570))
        screen.blit(self.text_screenwin,(965,670))
        screen.blit(big_font.render('Mise :', True, 'white'),(800,570))
        screen.blit(big_font.render('Gains :', True, 'white'),(800,670))

        pg.draw.rect(screen, 'white', pg.Rect(745,290,410,90),0,10)



        self.b1.draw()
        self.b2.draw()
        self.b3.draw()
        self.b4.draw()
        self.b5.draw()
        self.b6.draw()
        self.b7.draw()
        self.b8.draw()
        self.b9.draw()
        self.b10.draw()
        self.b11.draw()
        self.b12.draw()
        self.b13.draw()
        self.b14.draw()
        self.bjouer.draw()
        self.hundred_button.draw()
        self.ten_button.draw()
        self.one_button.draw()
        self.cents_button.draw()
        self.x_button.draw()
        self.ret.draw()
        #if perdu:
        #    bperdu.draw



class Button: 
    def __init__(self,text,width,height,pos,elevation,index,receiver=None):
        self.triggered = False
        self.pressed = False
        self.elevation = elevation
        self.decalage = elevation
        self.receiver = receiver
        self.pos_y = pos[1]
        self.index = index
        self.lancer = False
        self.text = text

        self.reset = True
        self.top_rect = pg.Rect(pos,(width,height))
        self.top_color = '#392E5C'

        self.bottom_rect = pg.Rect(pos,(width,height))
        self.aretirer = True
        self.calc = 2

        if self.index == -5:
            self.bottom_color = (255,255,255) 
        
        
        
        else:
            self.bottom_color = '#fdec96'        

       
            
        self.text_surf = gui_font.render(text,True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        self.abletoreset = False

    def adding(self):
        global bet_on
        global bet_balance
        global bet_pose
        global bet_win
        if bet_on and canbet:
            change = [0.1,1,10,100]
            if self.index >= 0 and self.index <= 3:
                if bet_balance <100 and self.index == 3:
                    pass
                elif bet_balance <10 and self.index == 2:
                    pass
                
                elif bet_balance <1 and self.index == 1:
                    pass
                
                elif bet_balance <=0 and self.index == 0:
                    pass

                else:
                    bet_balance = round(bet_balance-change[self.index],1)
                    bet_pose = round(bet_pose+change[self.index],1)

            elif self.index == -2:
                bet_balance = round(bet_balance+bet_pose,1)
                bet_pose = 0.0
            self.receiver.reset_text()
            
            

    def draw(self):
        # elevation
        
        self.top_rect.y = self.pos_y - self.decalage
        self.text_rect.center = self.top_rect.center 

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.decalage

        pg.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = 12)
        pg.draw.rect(screen,self.top_color, self.top_rect,border_radius = 12)
        screen.blit(self.text_surf, self.text_rect)
        self.check_click()
        
        if self.reset and self.index > 9 and not bet_on:
            self.bottom_color = '#fdf496'
        

    def check_click(self):
        global canbet
        global line
        global haut
        global bet_balance
        global bet_pose
        global bet_win
        global bet_on
        global commence
        mouse_pos = pg.mouse.get_pos()
        
            
        if self.top_rect.collidepoint(mouse_pos):
            if self.index == -5:
                self.top_color = '#ffffff'
                self.text_surf = gui_font.render(self.text,True,(0,0,0))

            else:
                self.top_color = '#fdf496'
                
            
            
            if event.type == pg.MOUSEBUTTONDOWN and self.triggered==False:
                
                

                self.decalage = 0
                self.pressed = True
                self.adding()
                self.triggered = False

                self.decalage = self.elevation
                if self.pressed == True:
                    
                    
                    if self.index == line:
                        
                        self.calc = 2
                        if reponse == 1 and self.index > 9:
                            self.bottom_color = (0,255,0)
                            self.aretirer = True
                            line += 1
                            bet_on = True
                            

                        elif reponse == 2 and self.index > 9: 
                            bet_win -= bet_pose                       
                            bet_pose = 0.0
                            self.bottom_color = (255,0,0)
                            line = -5
                            bet_on = True
                            canbet = True
                            commence = False     
                            
                        self.pressed = False

                        if self.index == -5 and commence == False and bet_pose>0.0:
                            bet_on = False
                            canbet = False
                            line = 10
                            commence = True
                            self.reset =True
                            self.aretirer=True
                            

                    if self.index ==150 and self.aretirer==True and commence and line!=10:
                        
                        self.calc = 2**(line-10)
                        bet_win += bet_pose * self.calc
                        bet_balance +=  bet_pose * self.calc
                        bet_pose = 0.0
                        line = -5
                        bet_on = True
                        canbet = True
                        commence = False
                        
                             
                
                                       

                self.triggered = True
                pg.time.wait(100)
                self.triggered =  False
                
                            
                        

                        
        else:
            self.decalage = self.elevation
            if self.index == -5:
                self.top_color = (16,16,16) 
                

            
            else:
                self.top_color = (25,25,25)
            self.text_surf = gui_font.render(self.text,True,'#FFFFFF')
               

number_font = pg.font.Font("WWG 0.2\Wild West Gold\WWG\images\Poppins2.ttf", 50)
big_font = pg.font.Font("WWG 0.2\Wild West Gold\WWG\images\Poppins2.ttf", 45)
small_font = pg.font.Font("WWG 0.2\Wild West Gold\WWG\images\Poppins2.ttf", 20)

gui = Gui()
#img = MyImage()

while running:
    reponse = randint(1,2)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
    

                
    screen.fill((20,20,20))
    
    gui.update()
    clock.tick(60)

    pg.display.update()