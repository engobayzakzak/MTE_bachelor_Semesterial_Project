# /ros2_ws/src/aetheris_description_pkg/launch/ekf_launch.py
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    pkg_share = get_package_share_directory('aetheris_description_pkg')
    ekf_params = os.path.join(pkg_share, 'config', 'ekf.yaml')

    ekf_node = Node(
        package='robot_localization',
        executable='ekf_node',
        name='ekf_node',
        output='screen',
        parameters=[ekf_params]
    )

    return LaunchDescription([
        ekf_node
    ])
