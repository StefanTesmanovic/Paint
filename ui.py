import pygame
from pygame.locals import *
import pygame.locals
import os
import tkinter
from tkinter import filedialog
from tkinter import font
from tkinter import *

pygame.init()

screenw = 500
screenh = 100
active_size = 0     #za odabir velicine
active_color = 0    #za odabir boja
active_click = 0
x = 0
y = 0
visina_menu = 50
boje_dole = screenh-100

screen = pygame.display.set_mode((screenw, screenh), RESIZABLE)
pygame.display.set_caption("Paint")
screen.fill((255, 255, 255))



def header(screen):      #gornji menu, nema nista na njemu
    pygame.draw.rect (screen, 'gray' ,[0, 0, 2500, 100])
    
#===========================================================================================================================
    
def menu(screen):        #u ovoj funkciji su sve slike (save, save as, undo, redo...), kvadrati za odabir debljine i desni menu
    pygame.draw.rect (screen, 'gray' ,[0, 0, 165, 2500])
    
    save = pygame.image.load(r"C:\Users\admin\Documents\PaintPetnica\save+icon-1320167995084087448.png")
    save1 = pygame.transform.scale(save,(100,100))
    s = pygame.draw.rect (screen, 'gray', [10,0,100,100])
    
    save_as = pygame.image.load(r"C:\Users\admin\Documents\PaintPetnica\save-as-icon-9.jpg")
    save_as1 = pygame.transform.scale (save_as,(140,140))
    s_a = pygame.draw.rect (screen, 'gray', [130,-13,110,110])
    
    undo = pygame.image.load(r"C:\Users\admin\Documents\PaintPetnica\img_518924.png")
    undo1 = pygame.transform.scale (undo,(90,90))
    u = pygame.draw.rect (screen, 'gray', [253,-3,100,100])
    
    redo = pygame.image.load(r"C:\Users\admin\Documents\PaintPetnica\img_93928.png")
    redo1 = pygame.transform.scale (redo,(90,90))
    r = pygame.draw.rect (screen, 'gray', [358,-3,100,100])
        
    brush = pygame.image.load(r"C:\Users\admin\Documents\PaintPetnica\103414.png")
    brush1 = pygame.transform.scale (brush,(85,85))
    b = pygame.draw.rect (screen, 'gray', [10,110,100,90])
    
    rubber = pygame.image.load(r"C:\Users\admin\Documents\PaintPetnica\3261131-200.png")
    rubber1 = pygame.transform.scale (rubber,(90,90))
    rub = pygame.draw.rect (screen, 'gray', [60,210,100,90])
    
    line = pygame.image.load(r"C:\Users\admin\Documents\PaintPetnica\177506-200.png")
    line1 = pygame.transform.scale (line,(90,90))
    l = pygame.draw.rect (screen, 'gray', [10,320,100,90])
    
    text = pygame.image.load(r"C:\Users\admin\Documents\PaintPetnica\text.png")
    text1 = pygame.transform.scale (text,(90,90))
    t = pygame.draw.rect (screen, 'gray', [60,420,90,90])
    
    d_component_list = [b,rub,l,t]
    s_component_list = [s, s_a]
    u_component_list = [u,r]
    
    xl = pygame.draw.rect (screen, (0,0,0), [1220,10, 70, 70])
    pygame.draw.rect (screen, (255,255,255), [1247,35,16,16])
    l = pygame.draw.rect (screen, (0,0,0), [1300,10, 70, 70])
    pygame.draw.rect (screen, (255,255,255), [1328,38,12,12])
    m = pygame.draw.rect (screen, (0,0,0), [1380,10, 70, 70])
    pygame.draw.rect (screen, (255,255,255), [1410,41,8,8])
    s = pygame.draw.rect (screen, (0,0,0), [1460,10, 70, 70])
    pygame.draw.rect (screen, (255,255,255), [1493,44,4,4])
    brush_list = [xl, l, m, s]
    
    screen.blit(save1, (10, 0))
    screen.blit(save_as1, (110,-20))
    screen.blit(redo1, (260,5))
    screen.blit(undo1,(360,7))
    screen.blit(brush1,(20, 110))
    screen.blit(rubber1,(60, 210))
    screen.blit(line1,(10, 320))
    screen.blit(text1,(60, 420))
    
    return brush_list, d_component_list, s_component_list, u_component_list

#===========================================================================================================
    
def boje():             #sve boje su ovde
    blue = pygame.draw.rect (screen, (0,0,255), [20, 710, 50, 50])
    yellow = pygame.draw.rect (screen, (255,255,0), [85, 710, 50, 50])
    green = pygame.draw.rect (screen, (26,148,49), [20, 650, 50, 50])
    red = pygame.draw.rect (screen, (255,0,0), [85, 650, 50, 50])
    black = pygame.draw.rect (screen, (0,0,0), [20, 590, 50, 50])
    purple = pygame.draw.rect (screen, (106,13,173), [85, 590, 50, 50])
    color_rect = [blue, yellow, green, red, black, purple]
    rgb_list = [(0,0,255),(255,255,0),(26,148,49),(255,0,0),(0,0,0),(106,13,173)]
    return color_rect,rgb_list

#===========================================================================================================
saved = False
ime = ""

def sejvuj():    
    global saved
    global ime

    if saved:
        root = Tk()
        root.withdraw()
        
        filePath = filedialog.asksaveasfilename(defaultextension='.png',
                                                 filetypes=[
                                                     ('PNG file','.png')
                                                 ])
        os.system("del /f "+filePath)
        pygame.image.save(screen, filePath)
    else:   
        root = Tk()
        root.withdraw()

        filePath = filedialog.asksaveasfilename(defaultextension='.png',
                                                 filetypes=[
                                                     ('PNG file','.png')
                                                 ])

        #ime = input("Unesite ime: ")
        pygame.image.save(screen, filePath)
        saved = True
    
    
#===========================================================================================================

    #mouse = pygame.mouse.get_pos()                     #ovo ti ide posle screen.filla
    #header()
    #brushes, components = menu()
    #colors,rgb_list = boje()
    #pygame.display.flip()
    #for event in pygame.event.get():
        #if event.type == pygame.QUIT:
            #running = False
            #pygame.quit()
            
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #for i in range(len(brushes)):
                #if brushes[i].collidepoint(event.pos):
                    #active_size = 16 - (i*4)
                    
            #for i in range(len(colors)):
                #if colors[i].collidepoint(event.pos):
                    #active_color = rgb_list[i]
                    
#=======================================================================================================
'''
running = True
while running:
    screen.fill((255, 255, 255))
    mouse = pygame.mouse.get_pos()
    #if mouse[1] < 100
    header(screen)
    #brush()
    #rubber()
    #floodFill()
    brushes, d_component_list, s_component_list, u_component_list = menu(screen)
    colors,rgb_list = boje()
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(brushes)):
                if brushes[i].collidepoint(event.pos):
                    active_size = 16 - (i*4)
                            
            for i in range(len(colors)):
                if colors[i].collidepoint(event.pos):
                    active_color = rgb_list[i]
                    
            for i in range(len(d_component_list)):
                if d_component_list[i].collidepoint(event.pos):
                    active_click1 = d_component_list[i]
                    
            for i in range(len(s_component_list)):
                if s_component_list[i].collidepoint(event.pos):
                    active_click2 = s_component_list[i]
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(s_component_list)):
                if s_component_list[i].collidepoint(event.pos):
                    sejvuj()
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (len(d_component_list)):
                if d_component_list[i].collidepoint(event.pos):
                    pass
                    # OVDE SAM TI OSTAVIO DA DODAS FUNKCIJE ZA CRTANJE,BRISANJE I TEKST
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (len(u_component_list)):
                if u_component_list[i].collidepoint(event.pos):
                    pass
                    # OVDE SAM TI OSTAVIO DA DODAS FUNKCIJE ZA UNDO I REDO
             
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                sejvuj()'''
                
    