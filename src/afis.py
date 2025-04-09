#!/usr/bin/env python
import rospy
x=0
rospy.init_node("Node")
while not rospy.is_shutdown():
	print(x)
	x+=1

