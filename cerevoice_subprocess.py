#!/usr/bin/env python
import subprocess
import signal
import time
import sys
import os

class CerevoiceProcess:
  def __init__( self, cerevoiceExecutableScript ):
    executable = cerevoiceExecutableScript 
    self.proc = subprocess.Popen(executable,
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            preexec_fn=os.setsid )
    while True:
      if os.path.exists("./cerevoice_output.wav"):
        break;
    #time.sleep(0.1)
    #os.killpg(self.proc.pid, signal.SIGTERM)

    os.system( "play ./cerevoice_output.wav" )
    os.system( "rm ./cerevoice_output.wav" )
