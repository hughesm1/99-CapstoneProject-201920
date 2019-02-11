"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Marcus Hughes-Oliver, Zachary Juday, Grant Stewart.
  Winter term, 2018-2019.
"""


class Handler(object):
    def __init__(self, robot):
        """

        :type robot: rosebot.RoseBot
        """
        self.robot = robot

    def forward(self, left_wheel_speed, right_wheel_speed):
        print('got forward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def backward(self, left_wheel_speed, right_wheel_speed):
        print('got backward', left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed) * -1, int(right_wheel_speed) * -1)

    def left(self, left_wheel_speed, right_wheel_speed):
        print('got left', int(left_wheel_speed) * -1, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed) * -1, int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        print('got right', left_wheel_speed, int(right_wheel_speed)*-1)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed) * -1)

    def stop(self):
        print('got stop')
        self.robot.drive_system.stop()

    def raise_arm(self):
        print('got raise arm')
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print('got lower arm')
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print('got calibrate arm')
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, arm_position):
        print('got move arm to position')
        self.robot.arm_and_claw.move_arm_to_position(int(arm_position))

    def quit(self):
        print('got quit')
        self.quit()

    def exit(self):
        print('got exit')
        self.quit()
        self.exit()

    def go_straight_for_seconds(self, sec, speed):
        print('got go straight for seconds')
        self.robot.drive_system.go_straight_for_seconds(int(sec), int(speed))

    def go_straight_for_inches_using_time(self, time, speed):
        print('got go straight for inches using time')
        self.robot.drive_system.go_straight_for_inches_using_time(int(time), int(speed))

    def go_straight_for_inches_using_encoder(self, encoder, speed):
        print('got go straight for inches using encoder')
        self.robot.drive_system.go_straight_for_inches_using_encoder(int(encoder), int(speed))

    def beep(self, n):
        print('got beep')
        self.beep(int(n))

    def tone(self, freq, dur):
        print('got tone')
        self.tone(int(freq), int(dur))

    def speak(self, string):
        print('got speak')
        self.speak(string)
