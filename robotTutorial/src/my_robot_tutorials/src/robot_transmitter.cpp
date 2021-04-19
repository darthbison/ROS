#include <ros/ros.h>
#include <std_msgs/String.h>


int main(int argc, char **argv)
{
    ros::init(argc, argv, "robot_transmitter");

    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::String>("/robot_news_radio",10);

    ros::Rate rate(3);

    while (ros::ok())
    {
        std_msgs::String msg;
        msg.data = "Hi this is the CPP message";
        pub.publish(msg);
        rate.sleep();
    }

}