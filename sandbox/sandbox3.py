# Put whatever you want in this module and do whatever you want with it.
# It exists here as a place where you can "try out" things without harm.



led_button = ttk.Button(frame, text='')


led_button.grid(row=0,column = 1)

def handle_led_button(mqtt_sender, led_speed_entry, led_start_time_entry, led_rate_entry):
    print('led')
    mqtt_sender.send_message('pick_up_object_with_led', [led_speed_entry.get(), led_start_time_entry.get(), led_rate_entry.get()])

