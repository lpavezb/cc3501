from CC3501Utils import *
from models.bomb import *


class Bomberman(Figura):
    def __init__(self, pos=Vector(0, 0), vel=20, rgb=(1.0, 1.0, 1.0)):
        self.vel_x = Vector(vel, 0)
        self.vel_y = Vector(0, vel)
        self.a = 6
        self.bombs = []
        super().__init__(pos, rgb)

    def figura(self):
        glBegin(GL_QUADS)

        # head
        glColor3f(1, 1, 1)
        self.rect(1, 8.5, 3, 2)

        # eyes
        glColor3f(0, 0, 0)
        self.rect(1.75, 9, 0.5, 0.5)
        self.rect(2.75, 9, 0.5, 0.5)

        # torso
        glColor3f(0.5, 0.5, 0.5)
        self.rect(2, 2.5, 1, 6)
        self.rect(0, 6.5, 5, 1)

        # arms
        glColor3f(0, 0, 0)
        self.rect(0, 3.5, 1, 4)
        self.rect(4, 3.5, 1, 4)

        # hands
        self.rect(0, 2.5, 0.3, 1)
        self.rect(0.7, 2.5, 0.3, 1)

        self.rect(4, 2.5, 0.3, 1)
        self.rect(4.7, 2.5, 0.3, 1)

        # base
        glColor3f(0.7, 0, 0)
        self.rect(1, 0.5, 3, 2)

        # wheels
        glColor3f(0, 0, 0)
        self.rect(1, 0, 1, 0.5)
        self.rect(3, 0, 1, 0.5)

        # antenna
        self.rect(0.7, 9.5, 0.3, 1.5)
        self.rect(4, 9.5, 0.3, 1.5)

        glColor3f(0.7, 0, 0)
        self.rect(0.6, 11, 0.5, 0.5)
        self.rect(3.9, 11, 0.5, 0.5)

        glEnd()

    def mover(self, dt, move_right, move_left, move_up, move_down):
        if move_up:
            self.pos = sumar(self.pos, ponderar(dt, self.vel_y))
        if move_down:
            self.pos = sumar(self.pos, ponderar(-1 * dt, self.vel_y))
        if move_right:
            self.pos = sumar(self.pos, ponderar(dt, self.vel_x))
        if move_left:
            self.pos = sumar(self.pos, ponderar(-1 * dt, self.vel_x))

        # limits
        if self.pos.x < 0:
            self.pos.x = 0
        if self.pos.y < 0:
            self.pos.y = 0
        if self.pos.x > 780:
            self.pos.x = 780
        if self.pos.y > 580:
            self.pos.y = 580

    def rect(self, x1, y1, w, h):
        a = self.a

        glVertex2f(x1 * a, y1 * a)
        glVertex2f(x1 * a, (y1 + h) * a)
        glVertex2f((x1 + w) * a, (y1 + h) * a)
        glVertex2f((x1 + w) * a, y1 * a)

    def place_bomb(self):
        b = Bomb()
        self.bombs.append(b)
