#!/bin/sh

WS=$1
PROJECTNAME=$2

mkdir -p $WS
cd $WS
mkdir -p src
catkin_make
cd devel/
source setup.bash 
cd src/
catkin_create_pkg $PROJECTNAME roscpp rospy std_msgs

