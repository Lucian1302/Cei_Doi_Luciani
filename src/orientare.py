#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist

rospy.init_node("Move")
rate=rospy.Rate(2)
move=Twist()
ok=1
def callback(msg):
	while ok==1:
		if msg.pose.pose.position.x<=0:
			move.linear.x+=0.1
		elif msg.pose.pose.position.x>=1:
			move.linear.x-=0.1
	

pub=rospy.Publisher('cmd_vel',Twist,queue_size=1)
sub=rospy.Subscriber('/odom',Odometry,callback)

while not rospy.is_shutdown():
	pub.publish(move)

