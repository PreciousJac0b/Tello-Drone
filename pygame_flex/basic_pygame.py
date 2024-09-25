import pygame


from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_ESCAPE,
  KEYDOWN,
  QUIT,
)

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])


running = True
while running:
  for event in pygame.event.get():
    # screen.fill((255,120, 85))
    if event.type == KEYDOWN:
      if event.key == K_ESCAPE:
        running = False

      if event.key == K_DOWN:
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

    elif event.type == QUIT:
      running = False

  screen.fill((255, 255, 255))

  # Create a surface and pass in a tuple containing its length and width
  surf = pygame.Surface((50, 50))

  # Give the surface a color to separate it from the background
  surf.fill((0, 0, 0))
  rect = surf.get_rect()

  surf_center = (
    (SCREEN_WIDTH-surf.get_width())/2,
    (SCREEN_HEIGHT-surf.get_height())/2
  )

  screen.blit(surf, surf_center)

  pygame.display.flip()


# screen.fill((255, 255, 255))

# surf = pygame.Surface((50, 50))


# surf.fill((0, 0, 0))


# rect = surf.get_rect()