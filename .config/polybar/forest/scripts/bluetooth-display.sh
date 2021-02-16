#!/bin/bash
devices_connected=$(bash -c "bluetoothctl devices | cut -f2 -d' ' | while read uuid; do bluetoothctl info $uuid; done|grep -E \"Connected|Name\" | grep -oE '[^ ]+$'")
my_array=($(echo $devices_connected | tr " " "\n"))
if [ ${#my_array[@]} != 0 ] && [ ${my_array[1]} == "yes" ]; then
	echo " ${my_array[0]}"
elif [[ $(pgrep -f blueman-manager) ]]; then
	echo "  "
else
	echo "  "
fi
