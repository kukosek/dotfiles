#!/usr/bin/python3

import sys
import json, subprocess

output = subprocess.check_output(['i3-msg', '-t', 'get_workspaces'])
workspaces = json.loads(output)

next_num = next(i for i in range(1, 100) if not [ws for ws in workspaces if ws['num'] == i])

if "-m" in sys.argv:
    subprocess.call(['i3-msg', 'move to workspace %i' % next_num])
else:
    subprocess.call(['i3-msg', 'workspace number %i' % next_num])
