#!/usr/bin/python3

from HumanTracker import HumanTracker
import rospy
import time

tracking_ugv = HumanTracker(auto_init=True)
tracking_ugv.start_human_detection()
tracking_ugv.start_tracking()

while True:
    if rospy.is_shutdown():
        print("Shutting down...")
        tracking_ugv.kill = True
        time.sleep(2)
        break
    
print("Program End.")

