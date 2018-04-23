from .stone import Stone
from .direction import Direction

STONE_SIZE = 32

SCREEN_HEIGHT = 350
SCREEN_WIDTH = 620
w = SCREEN_WIDTH // STONE_SIZE 
h = SCREEN_HEIGHT // STONE_SIZE

# create an empty grid  for building stones

#i = 0
#j = 0

#while i < SCREEN_HEIGHT:
 #   j = 0
  #  while j < SCREEN_WIDTH:
   #     grid[i][j] = 0 # 0 for no stone
    #    j+= STONE_SIZE
    #i+=STONE_SIZE

class Ability:
    def __init__(self, name, ab_type, cooldown):
        self.name = name
        self.ab_type = ab_type
        self.cool = cooldown
        self.current_cooldown = 0
        self.invoke = None

    def __str__(self):
        return self.name

    def __call__(self, *args, **kwargs):
        self.invoke()


class Heal(Ability):
    def __init__(self, cooldown, amount):
        super().__init__("Heal", "passive", cooldown)
        self.amount = amount

    def __call__(self, *args, **kwargs):
        if args[0].hp + self.amount <= 100:
            args[0].hp += self.amount
        else:
            args[0].hp = 100


class Build(Ability):
    grid = [[0 for y in range(w)] for x in range(h)]
    def __init__(self, cooldown, hp):
        super().__init__("Build", "active", cooldown)
        self.image = "wall.png"  # set file path
        self.hp = hp

    def __call__(self, *args, **kwargs):

        facing = args[0].current_facing
        player = args[0]
        x = player.x
        y = player.y

        offset = 16
        stone = Stone(x, y, self.image, 100)
        if facing == Direction.UP:
            #offset_y = (player.y % STONE_SIZE)
            #y = offset_y - STONE_SIZE
            #offset_x = player.x % STONE_SIZE
            #x = player.x - offset
            #if grid[x][y] == 0:
                #grid[x][y] = 1
                #stone.x = x
                #stone.y = y
            stone.y -= 32
            stone.x += offset
        if facing == Direction.DOWN:
           #offset_y = player.hitbox.height + (STONE_SIZE - (player.y % STONE_SIZE))
            #y = player.y + offset_y
            #offset_x = player.x % STONE_SIZE
            #x = player.x - offset_x
            #if grid[x][y] == 0:
             #   grid[x][y] = 1
            #stone.x = x
            #stone.y = y
            stone.y += 64
            stone.x += offset

        if facing == Direction.LEFT:
            #offset_x = player.x % STONE_SIZE
            #x = player.x - offset_x
            #offset_y = STONE_SIZE - ( player.y % STONE_SIZE)
            #y = player.y + offset_y
            #if grid[x][y] == 0:
                #grid[x][y] = 1 
                #stone.x = x
                #stone.y = y
            stone.x -= 32
            stone.y += offset
        if facing == Direction.RIGHT:
            #offset_x = player.hitbox.width + (STONE_SIZE - (player.x % STONE_SIZE ) )
            #x = player.x + offset_x
            #offset_y = STONE_SIZE - (player.y % STONE_SIZE)
            #y = player.y + offset_y
            #if grid[x][y] == 0:
                #grid[x][y] = 1
                #stone.x = x
                #stone.y = y
            stone.x += 64
            stone.y += offset

        new_x = stone.x - (stone.x % STONE_SIZE)
        new_y = stone.y - (stone.y % STONE_SIZE)
        ind_x = new_x // 32
        ind_y = new_y // 32
        if self.grid[ind_y][ind_x] == 1:
            return None
        stone.x = new_x
        stone.y = new_y
        stone.grid_x = ind_x
        stone.grid_y = ind_y
        self.grid[ind_y][ind_x] = 1
        return stone
