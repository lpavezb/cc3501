from CC3501Utils import *
import time


class Bomb(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0), sound=None):
        self.a = 50
        self.place_time = time.time()
        self.active = True
        self.exploding = False
        self.invincible = True
        self.invincible_time = time.time()
        self.explode_time = 1
        self.w = 0.6 * self.a
        self.h = 0.8 * self.a
        self.explosion_sound = sound
        self.texture = glGenTextures(1)
        self.sprites = None
        super().__init__(pos, rgb)

    def figura(self):
        if not self.exploding:
            self.bomb()
        else:
            self.explosion()

    def bomb(self, tx=0, ty=0):
        glBegin(GL_POLYGON)
        a = self.a
        # head
        glColor3f(0, 0, 0)
        glVertex2f((0.2 + tx) * a, (0 + ty) * a)
        glVertex2f((0 + tx) * a, (0.2 + ty) * a)
        glVertex2f((0 + tx) * a, (0.4 + ty) * a)
        glVertex2f((0.2 + tx) * a, (0.6 + ty) * a)
        glVertex2f((0.4 + tx) * a, (0.6 + ty) * a)
        glVertex2f((0.6 + tx) * a, (0.4 + ty) * a)
        glVertex2f((0.6 + tx) * a, (0.2 + ty) * a)
        glVertex2f((0.4 + tx) * a, (0 + ty) * a)

        glEnd()

        glBegin(GL_QUADS)
        glColor3f(1, 1, 1)
        rect(0.4+tx, 0.2+ty, 0.1, 0.2, a)

        rect(0.3+tx, 0.4+ty, 0.1, 0.1, a)

        glColor3f(0.5, 0.5, 0.5)
        rect(0.2+tx, 0.6+ty, 0.1, 0.1, a)
        rect(0.3+tx, 0.7+ty, 0.1, 0.1, a)
        glColor3f(1, 0, 0)
        rect(0.4+tx, 0.7+ty, 0.1, 0.1, a)

        glEnd()

    def explode(self, explosion_sprites):
        self.sprites = explosion_sprites
        self.crear()
        if time.time() - self.invincible_time > 0.3:
            self.invincible = False
        if time.time() - self.place_time > self.explode_time:
            if not self.exploding:
                self.explosion_sound.play(0)
            self.explode_time = 1
            self.place_time = time.time()
            if self.exploding:
                self.active = False
            self.exploding = True

    def explosion(self):
        w = self.w
        h = self.h

        # mid
        self.set_texture(3, 0)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glBindTexture(GL_TEXTURE_2D, self.texture)
        x = 0
        y = 0
        glBegin(GL_QUADS)
        glTexCoord(0, 0)
        glVertex2f(x, y)
        glTexCoord(0, 1)
        glVertex2f(x, y+h)
        glTexCoord(1, 1)
        glVertex2f(x+w, y+h)
        glTexCoord(1, 0)
        glVertex2f(x+w, y)
        glEnd()

        glBindTexture(GL_TEXTURE_2D, 0)
        # up
        self.set_texture(3, 4)
        x = 0
        y = h
        glBegin(GL_QUADS)
        glTexCoord(0, 0)
        glVertex2f(x, y)
        glTexCoord(0, 1)
        glVertex2f(x, y + h)
        glTexCoord(1, 1)
        glVertex2f(x + w, y + h)
        glTexCoord(1, 0)
        glVertex2f(x + w, y)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)

        # down
        self.set_texture(3, 3)
        x = 0
        y = -1 * h
        glBegin(GL_QUADS)
        glTexCoord(0, 0)
        glVertex2f(x, y)
        glTexCoord(0, 1)
        glVertex2f(x, y + h)
        glTexCoord(1, 1)
        glVertex2f(x + w, y + h)
        glTexCoord(1, 0)
        glVertex2f(x + w, y)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)

        # right
        self.set_texture(3, 5)
        x = w
        y = 0
        glBegin(GL_QUADS)
        glTexCoord(0, 0)
        glVertex2f(x, y)
        glTexCoord(0, 1)
        glVertex2f(x, y + h)
        glTexCoord(1, 1)
        glVertex2f(x + w, y + h)
        glTexCoord(1, 0)
        glVertex2f(x + w, y)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)

        # left
        self.set_texture(3, 6)
        x = -1 * w
        y = 0
        glBegin(GL_QUADS)
        glTexCoord(0, 0)
        glVertex2f(x, y)
        glTexCoord(0, 1)
        glVertex2f(x, y + h)
        glTexCoord(1, 1)
        glVertex2f(x + w, y + h)
        glTexCoord(1, 0)
        glVertex2f(x + w, y)
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)
        glBindTexture(GL_TEXTURE_2D, glGenTextures(1))

    def destroy_range_up(self):
        b = Bomb(pos=Vector(self.pos.x, self.pos.y + self.h))
        b.invincible = False
        return b

    def destroy_range_down(self):
        b = Bomb(pos=Vector(self.pos.x, self.pos.y - self.h))
        b.invincible = False
        return b

    def destroy_range_right(self):
        b = Bomb(pos=Vector(self.pos.x + self.w, self.pos.y))
        b.invincible = False
        return b

    def destroy_range_left(self):
        b = Bomb(pos=Vector(self.pos.x - self.w, self.pos.y))
        b.invincible = False
        return b

    def set_texture(self, i, j):
        sprite_size = 32
        img = self.sprites[i][j]

        img_data = pygame.image.tostring(img, 'RGBA')
        img_width = img_height = sprite_size

        glBindTexture(GL_TEXTURE_2D, self.texture)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img_width, img_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
        glBindTexture(GL_TEXTURE_2D, 0)

        glEnable(GL_TEXTURE_2D)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texture)
