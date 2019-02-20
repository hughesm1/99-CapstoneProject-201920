import rosebot
import time
import math

def moon_rocks(robot, initial_speed, r):


def how_many():

def print_to_laptop(num, start_time, r):
    print('time from start is', time.time() - start_time)
    r.send_message('the_time')
    r.send_message('print_GUI', [time.time() - start_time])
    print('Its all over. The number of moon rocks you picked up was', num)
    r.send_message('num_of_rocks')
    r.send_message('print_GUI', [num])