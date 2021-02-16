#!/bin/bash
if [[ ! $(pgrep -f blueman-manager) ]]; then
	blueman-manager &
else
	killall -s TERM blueman-manager
fi
