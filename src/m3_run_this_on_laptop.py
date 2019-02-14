"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Zachary Juday.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender = com.MqttClient()
    mqtt_sender.connect_to_ev3()

    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("Zach lego12")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    get_my_frames(main_frame,mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------


    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_frame = shared_gui.get_drivey_frame(main_frame,mqtt_sender)
    sound_frame = shared_gui.get_sound_frame(main_frame,mqtt_sender)
    sensor_frame = shared_gui.get_sensor_system(main_frame, mqtt_sender)


    return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame

def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_frame.grid(row=1, column=1)
    sound_frame.grid(row=0, column=1)
    sensor_frame.grid(row=0, column =2)


def get_my_frames(main_frame,mqtt_sender):
    led_frame_function(main_frame,mqtt_sender)
    get_with_camera_frame(main_frame, mqtt_sender)


def led_frame_function(main_frame, mqtt_sender):
    led_frame = ttk.Frame(main_frame, padding=2, borderwidth=5, relief="ridge")
    led_frame.grid(row=2,column=1)

    led_frame_label = ttk.Label(led_frame, text="Pick up with LED")
    led_frame_label.grid(row=0, column=0)

    led_frame_button = ttk.Button(led_frame, text='Go')
    led_frame_button.grid(row=2, column=3)

    led_frame_speed_entry = ttk.Entry(led_frame)
    led_frame_speed_entry_label = ttk.Label(led_frame, text='speed')
    led_frame_speed_entry.grid(row=2,column=0)
    led_frame_speed_entry_label.grid(row=1,column=0)

    led_frame_start_time_entry = ttk.Entry(led_frame)
    led_frame_start_time_entry_label = ttk.Label(led_frame, text='start time between')
    led_frame_start_time_entry.grid(row=2,column=1)
    led_frame_start_time_entry_label.grid(row=1,column=1)

    led_frame_rate_entry = ttk.Entry(led_frame)
    led_frame_rate_entry_label = ttk.Label(led_frame, text='decrease rate between')
    led_frame_rate_entry.grid(row=2,column=2)
    led_frame_rate_entry_label.grid(row=1,column=2)

    led_frame_button['command'] = lambda: handle_ledProx(mqtt_sender,
                                                         int(led_frame_speed_entry.get()),
                                                         int(led_frame_start_time_entry.get()),
                                                         int(led_frame_rate_entry.get()))
    return led_frame

def get_with_camera_frame(main_frame, mqtt_sender):

    frame = ttk.Frame(main_frame, padding=2, borderwidth=5, relief="ridge")
    frame.grid(row=1,column=2)

    frame_lable = ttk.Label(frame, text='Get with Camera, LED')
    frame_lable.grid(row=0,column=0)

    frame_button = ttk.Button(frame, text='Go')
    frame_button.grid(row=2, column=4)

    frame_clock = ttk.Entry(frame)
    frame_clock_lable = ttk.Label(frame, text= 'C-Clockwise=0,Clockwise=1')
    frame_clock.grid(row=2,column=0)
    frame_clock_lable.grid(row=1, column=0)

    frame_speed_entry = ttk.Entry(frame)
    frame_speed_entry_label = ttk.Label(frame, text='speed')
    frame_speed_entry.grid(row=2,column=1)
    frame_speed_entry_label.grid(row=1,column=1)

    frame_start_time_entry = ttk.Entry(frame)
    frame_start_time_entry_label = ttk.Label(frame, text='start time between')
    frame_start_time_entry.grid(row=2,column=2)
    frame_start_time_entry_label.grid(row=1,column=2)

    frame_rate_entry = ttk.Entry(frame)
    frame_rate_entry_label = ttk.Label(frame, text='decrease rate between')
    frame_rate_entry.grid(row=2,column=3)
    frame_rate_entry_label.grid(row=1,column=3)

    frame_button['command'] = lambda: handle_get_with_camera(mqtt_sender,int(frame_clock.get()),
                                                             int(frame_speed_entry.get()),
                                                             int(frame_start_time_entry.get()),
                                                             int(frame_rate_entry.get()))

    return frame

def handle_ledProx(mqtt_sender, speed, start_time, rate):
    print('ledProx')
    mqtt_sender.send_message('ledProx', [speed, start_time, rate])

def handle_get_with_camera(mqtt_sender, left_or_right, speed, start_time, rate):
    print('camera with LED')
    mqtt_sender.send_message('go_get_with_camera',[left_or_right, speed, start_time, rate])
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()