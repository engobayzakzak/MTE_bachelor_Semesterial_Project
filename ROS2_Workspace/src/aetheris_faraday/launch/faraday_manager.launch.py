from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='aetheris_faraday',
            executable='faraday_manager',
            name='faraday_manager',
            parameters=['config/faraday_params.yaml']
        )
    ])

