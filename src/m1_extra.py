import rosebot
import time
import math

def moon_rocks(robot, initial_speed, r):
    speed = initial_start_systems(robot, initial_speed)
    start_time = time.time()
    move_stuff(robot, speed, start_time, r)
    get_to_rock(robot, speed, r)
    pick_up_rock(robot, r)
    get_back_to_line(robot, speed, r)

# def how_many():

def print_to_laptop(num, start_time, r):
    print('time from start is', time.time() - start_time)
    r.send_message('the_time')
    r.send_message('print_GUI', [time.time() - start_time])
    print('Its all over. The number of moon rocks you picked up was', num)
    r.send_message('num_of_rocks')
    r.send_message('print_GUI', [num])

def initial_start_systems(robot,initial_speed):
    # start_fule = 1000  # amout of full you start with ####################################################################
    # if start_speed == 0:
    #     start_speed = 1
    speed = initial_speed
    for _ in range(3):
        robot.sound_system.beeper.beep()
        time.sleep(1)
    robot.sound_system.tone_maker.play_tone(500, 500).wait()
    robot.sound_system.speech_maker.speak("Lets get ready to rumble").wait()
    # curent_fule = start_fule
    return speed

def move_stuff(robot, speed, start_time, r):
    # robot.drive_system.go(speed, speed)
    while True:
        robot.drive_system.go(int(speed), int(speed))
        if 70 <= robot.sensor_system.color_sensor.get_reflected_light_intensity():
            robot.drive_system.go(-int(speed), int(speed))
            time.sleep(.2)
        if 70 <= robot.sensor_system.color_sensor.get_reflected_light_intensity():
            robot.drive_system.go(int(speed, -int(speed)))
            time.sleep(.2)

        if start_time >= 10:
            robot.drive_system.stop()
            break

def get_to_rock(robot, speed, r):
    robot.drive_system.spin_clockwise_until_sees_object(speed, 3)
    robot.drive_system.go_forward_until_distance_is_less_than(3, speed)

def pick_up_rock(robot, r):
    robot.arm_and_claw.raise_arm()

def get_back_to_line(robot, speed, r):
    robot.drive_system.go(-int(speed), int(speed))
    time.sleep(1)
    robot.drive_system.go_straight_until_intensity_is_less_than(20, speed)