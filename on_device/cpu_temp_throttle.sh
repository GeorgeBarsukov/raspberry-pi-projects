#!/bin/bash

# Settings
THROTTLE_TEMP=75000    # 75.0°C
RECOVER_TEMP=65000     # 65.0°C
NORMAL_FREQ="1500000"  # Normal CPU frequency in kHz (example: 1.5GHz)
LOW_FREQ="600000"      # Throttled CPU frequency in kHz (example: 600MHz)
CHECK_INTERVAL=5       # How often to check (in seconds)

# Helper functions
throttle_cpu() {
  echo "Throttling CPU to $LOW_FREQ kHz"
  sudo cpufreq-set -u "${LOW_FREQ}" >/dev/null
}

restore_cpu() {
  echo "Restoring CPU to $NORMAL_FREQ kHz"
  sudo cpufreq-set -u "${NORMAL_FREQ}" >/dev/null
}

# Main loop
is_throttled=0

while true; do
  temp=$(cat /sys/class/thermal/thermal_zone0/temp)

  if (( temp >= THROTTLE_TEMP )); then
    if (( is_throttled == 0 )); then
      throttle_cpu
      is_throttled=1
    fi
  elif (( temp <= RECOVER_TEMP )); then
    if (( is_throttled == 1 )); then
      restore_cpu
      is_throttled=0
    fi
  fi

  sleep "$CHECK_INTERVAL"
done
