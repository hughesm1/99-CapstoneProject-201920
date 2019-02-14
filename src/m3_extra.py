import time
import math
import rosebot



def ledProx(robot, speed, start_time, rate):
    print(speed)
    print(start_time)
    print(rate)

    robot.drive_system.go(int(speed), speed)
    robot.drive_system.left_motor.reset_position()
    left = robot.led_system.left_led
    right = robot.led_system.right_led
    robot.drive_system.left_motor.reset_position()
    t = 0
    a = 0
    b = 0
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        t = t + rate*b
        if distance <= 5:
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm()
            left.turn_off()
            right.turn_off()
            break
        time_between = start_time*math.exp(-t)
        if a == 0:
            left.turn_on()
            time.sleep(0.2)
            left.turn_off()
            time.sleep(time_between)
            a = 1
            b = 1
        if a == 1:
            right.turn_on()
            time.sleep(.2)
            right.turn_off()
            time.sleep(time_between)
            a = 2
            b = 1
        if a == 2:
            right.turn_on()
            left.turn_on()
            time.sleep(.2)
            right.turn_off()
            left.turn_off()
            time.sleep(time_between)
            a = 0
            b = 1