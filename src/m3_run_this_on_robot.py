"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Zachary Juday
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot
import math

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #run_test_arm_raise()
    #run_test_arm_calibrate()
    #run_test_move_arm_to_position()
    #run_test_lower_arm()

    #run_test_go()
    run_test_stop()
    #run_test_go_straight_for_seconds()
    #run_test_go_straight_for_inches_using_time()
    #run_test_go_straight_for_inches_using_encoder()

    #run_test_beeper()
    #run_test_tone_maker()
    #run_test_speak_maker()

    # run_test_pick_up_with_led()

    # real_thing()

def run_test_arm_raise():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.raise_arm()

def run_test_arm_calibrate():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.calibrate_arm()

def run_test_move_arm_to_position():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.move_arm_to_position(0)

def run_test_lower_arm():
    robot=rosebot.RoseBot()
    robot.arm_and_claw.lower_arm()

def run_test_go():
    robot=rosebot.RoseBot()
    print("go")
    robot.drive_system.go(100,100)

def run_test_go_straight_for_seconds():
    robot=rosebot.RoseBot()
    print("go straight for seconds")
    robot.drive_system.go_straight_for_seconds(100, 100)

def run_test_stop():
    robot=rosebot.RoseBot()
    time.sleep(3)
    print("stop")
    robot.drive_system.stop()

def run_test_go_straight_for_inches_using_time():
    robot = rosebot.RoseBot()
    print("go straight for inches using time")
    robot.drive_system.go_straight_for_inches_using_time(50, 100)

def run_test_go_straight_for_inches_using_encoder():
    robot = rosebot.RoseBot()
    print("go straight for inches using encoder")
    robot.drive_system.go_straight_for_inches_using_encoder(50,100)

def run_test_beeper():
    robot=rosebot.Beeper()


def run_test_tone_maker():
    robot=rosebot.ToneMaker()


def run_test_speak_maker():
    robot=rosebot.SpeechMaker()
    robot.speak("don't make me sing")


def run_test_pick_up_with_led():
    pick_up_object_with_led(100,1,1)


def pick_up_object_with_led(speed, start_time, rate):
    robot = rosebot.RoseBot()
    robot.drive_system.go(speed, speed)
    original_distance = robot.sensor_system.ir_proximity_sensor.get_distance()
    while True:
        distance = robot.sensor_system.ir_proximity_sensor.get_distance()
        if abs(distance) <= 3:
            robot.led_system.left_led.turn_off()
            robot.led_system.right_led.turn_off()
            robot.drive_system.stop()
            robot.arm_and_claw.raise_arm().wait()
            break
        time_between = (start_time + (start_time*math.exp((-distance)*rate)))/100
        robot.led_system.left_led.turn_on().wait()
        robot.led_system.left_led.turn_off().wait()
        time.sleep(time_between)
        robot.led_system.right_led.turn_on().wait()
        robot.led_system.right_led.turn_off().wait()
        time.sleep(time_between)
        robot.led_system.right_led.turn_on().wait()
        robot.led_system.left_led.turn_on().wait()
        robot.led_system.right_led.turn_off().wait()
        robot.led_system.left_led.turn_off().wait()
        time.sleep(time_between)
        time.sleep(time_between)



def real_thing():
    robot=rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_receiver = com.MqttClient(delegate)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if delegate.is_time_to_stop:
            break



# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()