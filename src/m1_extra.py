import rosebot
import time
import math

"""main code to run that runs everything else and should clean 
up the Earth by picking up trash and moving it off of the path"""
def moon_rocks(robot, initial_speed, how_many_rocks, r):
    speed = initial_start_systems(robot, initial_speed)
    start_time = time.time()
    max = int(how_many_rocks)
    count = 0
    while True:
        move_stuff(robot, speed, start_time, r)
        pick_up_rock(robot, r)
        turn_with_rock(robot, speed)
        put_rock_down(robot)
        get_back_to_line(robot, speed, r)
        count = count + 1
        if count >= max:
            robot.sound_system.speech_maker.speak("I cleaned up the Earth today, humans are useless").wait()
            print_to_laptop(count, start_time, r)
            break


"""Once all of the trash has been picked up this prints to the laptop"""
def print_to_laptop(num, start_time, r):
    print('Time we spent picking up trash', time.time() - start_time)
    r.send_message('the_time')
    r.send_message('print_GUI', [time.time() - start_time])
    print('Its all over. The number of pieces of trash you picked up was', num)
    r.send_message('num_of_rocks')
    r.send_message('print_GUI', [num])


"""This will start the first portion of the robot activity by speaking a message"""
def initial_start_systems(robot,initial_speed):
    speed = initial_speed
    robot.sound_system.speech_maker.speak("Lets clean up this Earth").wait()
    return speed


"""This will constantly run a line follow function defined below and then also
 check to see if there is a piece of trash in front of it. If there is a piece 
 of trash in front of the robot it will break out of this function"""
def move_stuff(robot, speed, start_time, r):
    t = .4
    while True:
        robot.drive_system.go(int(speed), int(speed))
        line_follow(robot, speed, t)
        t += .2
        if int(robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()) <= 1:
            robot.drive_system.stop()
            break

        if time.time() - start_time >= 100:
            robot.drive_system.stop()
            print('it stopped')
            break


"""This function should follow a black line constantly"""
def line_follow(robot, speed, t):
    if 70 <= robot.sensor_system.color_sensor.get_reflected_light_intensity():
        print(robot.sensor_system.color_sensor.get_reflected_light_intensity())
        robot.drive_system.go(-int(speed), int(speed))
        time.sleep(t)
        t += .2
    if 70 <= robot.sensor_system.color_sensor.get_reflected_light_intensity():
        print(robot.sensor_system.color_sensor.get_reflected_light_intensity())
        robot.drive_system.go(int(speed), -int(speed))
        time.sleep(t)
        t += .2
    if 70 >= robot.sensor_system.color_sensor.get_reflected_light_intensity():
        t = .4


"""This function should raise the arm when called"""
def pick_up_rock(robot, r):
    robot.arm_and_claw.raise_arm()


"""This function should turn left when called and then stopping movement"""
def turn_with_rock(robot, speed):
    robot.drive_system.go(-int(speed), int(speed))
    time.sleep(1.5)
    robot.drive_system.stop()


"""This function will lower the arm and drop the trash off the path"""
def put_rock_down(robot):
    robot.arm_and_claw.lower_arm()


"""This function will turn back to the right until it sees the line and then stop movement"""
def get_back_to_line(robot, speed, r):
    robot.drive_system.go(int(speed), -int(speed))
    time.sleep(1.6)
    robot.drive_system.stop()