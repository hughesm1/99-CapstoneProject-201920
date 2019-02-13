"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Marcus Hughes-Oliver, Zachary Juday, Grant Stewart.
  Winter term, 2018-2019.
"""
import time

class Handler(object):
    def __init__(self, robot):
        """

        :type robot: rosebot.RoseBot
        """
        self.robot = robot
        self.is_time_to_stop = False


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
        self.is_time_to_stop = True

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
        for _ in range(int(n)):
            self.robot.sound_system.beeper.beep()
            time.sleep(.5)

    def tone(self, freq, dur):
        print('got tone', freq, dur)
        self.robot.sound_system.tone_maker.play_tone(int(freq), int(dur)).wait()

    def speak(self, string):
        print('got speak')
        self.robot.sound_system.speech_maker.speak(string)

    def color(self):
        print('color')
        self.robot.sensor_system.color_sensor.get_color()


    def proximity_forward(self, inches, speed):
        print('proximity')
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))

    def proximity_backward(self, inches, speed):
        print('proximity')
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))



    def camera(self, speed, area):
        print('camera')
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    # marcus stuff
    def beepProx(self, beepProx, increase):
        print('got beepProx')
        n = int(beepProx)
        x = int(increase)
        self.robot.drive_system.go(30, 30)
        while True:
            dist = int(self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
            self.robot.sound_system.beeper.beep().wait()
            time.sleep(2)
            if dist <= 20:
                break
        while True:
            dist = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if dist <= 20:
                if 19 >= dist >= 5:
                    if dist <= 3:
                        self.robot.drive_system.stop()
                        self.robot.arm_and_claw.raise_arm()
                        break
                    # inc = n + x * (1 / dist)
                    self.robot.sound_system.beeper.beep().wait()
                    time.sleep(.1)
                self.robot.sound_system.beeper.beep().wait()
                time.sleep(.5)
        self.robot.drive_system.stop()

    # code for person 2 to do feature 9
    def move_with_tone(self, initial_frequency, increase_in_frequency):
        print('got move with tone')
        #self.robot.drive_system.go_forward_until_distance_is_less_than(1,100) #posible poblem is staying on this line and not moving on may just change to go and put stop at end
        self.robot.drive_system.go(25, 25)
        n = int(initial_frequency) # the initial value that the user puts in
        x = int(increase_in_frequency) # the rate of increase for frequency
        """while True:
            self.robot.sound_system.tone_maker.play_tone(n, 500).wait()
            m = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if m <= 20:
                break"""
        while True:
            m = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            print(m)
            if m <= 20:
                if m <= 3:
                    self.robot.drive_system.stop()
                    self.robot.arm_and_claw.raise_arm()
                    break
                z = n + x * (1 / m)  # the actual increase in frequency  not linear but will increase every inch
                self.robot.sound_system.tone_maker.play_tone(z,500).wait() #i beleave that duration is in ms so 500 should be 1/2 a second
            else:
                self.robot.sound_system.tone_maker.play_tone(n,500).wait()

    def find_with_camera(self, speed, direction):
        if direction == 0:
            self.robot.drive_system.spin_clockwise_until_sees_object(speed,30)
        if direction == 1:
            self.robot.drive_system.spin_counterclockwise_until_sees_object(speed,30)



