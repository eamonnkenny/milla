#!/usr/bin/env python
import subprocess
import signal
import time
import sys
import os

proc = subprocess.Popen('./cerevoice-using-heather-voice.sh', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        preexec_fn=os.setsid )
while True:
  if os.path.exists("./cerevoice_output.wav"):
    os.killpg(proc.pid, signal.SIGTERM)
    break;
