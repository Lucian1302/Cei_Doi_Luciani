#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan

rospy.init_node("Nod")

move=Twist()

def callback(msg):
	while msg.ranges[179]>=1:
		move.linear.x=0.5
	while msg.ranges[179]<1:
		move.linear.x=0
		move.angular.z=1.57
		move.linear.x=0.5
	while msg.ranges[0]<1:
		move.linear.x=0
		move.angular.z=1.57
		move.linear.x=0.5

	while msg.ranges[359]<1:

		move.linear.x=0
		move.angular.z=-1.57
		move.linear.x=0.5

pub=rospy.Publisher("/cmd_vel",Twist,queue_size=1)
sub=rospy.Subscriber("/scan",LaserScan,callback)


while not rospy.is_shutdown():
	pub.publish(move)
	rospy.sleep(0.25)
rospy.spin()


