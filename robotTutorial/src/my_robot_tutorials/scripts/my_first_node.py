#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('first_python_node')
    rospy.loginfo('Node has started')
    rate = rospy.Rate(10)

    name = rospy.get_param("/robot_name")

    rospy.loginfo(name)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()