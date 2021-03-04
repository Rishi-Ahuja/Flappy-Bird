import pgzrun
import random
import time
WIDTH=1200
HEIGHT=800
bird=Actor('bird')
grass=Actor('ground')
mountain=Actor('mountain')
mountain2=Actor('mountain')
mountain.pos=600,400
mountain2.pos=1800,400
grass.pos=600,510
play=Actor('play')
play.pos=3000,3000
cloud=Actor('cloud')
cloud.pos=500,500
cloud2=Actor('cloud')
cloud2.pos=1800,500
restart=Actor('restart')
restart.pos=3000,3000
game=False
score=0
bird.pos=600,200
walls=[]
for x in range (0,10):
    wall=Actor('wall')
    walls.append(wall)
for a in range (0,len(walls)):
          walls[a].pos=random.randint(1500,1800)+(a*400),random.choice([150,650])

    
def start():
    global score,game
    restart.pos=3000,3000
    game=True
    score=0
    bird.pos=600,200
    for a in range (0,len(walls)):
          walls[a].pos=random.randint(1500,1800)+(a*300),random.choice([150,650])

def draw():
    global count
    screen.blit('air',(0,0))
    screen.draw.text("Score-:"+str(score),color='black',topleft=(10,10),fontsize=40)
    mountain.draw()
    mountain2.draw()
    grass.draw()
    cloud.draw()
    cloud2.draw()
    for b in range(0,10):
        walls[b].draw()
        
    bird.draw()
    
    if game=='over':
        restart.pos=600,400
        restart.draw()
        screen.draw.text("Restart",color='black',topleft=(560,450),fontsize=40)
        screen.draw.text("GAME OVER",color='black',topleft=(440,250),fontsize=80)
    if game==False:
        play.draw()
        play.pos=600,300
        screen.draw.text("Start",color='black',topleft=(560,350),fontsize=40)
        screen.draw.text("How to Play? -: Press space key to move up. Press start button to start",color='black',topleft=(200,400),fontsize=40)
        screen.draw.text("FLAPPY BIRD",topleft=(430,100),fontsize=80,color='red')

def on_mouse_down(pos):
    global game 
    if restart.collidepoint(pos):
        game=True
        start()
    if play.collidepoint(pos):
        game=True
        start()

def on_key_up(key):
    if game==True:
      if key==key.SPACE:
        bird.y=bird.y-100
     
def update():
    global game,score
    if game==True:
     for c in range(0,10):
         walls[c].x=walls[c].x-5
         if walls[c].x<0:
                walls[c].pos=random.randint(1200,1500)+(a*300),random.choice([150,650])
                score=score+1
         if bird.colliderect(walls[c]):
             game='over'
                
     if bird.y>0 and bird.y<800:
        bird.y=bird.y+4
     else:
         game='over'
     cloud.x=cloud.x-2
     cloud2.x=cloud2.x-2
     mountain.x=mountain.x-2
     mountain2.x=mountain2.x-2
     if cloud.x==-100 :
        cloud.x=1800
     if cloud2.x==-100:
        cloud.x=1800
     if mountain.x==-450 :
        mountain.x=1800
     if mountain2.x==-450:
        mountain2.x=1800
    

pgzrun.go()
