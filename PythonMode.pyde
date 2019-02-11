from Player import Player
from Enemy import Enemy

def setup():
    global player, enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7
    size(500, 500)
    player = Player(width/2, height/2, 1)
    enemy1 = Enemy(width/2, height/2, 1)
    enemy2 = Enemy(width/2, height/2, 1)
    enemy3 = Enemy(width/2, height/2, 1)
                           
def draw():
    global player, enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7
    background(255)    
    player.animate()
    enemy1.animate()
    enemy2.animate()
    enemy3.animate()


    
def keyPressed():
    global player
    player.keyDown()
        
def keyReleased():
    global player
    player.keyUp()
