#!/usr/bin/env python
import rospy
from Cei_Doi_Luciani.msg import Robot
rospy.init_node("Nod")
pub=rospy.Publisher('/topic', Robot,queue_size=1)
rate=rospy.Rate(5)
robot=Robot()
robot.nume="Marin"
robot.nr_roti=4
robot.unghi=32.2
while not rospy.is_shutdown():
	print(robot.nume,robot.nr_roti,robot.unghi)
	pub.publish(robot)
	rate.sleep()


