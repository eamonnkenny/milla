#!/usr/bin/env python
import subprocess
import signal
import time
import sys
import os

class KaldiProcess:
  def __init__( self, kaldiExecutableScript ):
    self.proc = subprocess.Popen(kaldiExecutableScript, 
                            shell=True,
                            stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE,
                            preexec_fn=os.setsid )
    self.pid = self.proc.pid

  def getline(self):
    output = self.proc.stdout.readline()
    if output.rstrip() != "":
      print "Reading: (" +  output.rstrip().lstrip() + ")"

    return output.rstrip().lstrip()

  def destroy(self):
    os.killpg( self.pid, signal.SIGTERM )
    print "Destroying kaldi process gracefully"
