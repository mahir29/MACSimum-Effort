import pygame as pg
from Network import Network
from Player import *
import Config
from Ball import Ball
from _thread import *

width = Config.WindowWidth
height = Config.WindowHeight

win = pg.display.set_mode((width,height))
pg.display.set_caption("Client")
image = pg.image.load(r'images\bg.jpg')
#image = pg.transform.scale(pg.image.load(r'images\bg.jpg'), (width,height))


PlayerID=-1

def redrawWindow(win,players,ball):

    win.fill((255,255,255))
    win.blit(image, (0, 0))
    for p in players:
        if p.isActive:
            p.draw(win)
    ball.draw(win)
    pg.display.update()



def main():
    run=True
    n=Network()
    p=n.getP()
    global PlayerID
    PlayerID=p.id
    pg.display.set_caption("Player "+str(PlayerID+1))
    clock=pg.time.Clock()
    pg.mixer.music.load(r'sounds\mixkit-mystwrious-bass-pulse-2298.wav')
    pg.mixer.music.play(-1)
    while run:
        clock.tick(Config.FPS)
        data=n.send(p)
        for event in pg.event.get():
            if event.type ==pg.QUIT:
                run =False
                pg.quit()
        #print(data)
        p.move()
        redrawWindow(win,data[0],data[1])

main()
