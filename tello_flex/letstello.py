from djitellopy import Tello

tello = Tello()

tello.connect()
tello.takeoff()

tello.move_left(100)
tello.rotate_counter_clockwise(90)
tello.rotate_counter_clockwise(90)
tello.rotate_counter_clockwise(90)
tello.rotate_counter_clockwise(90)
tello.move_right(100)


tello.land()

print("Battery percentage is presently: {}%".format(tello.get_battery()))