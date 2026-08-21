from launch import LaunchDescription
from launch_ros.actions import Node
import os

def generate_launch_description():
    # Path to your Xacro file in the src folder
    xacro_file = '/ros2_ws/src/aetheris_description_pkg/xacro/prime.urdf.xacro'
    urdf_file = '/ros2_ws/src/aetheris_description_pkg/xacro/prime.urdf'

    # Convert Xacro to URDF
    os.system(f"xacro {xacro_file} -o {urdf_file}")

    # Read URDF content
    with open(urdf_file, 'r') as f:
        robot_desc = f.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen'
        )
    ])
