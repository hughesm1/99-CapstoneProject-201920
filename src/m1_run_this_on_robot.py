"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Marcus Hughes-Oliver
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    real_thing()
    # my_stuff()

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
    robot.beep(3)

def run_test_tone_maker():
    robot=rosebot.ToneMaker()
    robot.tone(300, 3)

def run_test_speak_maker():
    robot=rosebot.SpeechMaker()
    robot.speak("don't make me sing")

def my_stuff():
    robot = rosebot.SensorSystem()
    robo = rosebot.Beeper()
    rob = rosebot.RoseBot()
    disty = 0
    while True:
        dist = int(robot.ir_proximity_sensor.get_distance_in_inches())
        robo.beep()
        # print('beep')
        if disty > dist:
            break
        disty = dist
    rob.drive_system.stop()

def real_thing():
    robot = rosebot.RoseBot()
    delegate = shared_gui_delegate_on_robot.Handler(robot)
    mqtt_reciever = com.MqttClient(delegate)
    mqtt_reciever.connect_to_pc()

    while True:
        time.sleep(.01)
        if delegate.is_time_to_stop:
            break

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()