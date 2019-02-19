import time
import math
import rosebot

"""The code should have the user put in a start speed and acceleration and using those 
have the car drive forward until it goes over white, but there is a catch. the catch is that you have a limited amount 
of full and when you run out of full the car will stop. There are other parts as well such as the car will also stop if 
it detects a wall in front of it. 

sugestions for use is to put the finish line between 28in to 38in away"""

#note the code will not run corectly on a light cullered floor as it will not work with the color sensor.

'''Main code for the Final that is to mimic a drag race concept.'''
def drag_race(robot,start_speed, acceration,r):
    """ :type robot: rosebot.Rosebot"""
    #robot = rosebot.RoseBot() # will be removed for actual code just here to check . method

    start_fule, speed, curent_fule = initial_stat_systems(robot, start_speed, acceration)
    start_time = time.time()
    while True:
        speed = how_to_move(robot, speed, acceration, r)
        print(curent_fule)
        if you_win(robot,speed,curent_fule, start_fule, r, start_time):
            break
        if you_loose(robot, curent_fule, r):
            break
        if you_crashed(robot, r):
            break
        time.sleep(.5)
        curent_fule = curent_fule + ((math.sqrt(acceration))/(start_speed+1)) - (speed + start_speed) - acceration
    end_code(robot)

"""The code to decide if you have crosed the finish line and what happens if you do."""
def you_win(robot, speed, curent_fule,start_fule,r, start_time):
    win = robot.sensor_system.color_sensor.get_reflected_light_intensity()
    if win > 40:
        print_to_lab(start_time, curent_fule, r)
        robot.drive_system.go(speed, -speed)
        arm_height = 5112*curent_fule/start_fule
        time.sleep(.5)
        robot.drive_system.stop()
        robot.arm_and_claw.move_arm_to_position(arm_height)
        time.sleep(1)
        return True
    return False

"""this prints to labtop for win code"""
def print_to_lab(start_time, curent_fule, r):
    print('time from start is', time.time() - start_time)
    r.send_message('your_time')
    r.send_message('print_GUI', [time.time() - start_time])
    print('you win. The amount of fuel you have left is', curent_fule)
    r.send_message('your_fuel')
    r.send_message('print_GUI', [curent_fule])

"""This code is to find if you lost by running out of full"""
def you_loose(robot, curent_fule,r):
    if curent_fule <= 0:
        print('you loose')
        r.send_message('lose')
        robot.drive_system.stop()
        robot.sound_system.speech_maker.speak("if you ain't first your last").wait()
        return True
    return False

"""This is the code to see if the user crashed"""
def you_crashed(robot,r):
    crash = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    if crash < 3:
        print('you crashed')
        r.send_message('crash')
        robot.drive_system.stop()
        robot.sound_system.speech_maker.speak("you've got to learn to drive with the fear").wait()
        return True
    return False

"""These are the initial start values that the robot will be using"""
def initial_stat_systems(robot,start_speed, acceration):
    start_fule = 1000  # amout of full you start with ####################################################################
    if start_speed == 0:
        start_speed = 1
    speed = start_speed
    for _ in range(3):
        robot.sound_system.beeper.beep()
        time.sleep(1)
    robot.sound_system.tone_maker.play_tone(500, 500).wait()
    curent_fule = start_fule
    return start_fule,speed,curent_fule

"""This is the code to change the speed of the robot depending on the acceleration"""
def how_to_move(robot, speed, acceration,r):
    if speed > 100:
        print('at max speed 100')
        speed = 100
    robot.drive_system.go(speed, speed)
    if speed < 100:
        speed = speed + acceration
    return speed

"""this is the code that will run at the end to make sure that the robot can run again"""
def end_code(robot):
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()