class Enemy:
    
    # instance variables
    left = True
    right = True
    up = True
    down = True
    speed1 = random(1, 10)
    speed2 = random(1, 10)
    speed3 = random(1, 10)
    speed4 = random(1, 10)
    diameter = 50
    
    # constructor
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    # instance methods
    def display(self):
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def move(self):
        self.speed1 = random(-30, 30)
        self.speed2 = random(-30, 30)
        self.speed3 = random(-30, 30)
        self.speed4 = random(-30, 30)
        if self.left:
            self.x -= self.speed1
        if self.right:
            self.x += self.speed2
        if self.up:
            self.y -= self.speed3
        if self.down:
            self.y += self.speed4
        self.x = constrain(self.x, self.diameter / 2, width - self.diameter / 2)
        self.y = constrain(self.y, self.diameter / 2, height - self.diameter / 2)
    
    def animate(self):
        self.display()
        self.move()
