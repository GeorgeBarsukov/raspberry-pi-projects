import uinput
import time
import random
import subprocess
import os
import schedule

# Globals
PACKAGE_NAME = 'com.playstudios.showstar'
running = True
events = (uinput.BTN_LEFT, uinput.ABS_X + (0, 3840, 0, 0), uinput.ABS_Y + (0, 2160, 0, 0))
device = uinput.Device(events)

# Randomize time
def rt(time, deviation=.1):
    return(time + time * (2 * (random.random() - .5)) * deviation)

# Take a screenshot
def take_screenshot(save_path='/tmp/screenshot.png'):
    try:
        subprocess.run(['grim', save_path], check=True)
        print(f"Screenshot saved to {save_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to take screenshot with grim: {e}")

# Shut down the app
def shut_down_app():
    print("Shutting down app")
    subprocess.run(['adb', 'shell', 'am', 'force-stop', PACKAGE_NAME])
    running = False

# Start the application and click through the 3 ads
def startup_app():
    print("Starting app")
    time.sleep(3)
    subprocess.run(['waydroid', 'app', 'launch', PACKAGE_NAME])
    time.sleep(rt(15))
    tap_corner()
    time.sleep(rt(15))
    tap_corner()
    time.sleep(rt(15))
    tap_corner()
    running = True

def tap(x, y):
    print(f'Tapping on {str((x,y))}')
    # device.emit(uinput.ABS_X, x, syn=False)
    # device.emit(uinput.ABS_Y, y, syn=False)
    # device.emit(uinput.BTN_LEFT, 1)
    # time.sleep(0.1)
    # device.emit(uinput.BTN_LEFT, 0)
    subprocess.run(
            ['sudo', 'waydroid', 'shell', 'input', 'tap', str(x), str(y)],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True  # raises CalledProcessError if nonzero exit
    )

def tap_screen():
    #tap(3650, 350)
    tap(1850, 200)

def tap_corner():
    #tap(3650, 150)
    tap(1850, 80)

def tap_both():
    tap_corner()
    time.sleep(rt(5))
    tap_screen()
    time.sleep(rt(5))
    tap_corner()

print("Application starting...")

startup_app()

# Setup
#events = (uinput.BTN_LEFT, uinput.REL_X, uinput.REL_Y)
events = (uinput.BTN_LEFT, uinput.ABS_X + (0, 1920, 0, 0), uinput.ABS_Y + (0, 1080, 0, 0))
device = uinput.Device(events)

# Schedule startup at 6am and 6pm
schedule.every().day.at("06:00").do(startup_app)
schedule.every().day.at("18:00").do(startup_app)

# Schedule shutdown at 10am and 10pm
schedule.every().day.at("10:00").do(shut_down_app)
schedule.every().day.at("22:00").do(shut_down_app)

# Main loop
try:
    while True:
        if running:
            tap_screen()
            # -ef tap_both()
        take_screenshot() 

        schedule.run_pending()

        interval = rt(60) 
        time.sleep(interval)
except KeyboardInterrupt:
    print("\nMouse clicker stopped.")
finally:
    shut_down_app()
