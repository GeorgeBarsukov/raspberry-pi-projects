#!/bin/bash

# Run indefinitely
while true; do
  temp=$(vcgencmd measure_temp)
  echo "$(date '+%H:%M:%S') - CPU Temp: $temp"
  sleep 1
done

