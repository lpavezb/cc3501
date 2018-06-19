from CC3501Utils import *
from models.bomb import *


class Bomberman(Figura):
    def __init__(self, pos=Vector(0, 0), vel=15, rgb=(1.0, 1.0, 1.0)):
        self.vel_x = Vector(vel, 0)
        self.vel_y = Vector(0, vel)
        self.a = 3.2
        self.can_place_bomb = True
        self.place_bomb_time = time.time()
        self.bombs = []
        self.w = 0
        self.h = 0
        super().__init__(pos, rgb)

    def figura(self):
        self.w = 5 * self.a
        self.h = 11.5 * self.a

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

    def place_bomb(self, timeout=0.5):
        if self.can_place_bomb:
            self.place_bomb_time = time.time()
            self.bombs.append(Bomb(pos=self.pos))
            self.can_place_bomb = False
        if time.time() - self.place_bomb_time > timeout:
            self.can_place_bomb = True

    def explode_bomb(self):
        for bomb in self.bombs:
            bomb.explode()

    def collide_left(self, wall):
        w_w = wall.w
        w_h = wall.h
        w_x = wall.pos.x
        w_y = wall.pos.y
        h = self.h
        x = self.pos.x
        y = self.pos.y
        if w_y <= y <= w_y+w_h:
            if w_x <= x <= w_x+w_w+1:
                self.pos.x = w_x + w_w + 1
                return True
        if y < w_y < y+h < w_y+w_h:
            if w_x <= x <= w_x+w_w+1:
                self.pos.x = w_x + w_w + 1
                return True
        return False

    def collide_right(self, wall):
        w_w = wall.w
        w_h = wall.h
        w_x = wall.pos.x
        w_y = wall.pos.y
        w = self.w
        h = self.h
        x = self.pos.x
        y = self.pos.y
        if w_y <= y <= w_y+w_h:
            if w_x <= x+w <= w_x+w_w:
                self.pos.x = w_x - w
                return True
        if y < w_y < y+h < w_y+w_h:
            if w_x <= x+w <= w_x+w_w:
                self.pos.x = w_x - w
                return True
        return False

    def collide_up(self, wall):
        w_w = wall.w
        w_h = wall.h
        w_x = wall.pos.x
        w_y = wall.pos.y
        w = self.w
        h = self.h
        x = self.pos.x
        y = self.pos.y
        if w_x <= x <= w_x+w_w:
            if w_y <= y+h <= w_y+w_h:
                self.pos.y = w_y-h
                return True
        if x < w_x < x+w < w_x+w_w:
            if w_y <= y+h <= w_y+w_h:
                self.pos.y = w_y - h
                return True
        return False

    def collide_down(self, wall):
        w_w = wall.w
        w_h = wall.h
        w_x = wall.pos.x
        w_y = wall.pos.y
        w = self.w
        h = self.h
        x = self.pos.x
        y = self.pos.y
        if w_x <= x <= w_x+w_w:
            if w_y <= y <= w_y+w_h+1:
                self.pos.y = w_y + w_h + 1
                return True
        if x < w_x < x+w < w_x+w_w:
            if w_y <= y <= w_y+w_h+1:
                self.pos.y = w_y + w_h + 1
                return True
        return False
