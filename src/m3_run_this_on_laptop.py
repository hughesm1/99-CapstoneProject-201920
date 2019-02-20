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
    # right_90_frame(main_frame, mqtt_sender)
    start_game_frame(main_frame, mqtt_sender)

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


def right_90_frame(main_frame, mqtt_sender):

    frame = ttk.Frame(main_frame, padding=2, borderwidth=5, relief="ridge")
    frame.grid(row=2, column=2)

    frame_label = ttk.Label(frame, text='turn 90 frame')
    frame_label.grid(row=0, column=0)

    frame_button = ttk.Button(frame, text='go')
    frame_button.grid(row=2, column=2)

    speed_entry = ttk.Entry(frame)
    speed_entry_label = ttk.Label(frame, text='speed')
    speed_entry.grid(row=2, column=0)
    speed_entry_label.grid(row=1,column=0)

    l_r_entry = ttk.Entry(frame)
    l_r_entry_label = ttk.Label(frame, text='right=0 left=1')
    l_r_entry.grid(row=2, column=1)
    l_r_entry_label.grid(row=1, column=1)

    frame_button['command'] = lambda: handle_turn_90(mqtt_sender, int(speed_entry.get()),
                                                     int(l_r_entry.get())) #frame_button)

    return frame

def start_game_frame(main_frame,mqtt_sender):

    frame = ttk.Frame(main_frame, padding=2, borderwidth=5, relief="ridge")
    frame.grid(row=2, column=2)

    frame_label = ttk.Label(frame, text='Tic-Tac-Toe')
    frame_label.grid(row=0, column=0)

    frame_button = ttk.Button(frame, text='PLAY')
    frame_button.grid(row=1, column=0)

    frame_button['command'] = lambda:ttt_frame(mqtt_sender)

    return frame

def ttt_frame(mqtt_sender):
    root2 = tkinter.Tk()
    root2.title("Tic-Tak-Toe")

    frame = ttk.Frame(root2, padding=10, borderwidth=5, relief="groove")
    frame.grid()

    button1 = ttk.Button(frame)
    button1.grid(row=2, column=0)

    button2 = ttk.Button(frame)
    button2.grid(row=2, column=1)

    button3 = ttk.Button(frame)
    button3.grid(row=2, column=2)

    button4 = ttk.Button(frame)
    button4.grid(row=3, column=0)

    button5 = ttk.Button(frame)
    button5.grid(row=3, column=1)

    button6 = ttk.Button(frame)
    button6.grid(row=3, column=2)

    button7 = ttk.Button(frame)
    button7.grid(row=4, column=0)

    button8 = ttk.Button(frame)
    button8.grid(row=4, column=1)

    button9 = ttk.Button(frame)
    button9.grid(row=4, column=2)

    x_button = ttk.Button(frame, text ="X's")
    x_button.grid(row=1,column=0)

    o_button = ttk.Button(frame, text ="O's")
    o_button.grid(row=1,column=1)

    turn_lable = ttk.Label(frame, text="Who's turn is it?")
    turn_lable.grid(row=0, column=0)

    holder1 = ttk.Label(frame, text='---')
    holder2 = ttk.Label(frame, text='---')
    holder3 = ttk.Label(frame, text='---')
    holder4 = ttk.Label(frame, text='---')
    holder5 = ttk.Label(frame, text='---')
    holder6 = ttk.Label(frame, text='---')
    holder7 = ttk.Label(frame, text='---')
    holder8 = ttk.Label(frame, text='---')
    holder9 = ttk.Label(frame, text='---')

    play_again_lable = ttk.Label(frame, text="To restart or play again, close the window and click 'PLAY' again")
    play_again_lable.grid(row=5, column=4)

    s = Scorer()
    x_button['command'] = lambda: handle_x(mqtt_sender, s)
    o_button['command'] = lambda: handle_o(mqtt_sender, s)

    running_score = [2,2,2,2,2,2,2,2,2]

    button1['command'] = lambda: handle_button1(mqtt_sender,button1,holder1,s,running_score,frame)
    button2['command'] = lambda: handle_button2(mqtt_sender,button2,holder2,s,running_score,frame)
    button3['command'] = lambda: handle_button3(mqtt_sender,button3,holder3,s,running_score,frame)
    button4['command'] = lambda: handle_button4(mqtt_sender,button4,holder4,s,running_score,frame)
    button5['command'] = lambda: handle_button5(mqtt_sender,button5,holder5,s,running_score,frame)
    button6['command'] = lambda: handle_button6(mqtt_sender,button6,holder6,s,running_score,frame)
    button7['command'] = lambda: handle_button7(mqtt_sender,button7,holder7,s,running_score,frame)
    button8['command'] = lambda: handle_button8(mqtt_sender,button8,holder8,s,running_score,frame)
    button9['command'] = lambda: handle_button9(mqtt_sender,button9,holder9,s,running_score,frame)

    return frame

class Scorer(object):
    def __init__(self):
        self.turn = 0

def keeping_score( Scorer, button, seq):
    seq = seq
    seq[button-1] = Scorer.turn















def handle_ledProx(mqtt_sender, speed, start_time, rate):
    print('ledProx')
    mqtt_sender.send_message('ledProx', [speed, start_time, rate])

def handle_get_with_camera(mqtt_sender, left_or_right, speed, start_time, rate):
    print('camera with LED')
    mqtt_sender.send_message('go_get_with_camera',[left_or_right, speed, start_time, rate])

def handle_turn_90(mqtt_sender, speed, right_left): # , button):
    print('turn 90')
    mqtt_sender.send_message('turn_90', [right_left, speed])
    # return button.grid_remove()








def handle_button1(mqtt_sender,button,holder,s,running_score, frame):
    print('button1 function')
    mqtt_sender.send_message('go_to_space1')
    keeping_score(s, 1, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=2, column=0)

def handle_button2(mqtt_sender,button,holder,s,running_score, frame):
    print('button2 function')
    mqtt_sender.send_message('go_to_space2')
    keeping_score(s, 2, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=2, column=1)

def handle_button3(mqtt_sender,button,holder,s,running_score, frame):
    print('button3 function')
    mqtt_sender.send_message('go_to_space3')
    keeping_score(s, 3, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=2, column=2)

def handle_button4(mqtt_sender,button,holder,s,running_score, frame):
    print('button4 function')
    mqtt_sender.send_message('go_to_space4')
    keeping_score(s, 4, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=3, column=0)

def handle_button5(mqtt_sender,button,holder,s,running_score, frame):
    print('button5 function')
    mqtt_sender.send_message('go_to_space5')
    keeping_score(s, 5, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=3, column=1)

def handle_button6(mqtt_sender,button,holder,s,running_score, frame):
    print('button6 function')
    mqtt_sender.send_message('go_to_space6')
    keeping_score(s, 6, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=3, column=2)

def handle_button7(mqtt_sender,button,holder,s,running_score, frame):
    print('button7 function')
    mqtt_sender.send_message('go_to_space7')
    keeping_score(s, 7, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=4, column=0)

def handle_button8(mqtt_sender,button,holder,s,running_score, frame):
    print('button8 function')
    mqtt_sender.send_message('go_to_space8')
    keeping_score(s, 8, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=4, column=1)

def handle_button9(mqtt_sender,button,holder,s,running_score, frame):
    print('button9 function')
    mqtt_sender.send_message('go_to_space9')
    keeping_score(s, 9, running_score)
    print(running_score)
    score_tracker(running_score, frame)
    return button.grid_remove(),holder.grid(row=4, column=2)


def handle_x(mqtt_sender, scorer):
    print("X's turn")
    scorer.turn = 0
    mqtt_sender.send_message('x_turn')

def handle_o(mqtt_sender, scorer):
    print("O's turn")
    scorer.turn = 1
    mqtt_sender.send_message('y_turn')

def score_tracker(running_score, frame):
    win_lable = ttk.Label(frame, text='Winner!')
    lose_lable =ttk.Label(frame, text='LOSERS')
    if running_score[0] != 2 and running_score[1] != 2 and running_score[2] != 2:
        if running_score[0] == running_score[1] and running_score[1] == running_score[2]:
            win_lable.grid(row=2, column=4)
    if running_score[3] != 2 and running_score[4] != 2 and running_score[5] != 2:
        if running_score[3] == running_score[4] and running_score[4] == running_score[5]:
            win_lable.grid(row=2, column=4)
    if running_score[6] != 2 and running_score[7] != 2 and running_score[8] != 2:
        if running_score[6] == running_score[7] and running_score[7] == running_score[8]:
            win_lable.grid(row=2, column=4)
    if running_score[0] != 2 and running_score[3] != 2 and running_score[6] != 2:
        if running_score[0] == running_score[3] and running_score[3] == running_score[6]:
            win_lable.grid(row=2, column=4)
    if running_score[1] != 2 and running_score[4] != 2 and running_score[7] != 2:
        if running_score[1] == running_score[4] and running_score[4] == running_score[7]:
            win_lable.grid(row=2, column=4)
    if running_score[2] != 2 and running_score[5] != 2 and running_score[8] != 2:
        if running_score[2] == running_score[5] and running_score[5] == running_score[8]:
            win_lable.grid(row=2, column=4)
    if running_score[0] != 2 and running_score[4] != 2 and running_score[8] != 2:
        if running_score[0] == running_score[4] and running_score[4] == running_score[8]:
            win_lable.grid(row=2, column=4)
    if running_score[6] != 2 and running_score[4] != 2 and running_score[2] != 2:
        if running_score[6] == running_score[4] and running_score[4] == running_score[2]:
            win_lable.grid(row=2, column=4)
    if running_score[0] != 2 and running_score[1] != 2 and running_score[2] != 2 and running_score[3] != 2 and running_score[4] != 2 and running_score[5] != 2 and running_score[6] != 2 and running_score[7] != 2 and running_score[8] != 2:
        lose_lable.grid(row=2, column=4)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()