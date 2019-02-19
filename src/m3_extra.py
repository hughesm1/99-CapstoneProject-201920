import time
import math
import rosebot

def ledProx(robot, speed, start_time, rate):
    robot.drive_system.go(int(speed), speed)
    robot.drive_system.left_motor.reset_position()
    left = robot.led_system.left_led
    right = robot.led_system.right_led
    t = 0
    a = 0
    b = 0
    led_loop(robot, left, right, t, a, b, rate, start_time)


def led_seq1(left,time_between):
    left.turn_on()
    time.sleep(0.2)
    left.turn_off()
    time.sleep(time_between)
    return 1


def led_seq2(right,time_between):
    right.turn_on()
    time.sleep(.2)
    right.turn_off()
    time.sleep(time_between)
    return 2


def led_seq3(left,right,time_between):
    right.turn_on()
    left.turn_on()
    time.sleep(.2)
    right.turn_off()
    left.turn_off()
    time.sleep(time_between)
    return 0


def led_end(left,right,robot):
    robot.drive_system.stop()
    robot.arm_and_claw.raise_arm()
    left.turn_off()
    right.turn_off()


def led_loop(robot, left, right, t, a, b, rate, start_time):
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        if distance <= 5:
            led_end(left, right, robot)
            break
        t = t + (rate * b)
        time_between = start_time*math.exp(-t)
        if a == 2:
            a = led_seq3(left, right, time_between)
        if a == 1:
            a = led_seq2(right, time_between)
        if a == 0:
            a = led_seq1(left, time_between)
            b = 1


def turn_90(robot, right_left, speed):
    robot.drive_system.left_motor.reset_position()
    if right_left == 0:
        # right  turn #
        robot.drive_system.go(speed,-speed)
    if right_left == 1:
        # left turn #
        robot.drive_system.go(-speed,speed)
    while True:
        print(robot.drive_system.left_motor.get_position())
        if abs(robot.drive_system.left_motor.get_position()) >= 415:
            robot.drive_system.stop()
            break




def go_get_with_camera(robot, left_or_right, speed, start_time, rate):
    area = 500
    if left_or_right == 0:
        robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)
    if left_or_right == 1:
        robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    ledProx(robot, speed, start_time, rate)
