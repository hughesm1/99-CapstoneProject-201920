import time
import math
import rosebot

"""The code should have the user put in a start speed and acceleration and using those 
have the car drive forward until it goes over white, but there is a catch. the catch is that you have a limited amount 
of full and when you run out of full the car will stop. There are other parts as well such as the car will also stop if 
it detects a wall in front of it. """

#note the code will not run corectly on a light cullered floor as it will not work with the color sensor.

'''Main code for the Final that is to mimic a drag race concept.'''
def drag_race(robot,start_speed, acceration,r):
    """ :type robot: rosebot.Rosebot"""
    robot = rosebot.RoseBot() # will be removed for actual code just here to check . method

    start_fule, speed, curent_fule = initial_stat_systems(robot, start_speed, acceration)
    while True:
        speed = how_to_move(robot, speed, curent_fule, acceration, r)
        if you_win(robot,speed,curent_fule, r):
            break
        if you_loose(robot, curent_fule, r):
            break
        if you_crashed(robot, r):
            break
        time.sleep(.5)
        curent_fule = curent_fule - speed ** 2  # + (((acceration+1)/speed
    end_code(robot)

"""The code to decide if you have crosed the finish line and what happens if you do."""
def you_win(robot, speed, curent_fule,r):
    win = robot.sensor_system.color_sensor.get_reflected_light_intensity()
    if win > 30:
        print('you win. The amount of fule you have left is', curent_fule)
        r.send_message('pirnt_GUI')
        robot.drive_system.go(speed, -speed)
        #robot.arm_and_claw.raise_arm()
        robot.arm_and_claw.move_arm_to_position(curent_fule*10)
        time.sleep(2)
        robot.drive_system.stop()
        return True
    return False

"""This code is to find if you lost by running out of full"""
def you_loose(robot, curent_fule,r):
    if curent_fule >= 0:
        print('you loose')
        r.send_message('pirnt_GUI')
        robot.drive_system.stop()
        robot.sound_system.speech_maker.speak("if you ain't first your last").wait()
        return True
    return False

"""This is the code to see if the user crashed"""
def you_crashed(robot,r):
    crash = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    if crash < 3:
        #crash = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        #if crash < 3:
            print('you crashed')
            r.send_message('pirnt_GUI')
            robot.drive_system.stop()
            robot.sound_system.speech_maker.speak("you've got to learn to drive with the fear").wait()
            return True
    return False

"""These are the initial start values that the robot will be using"""
def initial_stat_systems(robot,start_speed, acceration):
    start_fule = 500  # amout of full you start with
    speed = start_speed
    for _ in range(3):
        robot.sound_system.beeper.beep().wait()
    robot.sound_system.tone_maker.play_tone(1000, 1000).wait()
    curent_fule = start_fule
    return start_fule,speed,curent_fule

"""This is the code to change the speed of the robot depending on the acceleration"""
def how_to_move(robot, speed, acceration,r):
    if speed > 100:
        print('at max speed 100')
        r.send_message('pirnt_GUI')
        speed = 100
    robot.drive_system.go(speed, speed)
    if speed < 100:
        speed = speed + acceration
    return speed

"""this is the code that will run at the end to make sure that the robot can run again"""
def end_code(robot):
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()