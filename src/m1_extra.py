import rosebot
import time
import math

def moon_rocks(robot, initial_speed, how_many_rocks, r):
    speed = initial_start_systems(robot, initial_speed)
    start_time = time.time()
    max = int(how_many_rocks)
    count = 0
    while True:
        print('move stuff bouta happen')
        move_stuff(robot, speed, start_time, r)
        print('get to rock bouta happen')
        # get_to_rock(robot, speed, r)
        print('pick up bouta happen')
        pick_up_rock(robot, r)
        print('pick up is done')
        turn_with_rock(robot, speed)
        print('turn is done')
        put_rock_down(robot)
        print('put down is done')
        get_back_to_line(robot, speed, r)
        print('back on line')
        count = count + 1
        print('count is', count)
        # get_back_to_line(robot, speed, r)
        if count >= max:
            print_to_laptop(count, start_time, r)
            break

# def how_many():

def print_to_laptop(num, start_time, r):
    print('time from start is', time.time() - start_time)
    r.send_message('the_time')
    r.send_message('print_GUI', [time.time() - start_time])
    print('Its all over. The number of moon rocks you picked up was', num)
    r.send_message('num_of_rocks')
    r.send_message('print_GUI', [num])

def initial_start_systems(robot,initial_speed):
    speed = initial_speed
    # for _ in range(3):
    #     robot.sound_system.beeper.beep()
    #     time.sleep(1)
    # robot.sound_system.tone_maker.play_tone(500, 500).wait()
    robot.sound_system.speech_maker.speak("Lets clean up this Earth").wait()
    return speed

def move_stuff(robot, speed, start_time, r):
    # robot.drive_system.go(speed, speed)
    t = .4
    while True:
        robot.drive_system.go(int(speed), int(speed))
        if 70 <= robot.sensor_system.color_sensor.get_reflected_light_intensity():
            robot.drive_system.go(-int(speed), int(speed))
            time.sleep(t)
            t += .2
        if 70 <= robot.sensor_system.color_sensor.get_reflected_light_intensity():
            robot.drive_system.go(int(speed), -int(speed))
            time.sleep(t)
            t += .2
        if 70 >= robot.sensor_system.color_sensor.get_reflected_light_intensity():
            t = 0.4

        if int(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) <= 2:
            robot.drive_system.stop()
            break

        if time.time() - start_time >= 100:
            robot.drive_system.stop()
            print('it stopped')
            break

# def get_to_rock(robot, speed, r):
#     print('camera should about to start')
#     robot.drive_system.spin_clockwise_until_sees_object(speed, 70000)
#     # time.sleep(3)
#     # robot.drive_system.display_camera_data()
#     print('should go forward')
#     robot.drive_system.go_forward_until_distance_is_less_than(3, speed)

def pick_up_rock(robot, r):
    robot.arm_and_claw.raise_arm()

def turn_with_rock(robot, speed):
    robot.drive_system.go(-int(speed), int(speed))
    time.sleep(1)
    robot.drive_system.stop()

def put_rock_down(robot):
    robot.arm_and_claw.lower_arm()

def get_back_to_line(robot, speed, r):
    robot.drive_system.go(int(speed), -int(speed))
    time.sleep(1.1)
    robot.drive_system.stop()
    # robot.drive_system.go_straight_until_intensity_is_less_than(20, speed)