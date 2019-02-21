"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Marcus Hughes-Oliver, Zachary Juday, Grant Stewart.
  Winter term, 2018-2019.
"""
import time
import m3_extra
import m2_extra
import m1_extra


class Handler(object):
    def __init__(self, robot, r):
        """

        :type robot: rosebot.RoseBot
        """
        self.robot = robot
        self.is_time_to_stop = False
        self.r = r


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
        print('proximity forward')
        self.robot.drive_system.go_forward_until_distance_is_less_than(int(inches), int(speed))

    def proximity_backward(self, inches, speed):
        print('proximity backward')
        self.robot.drive_system.go_backward_until_distance_is_greater_than(int(inches), int(speed))

    def proximity_within(self, delta, inches, speed):
        print('proximity within')
        self.robot.drive_system.go_until_distance_is_within(int(delta),int(inches),int(speed))

    def camera_val(self):
        print('camera val')
        self.robot.drive_system.display_camera_data()

    def clock_camera(self, speed, area):
        print('clock_camera')
        self.robot.drive_system.spin_clockwise_until_sees_object(int(speed), int(area))

    def counter_camera(self, speed, area):
        print('counter_camera')
        self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed), int(area))

    # marcus stuff
    def beepProx(self, beepProx, increase):
        print('got beepProx')
        n = int(beepProx)
        x = int(increase)
        self.robot.drive_system.go(30, 30)
        # while True:
        #     dist = int(self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches())
        #     self.robot.sound_system.beeper.beep().wait()
        #     time.sleep(2)
        #     if dist <= 20:
        #         break
        while True:
            dist = self.robot.sensor_system.ir_proximity_sensor.get_distance_in_inches()
            if 19 >= dist:
                # print(dist)
                if dist <= 10:
                    print(dist)
                    if dist <= 1:
                        self.robot.drive_system.stop()
                        self.robot.arm_and_claw.raise_arm()
                        # print(dist)
                        break
                # inc = n + x * (1 / dist)
                    self.robot.sound_system.beeper.beep().wait()
                    time.sleep(.1)
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
        print((direction),'give me int')
        if int(direction) == 0:
            self.robot.drive_system.spin_clockwise_until_sees_object(int(speed),30)
        if int(direction) == 1:
            self.robot.drive_system.spin_counterclockwise_until_sees_object(int(speed),30)
        b = self.robot.sensor_system.camera.get_biggest_blob()
        x = b.center.x
        if x >= 170:
            while True:
                self.robot.drive_system.go(25,-25)
                b = self.robot.sensor_system.camera.get_biggest_blob()
                x = b.center.x
                if x < 170:
                    self.robot.drive_system.stop()
                    break
        if x <=150:
             while True:
                self.robot.drive_system.go(-25, 25)
                b = self.robot.sensor_system.camera.get_biggest_blob()
                x = b.center.x
                if x > 150:
                    self.robot.drive_system.stop()
                    break
        self.robot.drive_system.stop()
        self.move_with_tone(100,2000)

    def ledProx(self, speed, start_time, rate):
        m3_extra.ledProx(self.robot, speed, start_time, rate)

    def go_get_with_camera(self, left_or_right, speed, start_time, rate):
        m3_extra.go_get_with_camera(self.robot, left_or_right, speed, start_time, rate)

    def straight_intensity_greater(self, intensity, speed):
        while True:
            self.robot.drive_system.go(int(speed), int(speed))
            if int(intensity) <= self.robot.sensor_system.color_sensor.get_reflected_light_intensity():
                self.robot.drive_system.stop()
                break

    def straight_intensity_less(self, intensity, speed):
        while True:
            self.robot.drive_system.go(int(speed), int(speed))
            if int(intensity) >= self.robot.sensor_system.color_sensor.get_reflected_light_intensity():
                self.robot.drive_system.stop()
                break

    def straight_until_color_is(self, color, speed):
        while True:
            self.robot.drive_system.go(int(speed), int(speed))
            if color == self.robot.sensor_system.color_sensor.get_color_as_name():
                self.robot.drive_system.stop()
                break

    def straight_until_color_is_not(self, color, speed):
        while True:
            self.robot.drive_system.go(int(speed), int(speed))
            if color != self.robot.sensor_system.color_sensor.get_color_as_name():
                self.robot.drive_system.stop()
                break

    def drag_race(self, start_speed, acceleration):
        m2_extra.drag_race(self.robot,int(start_speed),int(acceleration),self.r)

    def turn_90(self, right_left, speed):
        m3_extra.turn_90(self.robot,right_left,speed)

    def moon_rocks(self, initial_speed, how_many_rocks):
        m1_extra.moon_rocks(self.robot, int(initial_speed), int(how_many_rocks), self.r)

    def go_to_space1(self):
        m3_extra.button_1_function(self.robot)

    def go_to_space2(self):
        m3_extra.button_2_function(self.robot)

    def go_to_space3(self):
        m3_extra.button_3_function(self.robot)

    def go_to_space4(self):
        m3_extra.button_4_function(self.robot)

    def go_to_space5(self):
        m3_extra.button_5_function(self.robot)

    def go_to_space6(self):
        m3_extra.button_6_function(self.robot)

    def go_to_space7(self):
        m3_extra.button_7_function(self.robot)

    def go_to_space8(self):
        m3_extra.button_8_function(self.robot)

    def go_to_space9(self):
        m3_extra.button_9_function(self.robot)

    def x_turn(self):
        m3_extra.x_turn(self.robot)

    def y_turn(self):
        m3_extra.y_turn(self.robot)




