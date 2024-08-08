import pgzrun, random

TITLE="Bumblebee and Flowers"
WIDTH=400
HEIGHT=400
score=0
gameover=False

bee=Actor("bee")
bee.pos=100,100

flower=Actor("flower")
flower.pos=260,300

def draw():
    global score
    screen.blit('background',(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score:"+str(score),color="white",bottomleft=(50,50))
    if gameover:
        screen.fill("black")
        screen.draw.text("Game Over!!! Your final score is:"+str(score),color="red",fontsize=30,midtop=(WIDTH/2,10))

def time_up():
    global gameover
    gameover=True


def update():
    global score
    if keyboard.left:
        bee.x-=2
    if keyboard.right:
        bee.x+=2
    if keyboard.up:
        bee.y-=2
    if keyboard.down:
        bee.y+=2
    flowercollected=bee.colliderect(flower)
    if flowercollected:
        flower.x=random.randint(50,350)
        flower.y=random.randint(50,350)
        score+=10

clock.schedule(time_up,60)
pgzrun.go()