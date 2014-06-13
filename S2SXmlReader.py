#!/usr/bin/env python

import sys
import string
import time
import datetime
import libxml2
from lxml import etree
from kaldi_subprocess import KaldiProcess
from cerevoice_subprocess import CerevoiceProcess
import re
import os

class SpeechToSpeechPrototype:
  def __init__( self, fileName ):
    """read all recognition prompts and response prompts from an XML file
       and produce some actions"""
    self.dryrun = False
    self.readXml( fileName )
    
  def readXml( self, fileName ):
    """read an XML file and extract its different elements
        currently consisting of recognition words and spoken output"""

    root = etree.parse(fileName)
    dialogues = root.findall("Dialogue")

    # start up the subprocess relating to kaldi
    # this will capture the standard output
    kaldiObject = KaldiProcess("./kaldi-using-voxforge-data.sh")

    dialogueCount = 0
    for dialogue in dialogues:
      dialogueCount = dialogueCount + 1
      elements = dialogue.getchildren()
      recognition = elements[0] 

      words = recognition.getchildren()
      # this is looking at the children of recognition which are <Words>
      keywords = []
      for word in words:
        keywords.append( word.text )
      print keywords

      # next look for a recognised word in our grammar list
      counter = 0
      while True:
        counter = counter + 1
        recognisedLine = kaldiObject.getline()
        if recognisedLine.lower() in keywords:
          print "I recognised the line: ", recognisedLine
          break;

      say = elements[1] 
      self.writeSpeechSentences( say.text )
      
      CerevoiceProcess( "./cerevoice-using-heather-voice.sh" )

    kaldiObject.destroy()

    #dialogues = root.Element("Dialogue")
    #for dialogue in dialogues:
      #print dialogue

  def writeSpeechSentences( self, sentences ):
    fp = open( './cerevoice_input_file.txt', 'w' )
    fp.write( sentences )
    fp.close()

  def readAllRecognitionWords( self, fileName ):
    xmlParser = libxml2.parseFile( fileName )
    tree = xmlParser.xpathNewContext()
    words = tree.xpathEval("/Dialogue/Recognition/Words/text()")
    for word in words:
      print word

def usage( argv ):
  print 'Error: Too few arguments, no XML input file specified, exiting now!\n'
  print 'Usage: ' + argv[0] + ' <speech-to-speech-description.xml>\n\n'
  print '   Please try again!'
  sys.exit(1)

def main( argv ):
  """This is the main function for this python script"""
  
  if ( len(argv) == 1 ):
    usage( argv )

  XmlInputFile = argv[1]

  SpeechToSpeechPrototype( XmlInputFile )

if __name__ == "__main__":
  main( sys.argv )
