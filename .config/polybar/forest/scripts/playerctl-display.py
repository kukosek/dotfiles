#!/usr/bin/python3.9
import subprocess
import textwrap
try:
    playing = subprocess.check_output(['playerctl', 'status'], stderr=subprocess.STDOUT).decode('utf-8').strip() == "Playing"
except subprocess.CalledProcessError:
    playing = False
if playing:
    track_title = ""
    track_author = ""

    metadata = subprocess.check_output(['playerctl', 'metadata']).decode('utf-8')
    for line in metadata.splitlines():
        source, meta, value = line.split(' ', 2)
        meta = meta.strip()
        value = value.strip()
        if meta == "xesam:title":
            track_title = value
        if meta == "xesam:artist":
            track_author = value
    if len(track_title+track_author) > 30:
        print(textwrap.shorten(track_title, width=45, placeholder="..."))
    else:
        print(track_author+" - "+track_title)
else:
    print("Offline")

