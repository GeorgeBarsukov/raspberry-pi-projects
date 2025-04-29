# This script connects to a Raspberry Pi via SSH, retrieves a screenshot image from the /tmp directory, opens it with the default image viewer, and then deletes the local copy of the image.
scp -i raspberrypi.pem admin@raspberrypi.local:/tmp/screenshot.png .
explorer screenshot.png
rm screenshot.png