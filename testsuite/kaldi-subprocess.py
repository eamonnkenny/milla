#!/usr/bin/env python
import subprocess
import signal
import time
import sys
import os

proc = subprocess.Popen('../kaldi-using-voxforge-data.sh', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        preexec_fn=os.setsid )

print 'You can speak now, Kaldi is running.'
counter = 0
while True:
    #proc.stdin.write('%d\n' % it)
    output = proc.stdout.readline()

    # process each output line if its not blank
    if output.rstrip() != "":
      print str(counter) + ": " +  output.rstrip()
      counter = counter + 1
    
    # exit kaldi if we have read three lines
    if counter == 3:
      print "about to kill kaldi process: ", proc.pid
      os.killpg(proc.pid, signal.SIGTERM)
      print "Exiting from Kaldi"
      sys.exit(1)
