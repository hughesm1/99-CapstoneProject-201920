"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Marcus Hughes-Oliver.
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
    recieve = Delegate()
    mqtt_sender = com.MqttClient(recieve)
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root = tkinter.Tk()
    root.title("Marcus Hughes-Oliver's final project")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief='groove')
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    # teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame, beep_proximity_frame\
    #     = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    # line follow
    # line_follow_frame = ttk.Frame(main_frame, padding=2, borderwidth=5, relief="ridge")
    # line_follow_frame.grid()
    # frame_label = ttk.Label(line_follow_frame, text="Line Follow")
    # beep_button = ttk.Button(line_follow_frame, text="Line Follow")
    # frame_label.grid(row=0, column=0)
    # beep_button.grid(row=1, column=1)
    final_frame(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    # grid_frames(teleop_frame, arm_frame, control_frame, drive_frame,
    #             sound_frame, sensor_frame, beep_proximity_frame, line_follow_frame)

    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()


def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame = shared_gui.get_teleoperation_frame(main_frame, mqtt_sender)
    arm_frame = shared_gui.get_arm_frame(main_frame, mqtt_sender)
    control_frame = shared_gui.get_control_frame(main_frame, mqtt_sender)
    drive_frame = shared_gui.get_drivey_frame(main_frame, mqtt_sender)
    sound_frame = shared_gui.get_sound_frame(main_frame, mqtt_sender)
    sensor_frame= shared_gui.get_sensor_system(main_frame,mqtt_sender)
    beep_proximity_frame = shared_gui.beep_proximity_frame(main_frame, mqtt_sender)
    return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame, beep_proximity_frame


def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame, beep_proximity_frame, line_follow_frame):
    teleop_frame.grid(row=0, column=0)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=0)
    drive_frame.grid(row=3, column=0)
    sound_frame.grid(row=1, column=4)
    sensor_frame.grid(row=0, column=4)
    beep_proximity_frame.grid(row=0, column=5)
    line_follow_frame.grid(row=0, column=6)


def final_frame(main_frame, mqtt_sender):
    frame = ttk.Frame(main_frame, padding=2, borderwidth=5, relief="ridge")
    frame.grid(row=0, column=2)

    moon_rocks_button = ttk.Button(frame, text='Find Humans Trash')
    initial_speed_scale = ttk.Scale(frame, from_=0, to=100)
    how_many_rocks_label = ttk.Label(frame, text='how many pieces of trash would you like to pick up')
    initial_speed_label = ttk.Label(frame, text='start speed')
    how_many_rocks_entry = ttk.Entry(frame)

    moon_rocks_button.grid(row=3, column=2)
    how_many_rocks_label.grid(row=3, column=0)
    initial_speed_label.grid(row=1, column=0)
    initial_speed_scale.grid(row=2, column=0)
    how_many_rocks_entry.grid(row=4, column=0)

    moon_rocks_button["command"] = lambda: handle_moon_rocks(mqtt_sender, initial_speed_scale, how_many_rocks_entry)

    return frame


class Delegate(object):
    def __init__(self, x=None):
        self.x = x
    def print_GUI(self,y):
        print(y)

    def the_time(self):
        print("its over in this many seconds")

    def num_of_rocks(self):
        print("the number of pieces of trash you collected is")


def handle_moon_rocks(mqtt_sender, initial_speed, how_many_rocks):
    print('lets do it', initial_speed.get(), how_many_rocks.get())
    mqtt_sender.send_message('moon_rocks', [initial_speed.get(), how_many_rocks.get()])
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()