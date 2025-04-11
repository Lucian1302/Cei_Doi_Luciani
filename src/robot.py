#!/usr/bin/env python
import rospy
from Cei_Doi_Luciani.msg import Mesaj1
rospy.init_node("nod")

rate=rospy.Rate(2)
mesaj=Mesaj1()
pub=rospy.Publisher('/topic', Mesaj1, queue_size=1)
mesaj.nume="Robot"
mesaj.model="nou"
mesaj.an_fabricatie=2002
mesaj.greutate=800.0


while not rospy.is_shutdown():
	print(mesaj.nume)
	print(mesaj.model)
	print(mesaj.an_fabricatie)
	print(mesaj.greutate)
	pub.publish(mesaj)
	rate.sleep()
