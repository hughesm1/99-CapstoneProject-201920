"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Grant Stewart, Zachary Juday, Marcus Hughes-Oliver
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")

    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)

    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)

    return frame


def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)

    return frame


def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

def get_drivey_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Drive Stuff")
    go_straight_for_seconds_button = ttk.Button(frame, text="Go straight for seconds")
    go_straight_for_seconds_using_time_button = ttk.Button(frame, text="Go straight for inches using time")
    go_straight_for_seconds_using_encoder_button = ttk.Button(frame, text='Go straight for inches using encoder')
    time_entry = ttk.Entry(frame, width=8)
    speed_entry = ttk.Entry(frame, width=8)

    speedy_entry = ttk.Entry(frame, width=8)
    encoder_entry = ttk.Entry(frame, width=8)

    yup_entry = ttk.Entry(frame, width=8)
    mhmm_entry = ttk.Entry(frame, width=8)

    summ_label = ttk.Label(frame, text='seconds, speed')
    ru_label = ttk.Label(frame, text='inches, speed')
    guy_label = ttk.Label(frame, text='inches, speed')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    go_straight_for_seconds_button.grid(row=1, column=3)
    go_straight_for_seconds_using_time_button.grid(row=2, column=3)
    go_straight_for_seconds_using_encoder_button.grid(row=3, column=3)
    time_entry.grid(row=2, column=1)
    speed_entry.grid(row=2, column=2)
    encoder_entry.grid(row=3, column=1)
    speedy_entry.grid(row=3, column=2)
    yup_entry.grid(row=1, column=1)
    mhmm_entry.grid(row=1, column=2)
    summ_label.grid(row=1, column=0)
    ru_label.grid(row=2, column=0)
    guy_label.grid(row=3, column=0)

    # Set the Button callbacks:
    go_straight_for_seconds_button["command"] = lambda: handle_straight_seconds(yup_entry, mhmm_entry, mqtt_sender)
    go_straight_for_seconds_using_time_button["command"] =\
        lambda: handle_straight_seconds_time(time_entry, speed_entry, mqtt_sender)
    go_straight_for_seconds_using_encoder_button["command"] = \
        lambda: handle_straight_for_inches_encoder(encoder_entry, speedy_entry, mqtt_sender)

    return frame

def get_sound_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=2, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Sound Stuff")
    beep_button = ttk.Button(frame, text="Beep")
    tone_button = ttk.Button(frame, text="Tone")
    speak_button = ttk.Button(frame, text="Speak")
    wow_entry = ttk.Entry(frame, width=8)
    tone_entry = ttk.Entry(frame, width=8)
    freq_entry = ttk.Entry(frame, width=8)
    speak_entry = ttk.Entry(frame, width=8)
    beep_label = ttk.Label(frame, text='# of beeps')
    tone_label = ttk.Label(frame, text='freq, duration')
    speak_label = ttk.Label(frame, text='What is said')

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    beep_button.grid(row=1, column=0)
    tone_button.grid(row=1, column=1)
    speak_button.grid(row=1, column=2)
    wow_entry.grid(row=3, column=0)
    tone_entry.grid(row=3, column=1)
    freq_entry.grid(row=4, column=1)
    speak_entry.grid(row=3, column=2)
    beep_label.grid(row=2, column=0)
    tone_label.grid(row=2, column=1)
    speak_label.grid(row=2, column=2)

    # Set the Button callbacks:
    beep_button["command"] = lambda: handle_beep(wow_entry, mqtt_sender)
    tone_button["command"] = lambda: handle_tone(tone_entry, freq_entry, mqtt_sender)
    speak_button["command"] = lambda: handle_speak(speak_entry, mqtt_sender)

    return frame

#create a new frame for sensors
def get_sensor_system(window, mqtt_sender):
    frame = ttk.Frame(window, padding=2, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Sensor Stuff")
    color_button = ttk.Button(frame, text="Color")
    proximity_button = ttk.Button(frame, text="Proximity")
    camera_button = ttk.Button(frame, text="Camera")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    color_button.grid(row=1, column=1)
    proximity_button.grid(row=2, column=1)
    camera_button.grid(row=3, column=1)

    # Set the Button callbacks:
    color_button["command"] = lambda: handle_color(mqtt_sender)
    proximity_button["command"] = lambda: handle_proximity(mqtt_sender)
    camera_button["command"] = lambda: handle_camera(mqtt_sender)

    return frame
# perons 1
def beep_proximity_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=2, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Beep Proximity")
    beep_button = ttk.Button(frame, text='start it')
    beep_entry = ttk.Entry(frame)
    increase_entry = ttk.Entry(frame)

    frame_label.grid(row=0, column=1)
    beep_button.grid(row=1, column=1)
    beep_entry.grid(row=1, column=0)
    increase_entry.grid(row=2, column=0)

    beep_button["command"] = lambda: handle_beepProx(mqtt_sender, beep_entry, increase_entry)

    return frame

def get_move_with_tone(window, mqtt_sender):
    frame = ttk.Frame(window, padding=2, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="move with tone")
    move_with_tone_button = ttk.Button(frame, text='move with tone')
    tone_entry = ttk.Entry(frame)
    increase_entry = ttk.Entry(frame)

    frame_label.grid(row=0, column=1)
    move_with_tone_button.grid(row=1, column=1)
    tone_entry.grid(row=1, column=0)
    increase_entry.grid(row=2, column=0)

    move_with_tone_button["command"] = lambda: handle_toneProx(mqtt_sender, tone_entry, increase_entry)

    return frame

###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################


###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('forward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('forward', [left_entry_box.get(), right_entry_box.get()])


def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('backward', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('backward', [left_entry_box.get(), right_entry_box.get()])


def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('left', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('left', [left_entry_box.get(), right_entry_box.get()])


def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print('right', left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message('right', [left_entry_box.get(), right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """
    print('stop')
    mqtt_sender.send_message('stop')


###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print('raise_arm')
    mqtt_sender.send_message('raise_arm')


def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print('lower_arm')
    mqtt_sender.send_message('lower_arm')


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print('calibrate_arm')
    mqtt_sender.send_message('calibrate_arm')


def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print('move_arm_to_position', arm_position_entry.get())
    mqtt_sender.send_message('move_arm_to_position', [arm_position_entry.get()])


###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')


def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    # mqtt_sender.send_message('exit')
    handle_quit(mqtt_sender)
    exit()


def handle_straight_seconds(sec, speed, mqtt_sender):
    print('go straight for seconds', sec.get())
    mqtt_sender.send_message('go_straight_for_seconds', [sec.get(), speed.get()])


def handle_straight_seconds_time(time, speed,  mqtt_sender):
    print('go straight for inches using time', time.get(), speed.get())
    mqtt_sender.send_message('go_straight_for_inches_using_time', [time.get(), speed.get()])


def handle_straight_for_inches_encoder(encoder, speed, mqtt_sender):
    print('go straight for inches using encoder', encoder.get(), speed.get())
    mqtt_sender.send_message('go_straight_for_inches_using_encoder', [encoder.get(), speed.get()])


def handle_beep(num, mqtt_sender):
    print('beep', num.get())
    mqtt_sender.send_message('beep', [num.get()])


def handle_tone(freq, dur, mqtt_sender):
    print('tone', freq.get(), dur.get())
    mqtt_sender.send_message('tone', [freq.get(), dur.get()])


def handle_speak(speak, mqtt_sender):
    print('speak', speak.get())
    mqtt_sender.send_message('speak', [speak.get()])

def handle_color(mqtt_sender):
    print('color')
    mqtt_sender.send_message('color')

def handle_proximity(mqtt_sender):
    print('proximity')
    mqtt_sender.send_message('proximity')

def handle_camera(mqtt_sender):
    print('camera')
    mqtt_sender.send_message('camera')

def handle_beepProx(mqtt_sender, beepprox, increase):
    print('beepProx')
    mqtt_sender.send_message('beepProx', [beepprox.get(), increase.get()])


def handle_toneProx(mqtt_sender, toneProx, increase):
    print('move with tone')
    mqtt_sender.send_message('move with tone', [toneProx.get(), increase.get()])