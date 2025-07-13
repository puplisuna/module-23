from turtle import *

class face:

    def __init__(self, xpos, ypos):
        self.size = 90
        self.coord = (xpos, ypos)
        self.nosesize = 'small'

    def setprize(self, radius):
        self.size = radius 

    def draw(self):
        self.gohome()
        pensize(3)
        speed(0)
        self.drawoutline()
        self.draweyes(135)
        self.draweyes(45)
        self.drawmouth()
        self.drawnose()
        pensize(5)

    def gohome(self):
        penup()
        goto(self.coord)
        setheading(0)

    def drawoutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.gohome()

    def draweyes(self, turn):
        penup()
        left(turn)
        forward(self.size / 2)
        pendown()
        dot(self.size / 10)
        self.gohome()

    def drawmouth(self):
        penup()
        right(135)
        forward(self.size / 1.7)
        left(90)
        pendown()
        circle(self.size / 1.7, 90)
        self.gohome()

    def drawnose(self):
        if self.nosesize == 'large':
            dot(self.size / 2, 'grey')
        elif self.nosesize == 'small':
            dot(self.size / 6, 'grey')
        else:
            dot(self.size / 4, 'grey')
        self.gohome()

# Create and draw the face
f1 = face(0, 0)
f1.draw()

showturtle()
done()