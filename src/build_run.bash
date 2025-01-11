#!/bin/bash

# Function to terminate all processes
terminate_processes() {
    echo "Terminating all processes..."
    kill $gzserver_pid $slam_pid $rviz_pid $rqt_pid $nav_demo_pid
    killall -9 gazebo gzserver gzclient
    wait $gzserver_pid $slam_pid $rviz_pid $rqt_pid $nav_demo_pid 2>/dev/null
    exit 0
}

# Trap termination signals
trap terminate_processes SIGINT SIGTERM

# Build the project
cd ~/Robotics/
colcon build
source install/setup.bash

# Run gazebo
ros2 launch CoffeeBot assessment.launch.py &
gzserver_pid=$!

ros2 launch navigation_demos nav_demo.launch.py &
slam_pid=$!

rviz2 &
rviz_pid=$!

# Wait for any process to exit
wait -n

# Terminate all processes if any of them exits
terminate_processes