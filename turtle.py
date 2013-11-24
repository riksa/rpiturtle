#-----------------------------------
# Name: Stepper Motor
#
# Author: matt.hawkins
#
# Created: 11/07/2012
# Copyright: (c) matt.hawkins 2012
#-----------------------------------
#!/usr/bin/env python
 
# Import required libraries
import time
import RPi.GPIO as GPIO
 
# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
 
# Define GPIO signals to use
# Pins 18,22,24,26
# GPIO24,GPIO25,GPIO8,GPIO7
StepPins = [24,25,8,7]
StepPins2 = [22,10,9,11]

STEPS_PER_CM=158
 
# Set all pins as output
for pin in StepPins:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
for pin in StepPins2:
  print "Setup pins"
  GPIO.setup(pin,GPIO.OUT)
  GPIO.output(pin, False)
 
# Define some settings
StepCounter = 0
WaitTime = 0.01
 
# Define simple sequence
StepCount1 = 4
Seq1 = []
Seq1 = range(0, StepCount1)
Seq1[0] = [1,0,0,0]
Seq1[1] = [0,1,0,0]
Seq1[2] = [0,0,1,0]
Seq1[3] = [0,0,0,1]
 
# Define advanced sequence
# as shown in manufacturers datasheet
StepCount2 = 8
Seq2 = []
Seq2 = range(0, StepCount2)
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]
 
# Choose a sequence to use
Seq = Seq1
StepCount = StepCount1

class Stepper(object):
  name = "NONAME"
  pins =[]
  stepcounter = 0
  def __init__(self, pins=[24,25,8,7], name="L" ):
    self.name = name
    self.pins = pins
    self.stepCounter = 0

  def step(self, dir):
    self.stepCounter += dir
    if self.stepCounter < 0:
      self.stepCounter += StepCount
    if self.stepCounter >= StepCount:
      self.stepCounter -= StepCount

#    print " Motor %s counter %d" %(self.name,self.stepCounter)    
    for pin in range(0, 4):
      xpin = self.pins[pin]
      if Seq[self.stepCounter][pin]!=0:
#        print " Step %i Enable %i" %(self.stepCounter,xpin)
        GPIO.output(xpin, True)
      else:
        GPIO.output(xpin, False)

def forward( steps ):
  print "Forward %s" %steps
  for step in xrange(0,steps):
    stepperL.step(1)
    stepperR.step(1)
    time.sleep(WaitTime)

def backward( steps ):
  print "Backward %s" %steps
  for step in xrange(0,steps):
    stepperL.step(-1)
    stepperR.step(-1)
    time.sleep(WaitTime)

def left( steps ):
  print "Left %s" %steps
  for step in xrange(0,steps):
    stepperL.step(1)
    stepperR.step(-1)
    time.sleep(WaitTime)

def right( steps ):
  print "Right %s" %steps
  for step in xrange(0,steps):
    stepperL.step(-1)
    stepperR.step(1)
    time.sleep(WaitTime)

# waarin pain
stepperL = Stepper( [24,25,8,7], "L")
stepperR = Stepper( [22,10,9,11], "R")

forward( 10*STEPS_PER_CM )
 
# Start main loop
#while 1==1:
#  right( 1 )
#  StepCounter+=1
#  print "StepCounter %d" %StepCounter
#  backward( 10 )

      
