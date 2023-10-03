from tkinter import messagebox
import psutil

battery = psutil.sensors_battery()


def show_message_box(percent, is_charging):
    title = "Battery Status"
    if is_charging:
        msg = "Battery at " + str(percent) + "%. Unplug charger"
    else:
        msg = "Battery at " + str(percent) + "%. Plug charger"
    messagebox.showinfo(title, msg)


if battery.percent > 85 and battery.power_plugged or battery.percent < 30 and not battery.power_plugged:
    show_message_box(battery.percent, battery.power_plugged)
