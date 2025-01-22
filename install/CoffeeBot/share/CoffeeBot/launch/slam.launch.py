import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node, SetParameter
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    ld = LaunchDescription()


    # Specify the name of the package and path to map yaml file
    pkg_name = 'gazebo_ros'
    pkg_dir = get_package_share_directory(pkg_name)
   

     # Start SLAM Toolbox with default parameters
    launch_slam_toolbox = IncludeLaunchDescription(
      PythonLaunchDescriptionSource([os.path.join(
         get_package_share_directory('slam_toolbox'), 'launch'),
         '/online_async_launch.py'])
      )

    # Add actions to LaunchDescriptio
    ld.add_action(launch_slam_toolbox)
   
    return ld
