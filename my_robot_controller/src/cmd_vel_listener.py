#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

def cmd_vel_callback(msg):
    rospy.loginfo("Received cmd_vel message: linear = (%f, %f, %f), angular = (%f, %f, %f)",
                  msg.linear.x, msg.linear.y, msg.linear.z,
                  msg.angular.x, msg.angular.y, msg.angular.z)

def listener():
    rospy.init_node('cmd_vel_listener', anonymous=True)
    rospy.Subscriber("cmd_vel", Twist, cmd_vel_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
