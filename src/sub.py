#!/usr/bin/env python
import rospy
from Cei_Doi_Luciani.msg import Robot

rospy.init_node("Nod2")

def callback(msg):
	print(msg.nume, msg.nr_roti,msg.unghi)

sub=rospy.Subscriber('/topic',Robot,callback)
rospy.spin()

