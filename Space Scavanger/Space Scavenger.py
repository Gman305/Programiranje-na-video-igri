import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen size and colors
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sonic-like Game")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)  # Simple blue square for player
        self.rect = self.image.get_rect()
        self.rect.center = (100, screen_height - 70)
        self.vel_x = 0
        self.vel_y = 0
        self.is_jumping = False

    def update(self):
        # Handle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.vel_x = -5
        elif keys[pygame.K_RIGHT]:
            self.vel_x = 5
        else:
            self.vel_x = 0

        # Handle jumping
        if self.is_jumping:
            self.vel_y += 1  # Gravity
        else:
            self.vel_y = 0

        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        # Prevent going off-screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screen_width:
            self.rect.right = screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height

    def jump(self):
        if not self.is_jumping:
            self.vel_y = -15  # Jump strength
            self.is_jumping = True

    def land(self):
        self.is_jumping = False
        self.rect.y = screen_height - 70

# Set up sprite groups
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    # Update game logic
    all_sprites.update()

    # Check for landing
    if player.rect.bottom >= screen_height - 20:
        player.land()

    # Drawing
    screen.fill(WHITE)
    all_sprites.draw(screen)

    pygame.display.flip()

    # Frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
