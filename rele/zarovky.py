#!/usr/bin/python

import RPi.GPIO as GPIO
import time

def myinit():
    #GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)


def vypni4():
    GPIO.output(4, True)

def zapni4():
    GPIO.output(4, False)

def vypni17():
    GPIO.output(17, True)

def zapni17():
    GPIO.output(17, False)

def cleanup():
    GPIO.cleanup()


