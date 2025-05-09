#!/usr/bin/env python
import rospy
from services_pkg.srv import serv,servResponse 
from geometry_msgs.msg import Twist
move=serv()
servv=move.side
rep=serv.repetitions()

def my_callback(request):
    rospy.loginfo("Make a circle")
   for i in range(rep):
    	 move_circle.linear.x = 0.2
   	 move_circle.angular.z = move_circle.linear.x/servv
    	 my_pub.publish(move_circle)
    	 rospy.loginfo("One circle is done")
    return servResponse()

rospy.init_node('move_in_circle') 
my_service = rospy.Service('/move_in_circle', serv , my_callback)
my_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
move_circle = Twist()

rospy.spin()

