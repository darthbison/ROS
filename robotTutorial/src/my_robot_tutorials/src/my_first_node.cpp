#include <ros/ros.h>
#include<string>
#include <my_robot_msgs/HardwareStatus.h>

using namespace std;

int main(int argc, char **argv)
{
    ros::init(argc, argv, "my_first_cpp_node");
    ros::NodeHandle nh;

    ROS_INFO("Node has been started");


    my_robot_msgs::HardwareStatus msg;

    string name;
    nh.getParam("/robot_name", name);

    cout << name << endl;

    ros::Rate rate(10);

    while (ros::ok)
    {
        ROS_INFO("Hello");
        rate.sleep();
    }
}
    
