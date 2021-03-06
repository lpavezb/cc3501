from models.breakable_wall import *
from models.power_up import *
from vista import *
from models.bomberman import *
from models.fondo import *
from models.wall import *
from random import *
os.environ['SDL_VIDEO_CENTERED'] = '1'  # centrar pantalla


def main():
    ancho = 800
    alto = 600
    init(ancho, alto, "Bomberman")
    vista = Vista()
    fondo = Fondo()
    ################
    # MAIN PROGRAM #
    ################

    # music
    pygame.mixer.pre_init(22050, -16, 2, 1024)
    pygame.mixer.quit()
    pygame.mixer.init(22050, -16, 2, 1024)
    win_sound = pygame.mixer.Sound("resources/Win.wav")
    pygame.mixer.music.load("resources/MainTheme.mp3")
    pygame.mixer.music.play(-1)

    # sprites
    explosion_sprites = get_sprites()

    # create walls
    w = Wall().w
    walls = create_walls(w)

    # create breakable walls
    r = 0.2  # breakable_wall creation probability (recommended r=0.2)
    breakable_walls, available_pos, break_wall_pos = create_breakable_walls(r, w)

    # create player Bomberman
    bomberman = Bomberman(pos=Vector(40, 30))

    # create enemies
    n_enemies = 4
    enemies, available_pos = create_enemies(n_enemies, available_pos, break_wall_pos)

    # create power ups
    power_ups = []
    r = randint(0, len(available_pos) - 1)
    power_ups.append(VelPowerUp(pos=available_pos[r]))
    available_pos.pop(r)
    r = randint(0, len(available_pos) - 1)
    power_ups.append(BombPowerUp(pos=available_pos[r]))
    available_pos.pop(r)

    # bomb list
    all_bombs = []
    run = True
    while run:
        #################
        # EVENT CONTROL #
        #################
        if bomberman.win:
            pygame.mixer.quit()
            pygame.mixer.init(32000)
            win_sound.play(0)
            pygame.time.delay(3500)
            run = False

        if not bomberman.active:
            run = False

        keys = pygame.key.get_pressed()

        bomberman.move_up = False
        bomberman.move_down = False
        bomberman.move_right = False
        bomberman.move_left = False

        # move keys
        if keys[pygame.K_UP]:
            bomberman.move_up = True

        if keys[pygame.K_DOWN]:
            bomberman.move_down = True

        if keys[pygame.K_RIGHT]:
            bomberman.move_right = True

        if keys[pygame.K_LEFT]:
            bomberman.move_left = True

        if keys[pygame.K_q]:
            run = False

        # two keys pressed
        if bomberman.move_up and bomberman.move_left:
            bomberman.move_up = False

        if bomberman.move_up and bomberman.move_right:
            bomberman.move_up = False

        if bomberman.move_down and bomberman.move_left:
            bomberman.move_down = False

        if bomberman.move_down and bomberman.move_right:
            bomberman.move_down = False

        # place bomb
        if keys[pygame.K_a]:
            all_bombs += bomberman.place_bomb()

        for event in pygame.event.get():
            if event.type == QUIT:  # cerrar ventana
                run = False

        # enemy place bomb
        for enemy in enemies:
            r = random()
            if r < 0.005:
                all_bombs += enemy.place_bomb()

        # move players
        bomberman.mover()
        for enemy in enemies:
            move(enemy)

        ##############
        # COLLISIONS #
        ##############
        all_walls = walls + breakable_walls
        players = [bomberman] + enemies
        for wall in all_walls:
            for player in players:
                if player.move_left and collide_left(player, wall):
                    player.move_left = False
                    player.stop_left(wall)
                if player.move_right and collide_right(player, wall):
                    player.move_right = False
                    player.stop_right(wall)
                if player.move_up and collide_up(player, wall):
                    player.move_up = False
                    player.stop_up(wall)
                if player.move_down and collide_down(player, wall):
                    player.move_down = False
                    player.stop_down(wall)

        for player in players:
            for bomb in all_bombs:
                if player.move_left and collide_left(player, bomb) and not bomb.invincible:
                    player.move_left = False
                    player.stop_left(bomb)
                if player.move_right and collide_right(player, bomb) and not bomb.invincible:
                    player.move_left = False
                    player.stop_right(bomb)
                if player.move_up and collide_up(player, bomb) and not bomb.invincible:
                    player.move_up = False
                    player.stop_up(bomb)
                if player.move_down and collide_down(player, bomb) and not bomb.invincible:
                    player.move_down = False
                    player.stop_down(bomb)

        for power_up in power_ups:
            if collide(bomberman, power_up):
                power_up.trigger(bomberman)

        for player in players:
            for bomb in all_bombs:
                if bomb.exploding and collide(player, bomb):
                    player.active = False
                if bomb.exploding and collide(player, bomb.destroy_range_up()):
                    player.active = False
                if bomb.exploding and collide(player, bomb.destroy_range_down()):
                    player.active = False
                if bomb.exploding and collide(player, bomb.destroy_range_left()):
                    player.active = False
                if bomb.exploding and collide(player, bomb.destroy_range_right()):
                    player.active = False

        for wall in breakable_walls:
            for bomb in all_bombs:
                if bomb.exploding and collide(bomb, wall):
                    wall.active = False
                if bomb.exploding and collide(bomb.destroy_range_up(), wall):
                    wall.active = False
                if bomb.exploding and collide(bomb.destroy_range_down(), wall):
                    wall.active = False
                if bomb.exploding and collide(bomb.destroy_range_left(), wall):
                    wall.active = False
                if bomb.exploding and collide(bomb.destroy_range_right(), wall):
                    wall.active = False

        for enemy in enemies:
            if collide(enemy, bomberman):
                enemy.active = False
                bomberman.active = False

        # explode bombs
        for bomb in all_bombs:
            bomb.explode(explosion_sprites)

        ###########
        # Drawing #
        ###########
        vista.dibujar(bomberman, enemies, fondo, walls, breakable_walls, power_ups, all_bombs)
    pygame.quit()


def create_enemies(n_enemies, available_pos, break_wall_pos):
    enemies = []
    aux = True
    for i in range(0, n_enemies):
        r = None
        while r is None:
            if available_pos == break_wall_pos:
                r = 0
                break
            r = randint(0, len(available_pos) - 1)
            if available_pos[r] in break_wall_pos:
                r = None
        if aux:
            figure_type = 1
            aux = not aux
        else:
            figure_type = 2
            aux = not aux
        enemies.append(Bomberman(pos=available_pos[r] + Vector(15, 10), figure_type=figure_type))
    return enemies, available_pos


def create_walls(w):
    walls = []
    for i in range(0, int(800 / w)):
        walls.append(Wall(pos=Vector(i * w, 0)))
        walls.append(Wall(pos=Vector(i * w, 600 - w)))
    walls.pop(32)
    walls.pop(30)
    for i in range(0, int(600 / w)):
        walls.append(Wall(pos=Vector(0, i * w)))
        walls.append(Wall(pos=Vector(800 - w, i * w)))
    wi_x = 3 * w
    wi_y = 3 * w
    while wi_y < 600:
        while wi_x < 800:
            walls.append(Wall(pos=Vector(wi_x, wi_y)))
            walls.append(Wall(pos=Vector(wi_x + w, wi_y)))
            walls.append(Wall(pos=Vector(wi_x, wi_y + w)))
            walls.append(Wall(pos=Vector(wi_x + w, wi_y + w)))
            wi_x = wi_x + 4 * w
        wi_x = 3 * w
        wi_y = wi_y + 4 * w
    return walls


def create_breakable_walls(r, w):
    breakable_walls = []
    available_pos = []
    wall_pos = []
    wi_x = 5 * w
    wi_y = w
    while wi_y < 600:
        while wi_x < 800 - 2 * w:
            pos = Vector(wi_x, wi_y)
            if random() < r:
                breakable_walls.append(BreakableWall(pos=pos))
                wall_pos.append(pos)
            available_pos.append(pos)
            wi_x = wi_x + 2 * w
        wi_x = w
        wi_y = wi_y + 4 * w
    wi_x = 5 * w
    wi_y = 3 * w
    while wi_y < 600 - 2 * w:
        while wi_x < 800 - 2 * w:
            pos = Vector(wi_x, wi_y)
            if random() < r:
                breakable_walls.append(BreakableWall(pos=pos))
                wall_pos.append(pos)
            available_pos.append(pos)
            wi_x = wi_x + 4 * w
        wi_x = w
        wi_y = wi_y + 4 * w

    # exit wall
    breakable_walls.append(BreakableWall(pos=Vector(15 * w, -w)))

    return breakable_walls, available_pos, wall_pos


def move(enemy):
    # TODO: move better

    # 20% stay still, 80% move
    r = np.random.choice(np.arange(0, 2), p=[0.2, 0.8])
    if r == 0:
        enemy.move_right = enemy.move_left = enemy.move_up = enemy.move_down = False
    else:
        r = np.random.choice(np.arange(0, 4), p=[0.25, 0.25, 0.25, 0.25])
        if r == 0:
            enemy.move_right = enemy.move_left = enemy.move_up = False
            enemy.move_down = True
        elif r == 1:
            enemy.move_right = enemy.move_left = enemy.move_down = False
            enemy.move_up = True
        elif r == 2:
            enemy.move_right = enemy.move_up = enemy.move_down = False
            enemy.move_left = True
        else:
            enemy.move_left = enemy.move_up = enemy.move_down = False
            enemy.move_right = True
    enemy.mover()


def collide(o1, o2):
    return collide_up(o1, o2) or collide_down(o1, o2) or collide_left(o1, o2) or collide_right(o1, o2)


main()
