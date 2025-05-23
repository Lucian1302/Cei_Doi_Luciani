#!/usr/bin/env python
import rospy
import actionlib
from std_srvs.srv import Empty
from action_as.msg import ArdroneAction, ArdroneGoal, ArdroneResult

class DroneCommandActionServer(object):
    def __init__(self):
        rospy.init_node('comanda')
       
        self._as = actionlib.SimpleActionServer(
            'drone_command',
            DroneCommandAction,
            execute_cb=self.execute_cb,
            auto_start=False
        )
       
        self._feedback = DroneCommandFeedback()
        self._result   = DroneCommandResult()
        
        rospy.loginfo("Se asteapta comanda")
        rospy.wait_for_service('/drone/takeoff')
        rospy.wait_for_service('/drone/land')
        self._srv_takeoff = rospy.ServiceProxy('/drone/takeoff', Empty)
        self._srv_land    = rospy.ServiceProxy('/drone/land',    Empty)

        self._as.start()
       

    def execute_cb(self, goal):
        cmd = goal.command.strip().upper()
        rate = rospy.Rate(1)  

        if cmd == "TAKEOFF":
            rospy.loginfo("Va decola")
            try:
                self._srv_takeoff()
            except rospy.ServiceException as e:
                rospy.logerr("Eroare takeoff: %s", e)
                self._as.set_aborted()
                return

            
            while not rospy.is_shutdown():
                if self._as.is_preempt_requested():
                    rospy.loginfo("Preempt primit – trec la LAND")
                    self._as.set_preempted()
                    return
                self._feedback.status = "taking off"
                self._as.publish_feedback(self._feedback)
                rate.sleep()

        elif cmd == 'LAND':
            rospy.loginfo("Comandă LAND primită")
            try:
                self._srv_land()
            except rospy.ServiceException as e:
                rospy.logerr("Eroare land: %s", e)
                self._as.set_aborted()
                return

            
            for _ in range(3):
                if rospy.is_shutdown():
                    break
                self._feedback.status = "landing"
                self._as.publish_feedback(self._feedback)
                rate.sleep()

            rospy.loginfo("DroneCommand LAND finalizat")
            self._as.set_succeeded(self._result)

        else:
            rospy.logwarn("Comandă necunoscută: %s", cmd)
            self._as.set_aborted()

if __name__ == '__main__':
    server = DroneCommandActionServer()
    rospy.spin()
