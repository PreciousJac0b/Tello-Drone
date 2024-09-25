import pygame
from djitellopy import Tello

from pygame.locals import (
  K_UP,
  K_DOWN,
  K_LEFT,
  K_RIGHT,
  K_t,
  K_l,
  K_d,
  K_s,
  K_u,
  K_ESCAPE,
  KEYDOWN,
  QUIT,
)

pygame.init()
pygame.display.set_mode([500, 500])


drone = Tello()
drone.connect()
# drone.takeoff()

print("Drone Battey percentage is: {}%".format(drone.get_battery()))


# def handle_key_input():
#   key_input = pygame.key.get_pressed()


#   if key_input[K_UP]:
#     drone.move_forward(90)
#   elif key_input[K_DOWN]:
#     drone.move_back(90)
#   elif key_input[K_RIGHT]:
#     drone.move_right(90)
#   elif key_input[K_LEFT]:
#     drone.move_left(90)

#   if key_input[K_t]:
#     drone.takeoff()
#   elif key_input[K_l]:
#     drone.land()

  
#   if key_input[K_w]:
#     drone.move_up(60)
#   elif key_input[K_s]:
#     drone.move_down(90)



def main():
  running = True

  while running:
    for event in pygame.event.get():
      if event.type == QUIT:
          running = False
          drone.land()
      elif event.type == KEYDOWN:
        if event.key == K_DOWN:
          drone.move_back(90)
        elif event.key == K_UP:
          drone.move_forward(90)
        elif event.key == K_LEFT:
          drone.move_left(90)
        elif event.key == K_RIGHT:
          drone.move_right(90)
        elif event.key == K_t:
          drone.takeoff()
        elif event.key == K_l:
          drone.land()
        elif event.key == K_u:
          drone.move_up(90)
        elif event.key == K_d:
          drone.move_down(90)
      
      # handle_key_input()
    pygame.display.update()
    pygame.display.flip()  

  pygame.quit()



if __name__ == '__main__':
  while True:
    main()