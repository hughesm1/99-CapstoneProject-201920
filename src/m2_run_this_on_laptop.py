"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Grant Stewart.
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
    root.title("Grant lego12")

    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame = ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()

    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame, person2_frame = get_shared_frames(main_frame, mqtt_sender)

    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)
    my_final_frame(main_frame, mqtt_sender)
    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame, person2_frame)

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
    sensor_frame= shared_gui.get_sensor_system(main_frame,mqtt_sender)
    person2_frame=shared_gui.get_move_with_tone(main_frame,mqtt_sender)


    return teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame, person2_frame



def grid_frames(teleop_frame, arm_frame, control_frame, drive_frame, sound_frame, sensor_frame, person2_frame):
    teleop_frame.grid(row=1, column=1)
    arm_frame.grid(row=1, column=0)
    control_frame.grid(row=2, column=2)
    drive_frame.grid(row=2, column=0)
    sound_frame.grid(row=2, column=1)
    sensor_frame.grid(row=0, column=0)
    person2_frame.grid(row=0, column=1)




def my_final_frame(main_frame, mqtt_sender):
    frame = ttk.Frame(main_frame, padding=2, borderwidth=5, relief="ridge")
    frame.grid(row=0, column = 2)

    frame_lable = ttk.Label(frame, text = 'final')
    drag_race_button = ttk.Button(frame, text='drag race')
    drag_race_speed_entry = ttk.Entry(frame)
    drag_race_speed_label = ttk.Label(frame, text = 'start speed')
    drag_race_acceleration_entry = ttk.Entry(frame)
    drag_race_acceleration_elabel = ttk.Label(frame, text = 'acceleration')

    frame_lable.grid(row=0, column=0)
    drag_race_button.grid(row=2, column= 2)
    drag_race_speed_entry.grid(row=2, column=0)
    drag_race_speed_label.grid(row=1, column = 0)
    drag_race_acceleration_entry.grid(row=2, column=1)
    drag_race_acceleration_elabel.grid(row=1, column=1)

    return frame

def handle_drag_race(mqtt_snder, input):
    print('race')
    mqtt_sender.send_message('drag_race',[input])
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()