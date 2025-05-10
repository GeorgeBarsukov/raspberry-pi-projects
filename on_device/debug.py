import time
import subprocess

# Take a screenshot
def take_screenshot(save_path='/tmp/screenshot.png'):
    try:
        subprocess.run(['grim', save_path], check=True)
        print(f"Screenshot saved to {save_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to take screenshot with grim: {e}")


while True:
    take_screenshot()
    time.sleep(5)
