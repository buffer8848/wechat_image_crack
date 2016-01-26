#!/usr/bin/python
# coding=utf-8
#
# 179770346@qq.com / binfeix.li@intel.com
# 2016/1/26 v0.1
#   execute cmd and save snapshot.

import sys
from com.android.monkeyrunner import MonkeyRunner

#-------------------------------------------------------------------------------------------------- 
# Lookup table to map command strings to functions that implement that
# command.
CMD_MAP = {
  'TOUCH': lambda dev, arg: dev.touch(**arg),
  'DRAG': lambda dev, arg: dev.drag(**arg),
  'PRESS': lambda dev, arg: dev.press(**arg),
  'TYPE': lambda dev, arg: dev.type(**arg),
  'WAIT': lambda dev, arg: MonkeyRunner.sleep(**arg)
}
 
# Process a single file for the specified device.
def process(device, cmd, parameter, time):
  try:
    # Parse the pydict
    rest = eval(parameter)
  except:
    print 'unable to parse options'
    exit(-1)
 
  if cmd not in CMD_MAP:
    print 'unknown command: ' + cmd
 
  CMD_MAP[cmd](device, rest)
  MonkeyRunner.sleep(time)
  pic = device.takeSnapshot()
  CMD_MAP[cmd](device, rest)

  return pic

#-------------------------------------------------------------------------------------------------- 
def main():
  touch_cmd = "TOUCH"
  touch_parameter = "{'x':300,'y':900,'type':'downAndUp',}"

  out_folder = sys.argv[1]

  device = MonkeyRunner.waitForConnection()
 
  #1. save origin snapshot
  pic = process(device, touch_cmd, touch_parameter, 4.0)
  pic.writeToFile("%s/0.png" % out_folder, "png")
  #2. save more new snaoshot, count 100 is enough
  for index in range(1, 100):
    pic = process(device, touch_cmd, touch_parameter, 2.0)
    pic.writeToFile("%s/%d.png" % (out_folder, index), "png") 
 
if __name__ == '__main__':
  main()