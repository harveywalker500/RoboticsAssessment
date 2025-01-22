import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node, SetParameter
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    ld = LaunchDescription()

     # Specify the name of the package and path to map yaml file
    pkg_name = 'navigation_demos'
    pkg_dir = get_package_share_directory(pkg_name)
    map_subpath = 'maps/my_map.yaml'
    map_yaml_filepath = os.path.join(get_package_share_directory(pkg_name), map_subpath)

    # map server node
    # Publishes a 2D occupancy grid based on a .pgm (and accompanying .yaml) file
    node_map_server = Node(
        package='nav2_map_server',
        executable='map_server',
        name='example_map_server',
        output='screen',
        parameters=[{'yaml_filename': map_yaml_filepath}] # add other parameters here if required
    )

    # Lifecycle Manager - Ensures localisation waits for map to be published etc
    lifecycle_nodes = ['example_map_server']
    node_lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        output='screen',
        parameters=[{'node_names':lifecycle_nodes, 'autostart': True}] # add other parameters here if required
    )


    # Add actions to LaunchDescription
    ld.add_action(SetParameter(name='use_sim_time', value=True))
    ld.add_action(node_lifecycle_manager)
    ld.add_action(node_map_server)
    
    return ld
