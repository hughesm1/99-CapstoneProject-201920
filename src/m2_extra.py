import time
import math
import rosebot



def drag_race(robot,start_speed, acceration):
    """ :type robot: rosebot.Rosebot"""
    robot = rosebot.RoseBot() # will be removed for actual code just here to check . method

    start_fule, speed, curent_fule = initial_stat_systems(robot, start_speed, acceration)
    while True:
        robot.drive_system.go(speed, speed)
        if speed < 100:
            speed = speed + acceration
        if you_win(robot,speed,curent_fule):
            break
        if you_loose(robot, speed, curent_fule):
            break
        if you_crashed(robot):
            break
        time.sleep(.5)
        curent_fule = curent_fule - speed ** 2  # + (((acceration+1)/speed))
    robot.drive_system.stop()
    robot.arm_and_claw.lower_arm()

def you_win(robot, speed, curent_fule):
    win = robot.sensor_system.color_sensor.get_reflected_light_intensity()
    if win > 30:
        print('you win. The amount of fule you have left is', curent_fule)
        robot.drive_system.go(speed, -speed)
        robot.arm_and_claw.raise_arm()
        time.sleep(2)
        robot.drive_system.stop()
        return True
    return False

def you_loose(robot, speed, curent_fule):
    if curent_fule >= 0:
        print('you loose')
        robot.drive_system.stop()
        robot.sound_system.speech_maker.speak("if you ain't first your last").wait()
        return True
    return False

def you_crashed(robot):
    crash = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
    if crash < 3:
        crash = robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
        if crash < 3:
            print('you crashed')
            robot.drive_system.stop()
            return True
    return False

def initial_stat_systems(robot,start_speed, acceration):
    start_fule = 200  # amout of full you start wit
    speed = start_speed
    for _ in range(3):
        robot.sound_system.beeper.beep().wait()
    robot.sound_system.tone_maker.play_tone(1000, 1000)
    curent_fule = start_fule
    return start_fule,speed,curent_fule