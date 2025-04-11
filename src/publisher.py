#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
rospy.init_node("Hi")

move=Twist()
rate=rospy.Rate(2)
pub=rospy.Publisher('/cmd_vel',Twist,queue_size=1)

while not rospy.is_shutdown():
	move.linear.x+=-0.0001
	pub.publish(move)
	rate.sleep()
