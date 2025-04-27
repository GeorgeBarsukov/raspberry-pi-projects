## Setup
Some small details are omitted, like making files executable, cleanup, and other basics.
- Installed Raspberry Pi latest OS via imager  
    https://www.raspberrypi.com/software/
- Connected mouse via bluetoothctl  
    ```
    ctl+alt+T  
    bluetoothctl  
    power on  
    scan on  
    pair MAC_ADDRESS  
    connect MAC_ADDRESS  
    ```
- Installed waydroid with google apps  
    ```
    sudo apt install waydroid  
    sudo waydroid init -s GAPPS  
    waydroid container start  
    ```
- Downloaded sqlite3 binary for ARM64  
    https://github.com/rojenzaman/sqlite3-arm-aarch64  
- Launched file server  
    python3 -m http.server 8000  
- From waydroid, downloaded the binary  
    ```
    curl http://HOST_IPV4:8000/sqlite3 -o sqlite3  
    ```
- Ran query to find android_id  
    ```
    sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "SELECT * FROM main WHERE name = 'android_id';"
    ```
- Registered android_id on google.com/android/uncertified  
    https://www.google.com/android/uncertified/