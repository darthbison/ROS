#!/usr/bin/env python

import rospy
from rospy_tutorials.srv import AddTwoInts

def handle_add_two_ints(req):
    result = req.a + req.b
    rospy.loginfo("Sum of " + str(req.a) + " and " +  str(req.b) + " is " + str(result))
    return result

if __name__ == '__main__':
    rospy.init_node("add_two_ints_client")
    rospy.wait_for_service("/add_two_ints")

    try:
        add_two_ints = rospy.ServiceProxy("/add_two_ints", AddTwoInts)
        response = add_two_ints(12, 50)
        rospy.loginfo("Sum is : " + str(response.sum))
        
    except rospy.ServiceException as e:
        rospy.logwarn("Service is not running: " + str(e))
    
    