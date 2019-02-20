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
    print('turn 90')
    print(right_left)
    robot.drive_system.left_motor.reset_position()
    if right_left == 0:
        # right  turn #
        robot.drive_system.go(speed,-speed)
    if right_left == 1:
        # left turn #
        robot.drive_system.go(-speed,speed)
    degrees = 415
    while True:
        print(robot.drive_system.left_motor.get_position())
        # 415 is 90
        if abs(robot.drive_system.left_motor.get_position()) >= degrees:
            robot.drive_system.stop()
            break


def line_follow(robot, intensity, speed, n, space):
    t = 0.4
    while True:
        robot.drive_system.go(int(speed), int(speed))
        if int(intensity) <= robot.sensor_system.color_sensor.get_reflected_light_intensity():
            robot.drive_system.go(-int(speed), int(speed))
            time.sleep(t)
            t += 0.2
        if int(intensity) <= robot.sensor_system.color_sensor.get_reflected_light_intensity():
            robot.drive_system.go(int(speed), -int(speed))
            time.sleep(t)
            t += 0.2
        if int(intensity) >= robot.sensor_system.color_sensor.get_reflected_light_intensity():
            t=0.4
        if robot.sensor_system.color_sensor.get_color() == 5:
            while True:
                if robot.sensor_system.color_sensor.get_color() != 5:
                    break
            n+=1
        if n == space:
            return n
        if n == 9:
            return n

def go_to_space(robot,space):
    n=0
    while True:
        n = line_follow(robot, 70, 50, n, space)
        if n == space:
            robot.drive_system.stop()
            turn_90(robot,0,50)
            rosebot.DriveSystem.go_straight_for_seconds(robot.drive_system,1,50)
            robot.arm_and_claw.lower_arm()
            rosebot.DriveSystem.go_straight_for_seconds(robot.drive_system, 1, -50)
            turn_90(robot,1,50)
            break
    while True:
        n = line_follow(robot, 70, 50, n, space)
        if n == 9:
            robot.drive_system.stop()
            break

def go_to_space_5(robot,space):
    n=0
    while True:
        n = line_follow(robot, 70, 50, n, space)
        if n == space:
            robot.drive_system.stop()
            turn_90(robot,0,50)
            rosebot.DriveSystem.go_straight_for_seconds(robot.drive_system,3,50)
            robot.arm_and_claw.lower_arm()
            rosebot.DriveSystem.go_straight_for_seconds(robot.drive_system, 3, -50)
            turn_90(robot,1,50)
            break
    while True:
        n = line_follow(robot, 70, 50, n, space)
        if n == 9:
            robot.drive_system.stop()
            break

def go_get_with_camera(robot, left_or_right, speed, start_time, rate):
    area = 500
    if left_or_right == 0:
        robot.drive_system.spin_counterclockwise_until_sees_object(speed, area)
    if left_or_right == 1:
        robot.drive_system.spin_clockwise_until_sees_object(speed, area)
    ledProx(robot, speed, start_time, rate)

def button_1_function(robot):
    go_to_space(robot,4)

def button_2_function(robot):
    go_to_space(robot,5)

def button_3_function(robot):
    go_to_space(robot,6)

def button_4_function(robot):
    go_to_space(robot,3)

def button_5_function(robot):
    go_to_space_5(robot, 1)

def button_6_function(robot):
    go_to_space(robot,7)

def button_7_function(robot):
    go_to_space(robot,1)

def button_8_function(robot):
    go_to_space(robot,2)

def button_9_function(robot):
    go_to_space(robot,8)

def x_turn(robot):
    turn_90(robot,1,50)
    rosebot.DriveSystem.go_forward_until_distance_is_less_than(robot.drive_system,1,40)
    robot.arm_and_claw.raise_arm()
    rosebot.DriveSystem.go_straight_until_color_is(robot.drive_system,'Black',-40)
    turn_90(robot,0,50)

def y_turn(robot):
    turn_90(robot,0,50)
    rosebot.DriveSystem.go_forward_until_distance_is_less_than(robot.drive_system, 1, 40)
    robot.arm_and_claw.raise_arm()
    rosebot.DriveSystem.go_straight_until_color_is(robot.drive_system, 'Black', -40)

    turn_90(robot,1,50)

