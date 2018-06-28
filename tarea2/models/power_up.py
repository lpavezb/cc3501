from CC3501Utils import *


class VelPowerUp(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 50
        self.w = self.h = self.a
        self.active = True
        self.sound = pygame.mixer.Sound("resources/VelBonus.wav")
        super().__init__(pos, rgb)

    def figura(self):
        a = self.a
        glPushMatrix()
        glTranslatef(12.5, 12.5, 0)
        glBegin(GL_QUADS)

        # boot
        glColor3f(160/255, 82/255, 45/255)
        rect(0.2, 0.2, 0.2, 0.35, a)
        rect(0.2, 0, 0.4, 0.2, a)

        # wind
        glColor3f(0, 191/255, 1)
        rect(0.05, 0.05, 0.1, 0.1, a)
        rect(0.05, 0.25, 0.1, 0.1, a)
        rect(0.05, 0.45, 0.1, 0.1, a)

        # arrow
        glColor3f(1, 1, 0)
        rect(0.45, 0.25, 0.1, 0.2, a)
        glEnd()

        glBegin(GL_TRIANGLES)
        glVertex2f(0.4 * a, 0.45 * a)
        glVertex2f(0.5 * a, 0.55 * a)
        glVertex2f(0.6 * a, 0.45 * a)
        glEnd()
        glPopMatrix()

    def trigger(self, bomberman):
        self.sound.play(0)
        bomberman.set_vel(40)
        self.active = False


class BombPowerUp(Figura):
    def __init__(self, pos=Vector(0, 0), rgb=(1.0, 1.0, 1.0)):
        self.a = 50
        self.w = self.h = self.a * 0.5
        self.active = True
        self.texture = glGenTextures(1)
        self.sound = pygame.mixer.Sound("resources/BombBonus.wav")
        super().__init__(pos, rgb)

    def figura(self):
        a = self.a * 0.6

        glPushMatrix()
        glTranslatef(12, 10, 0)

        self.bomb(tx=0.2, ty=0.2)
        self.bomb(tx=0.1, ty=0.1)
        self.bomb()

        glBegin(GL_QUADS)
        glColor3f(1, 0, 0)
        rect(0.2, 0.2, 0.2, 0.2, a)
        glColor3f(1, 1, 0)
        rect(0.25, 0.2, 0.1, 0.2, a)
        rect(0.2, 0.25, 0.2, 0.1, a)
        glEnd()
        glPopMatrix()
        # arrow

    def trigger(self, bomberman):
        self.sound.play(0)
        bomberman.set_bomb_place_time(bomberman.can_place_bomb_timeout/2)
        self.active = False

    def set_texture(self, image_path):
        ID = glGenTextures(1)
        img = pygame.image.load(image_path)
        image_data = pygame.image.tostring(img, 'RGBA')
        tex_width, tex_height = img.get_size()
        glBindTexture(GL_TEXTURE_2D, ID)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, tex_width, tex_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
        glBindTexture(GL_TEXTURE_2D, 0)

        self.texture = ID
        glEnable(GL_TEXTURE_2D)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
        glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
        glBindTexture(GL_TEXTURE_2D, self.texture)

    def bomb(self, tx=0, ty=0):
        glBegin(GL_POLYGON)
        a = self.a * 0.6
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
        rect(0.4 + tx, 0.2 + ty, 0.1, 0.2, a)

        rect(0.3 + tx, 0.4 + ty, 0.1, 0.1, a)

        glColor3f(0.5, 0.5, 0.5)
        rect(0.2 + tx, 0.6 + ty, 0.1, 0.1, a)
        rect(0.3 + tx, 0.7 + ty, 0.1, 0.1, a)
        glColor3f(1, 0, 0)
        rect(0.4 + tx, 0.7 + ty, 0.1, 0.1, a)

        glEnd()
