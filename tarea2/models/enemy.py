from models.bomb import *
import math


class Enemy(Figura):
    def __init__(self, pos=Vector(0, 0), vel=20, rgb=(1.0, 1.0, 1.0)):
        self.alive = True
        self.vel = vel
        self.vel_x = Vector(self.vel, 0)
        self.vel_y = Vector(0, self.vel)
        self.a = 3.2
        self.can_place_bomb = True
        self.place_bomb_time = time.time()
        self.bombs = []
        self.w = 5 * self.a
        self.h = 11.5 * self.a
        self.can_place_bomb_timeout = 1
        self.win = False
        self.aux_animation = False
        self.aux_animation_time = time.time()
        super().__init__(pos, rgb)

    def set_vel(self, v):
        self.vel_x = Vector(v, 0)
        self.vel_y = Vector(0, v)

    def set_bomb_place_time(self, t):
        self.can_place_bomb_timeout = t

    def figura(self):
        a = self.a

        # head
        glBegin(GL_POLYGON)
        glVertex2f(1 * a, 8 * a)
        glVertex2f(1 * a, 9 * a)
        glVertex2f(2 * a, 10 * a)
        glVertex2f(4 * a, 10 * a)
        glVertex2f(5 * a, 9 * a)
        glVertex2f(5 * a, 8 * a)
        glVertex2f(4 * a, 7 * a)
        glVertex2f(2 * a, 7 * a)
        glEnd()

        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.5, 0.5)
        glVertex2f(2 * a, 9.5 * a)
        glVertex2f(2 * a, 10 * a)
        glVertex2f(4 * a, 10 * a)
        glVertex2f(4 * a, 9.5 * a)
        glVertex2f(3.5 * a, 9 * a)
        glVertex2f(2.5 * a, 9 * a)
        glEnd()

        glBegin(GL_QUADS)
        glColor3f(0, 0, 0)
        # eyes
        rect(2, 8.25, 0.5, 0.5, a)
        rect(3.5, 8.25, 0.5, 0.5, a)

        # mouth
        rect(2.75, 7.25, 0.5, 0.25, a)

        # camera in the head
        rect(2.85, 9.1, 0.25, 0.25, a)

        glColor3f(0.6, 0.6, 0.6)
        # arms
        rect(0, 4, 1, 3, a)
        rect(5, 4, 1, 3, a)

        glColor3f(0.6, 0.6, 0.6)
        # legs
        rect(1, 0, 1, 3.5, a)
        rect(4, 0, 1, 3.5, a)
        glEnd()

        # torso
        glColor3f(162/255, 0, 0)
        glBegin(GL_POLYGON)
        glVertex2f(1 * a, 6 * a)
        glVertex2f(1 * a, 7 * a)
        glVertex2f(5 * a, 7 * a)
        glVertex2f(5 * a, 6 * a)
        glVertex2f(4 * a, 4 * a)
        glVertex2f(2 * a, 4 * a)
        glEnd()
        glBegin(GL_QUADS)
        rect(2, 3, 2, 1, a)
        glEnd()

        # aldebaran logo
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(0.6, 0.6, 0.6)
        glVertex2f(3 * a, 5.5 * a)
        for i in range(9):
            glVertex2f((3 + 0.5 * math.cos(i * 2 * math.pi / 8)) * a, (5.5 + 0.5 * math.sin(i * 2 * math.pi / 8)) * a)
        glEnd()

        glLineWidth(3)
        glBegin(GL_LINES)
        glColor3f(0, 0, 1)
        glVertex2f(3 * a, 5.8 * a)
        glVertex2f(3 * a, 5.6 * a)

        glVertex2f(2.9 * a, 5.5 * a)
        glVertex2f(3.1 * a, 5.5 * a)

        glVertex2f(2.95 * a, 5.4 * a)
        glVertex2f(2.8 * a, 5.2 * a)

        glVertex2f(3.05 * a, 5.4 * a)
        glVertex2f(3.1 * a, 5.3 * a)
        glEnd()

        glLineWidth(2)

    def figure1(self):
        glBegin(GL_QUADS)

        # head
        glColor3f(1, 1, 1)
        rect(1, 8.5, 3, 2, self.a)

        # eyes
        glColor3f(0, 0, 0)
        rect(1.75, 9, 0.5, 0.5, self.a)
        rect(2.75, 9, 0.5, 0.5, self.a)

        # torso
        glColor3f(0.5, 0.5, 0.5)
        rect(2, 2.5, 1, 6, self.a)
        rect(0, 6.5, 5, 1, self.a)

        # arms
        glColor3f(0, 0, 0)
        rect(0, 3.5, 1, 4, self.a)
        rect(4, 3.5, 1, 4, self.a)

        # hands
        rect(0, 2.5, 0.3, 1, self.a)
        rect(0.7, 2.5, 0.3, 1, self.a)

        rect(4, 2.5, 0.3, 1, self.a)
        rect(4.7, 2.5, 0.3, 1, self.a)

        # base
        glColor3f(0.7, 0, 0)
        rect(1, 0.5, 3, 2, self.a)

        # wheels
        glColor3f(0, 0, 0)
        rect(1, 0, 1, 0.5, self.a)
        rect(3, 0, 1, 0.5, self.a)

        # antenna
        rect(0.7, 9.5, 0.3, 1.5, self.a)
        rect(4, 9.5, 0.3, 1.5, self.a)

        glColor3f(0.7, 0, 0)
        rect(0.6, 11, 0.5, 0.5, self.a)
        rect(3.9, 11, 0.5, 0.5, self.a)

        glEnd()

    def figure2(self):
        glBegin(GL_QUADS)

        # head
        glColor3f(1, 1, 1)
        rect(1, 8.5, 3, 2, self.a)

        # eyes
        glColor3f(0, 0, 0)
        rect(1.75, 9, 0.5, 0.5, self.a)
        rect(2.75, 9, 0.5, 0.5, self.a)

        # torso
        glColor3f(0.5, 0.5, 0.5)
        rect(2, 2.5, 1, 6, self.a)
        rect(0, 6.5, 5, 1, self.a)

        # arms
        glColor3f(0, 0, 0)
        rect(0, 7.5, 1, 4, self.a)
        rect(4, 7.5, 1, 4, self.a)

        # hands
        rect(0, 11.5, 0.3, 1, self.a)
        rect(0.7, 11.5, 0.3, 1, self.a)

        rect(4, 11.5, 0.3, 1, self.a)
        rect(4.7, 11.5, 0.3, 1, self.a)

        # base
        glColor3f(0.7, 0, 0)
        rect(1, 0.5, 3, 2, self.a)

        # wheels
        glColor3f(0, 0, 0)
        rect(1, 0, 1, 0.5, self.a)
        rect(3, 0, 1, 0.5, self.a)

        # antenna
        rect(0.7, 9.5, 0.3, 1.5, self.a)
        rect(4, 9.5, 0.3, 1.5, self.a)

        glColor3f(0.7, 0, 0)
        rect(0.6, 11, 0.5, 0.5, self.a)
        rect(3.9, 11, 0.5, 0.5, self.a)

        glEnd()

    def mover(self, dt, move_right, move_left, move_up, move_down):
        self.crear()
        if time.time() - self.aux_animation_time > 0.5:
            self.aux_animation_time = time.time()
            self.aux_animation = not self.aux_animation
        if move_up:
            self.pos = sumar(self.pos, ponderar(dt, self.vel_y))
        if move_down:
            self.pos = sumar(self.pos, ponderar(-1 * dt, self.vel_y))
        if move_right:
            self.pos = sumar(self.pos, ponderar(dt, self.vel_x))
        if move_left:
            self.pos = sumar(self.pos, ponderar(-1 * dt, self.vel_x))

        # limits
        if self.pos.y < 0:
            self.pos.y = 0
            self.win = True

    def place_bomb(self):
        timeout = self.can_place_bomb_timeout
        if self.can_place_bomb:
            self.place_bomb_time = time.time()
            self.bombs.append(Bomb(pos=self.pos))
            self.can_place_bomb = False
        if time.time() - self.place_bomb_time > timeout:
            self.can_place_bomb = True

    def explode_bomb(self):
        for bomb in self.bombs:
            bomb.explode()

    def stop_left(self, wall):
        w_w = wall.w
        w_x = wall.pos.x
        self.pos.x = w_x + w_w + 1

    def stop_right(self, wall):
        w_x = wall.pos.x
        w = self.w
        self.pos.x = w_x - w

    def stop_up(self, wall):
        w_y = wall.pos.y
        h = self.h
        self.pos.y = w_y - h

    def stop_down(self, wall):
        w_h = wall.h
        w_y = wall.pos.y
        self.pos.y = w_y + w_h + 1

