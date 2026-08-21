import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
import random
import math

class DummyIMU(Node):
    def __init__(self):
        super().__init__('dummy_imu')
        self.pub = self.create_publisher(Imu, 'imu/data', 10)
        self.timer = self.create_timer(0.1, self.publish_data)

    def publish_data(self):
        msg = Imu()
        msg.linear_acceleration.x = random.uniform(-0.1, 0.1)
        msg.linear_acceleration.y = random.uniform(-0.1, 0.1)
        msg.linear_acceleration.z = 9.81 + random.uniform(-0.1, 0.1)
        msg.angular_velocity.z = random.uniform(-0.05, 0.05)
        self.pub.publish(msg)
        self.get_logger().info("Published dummy IMU data")

def main(args=None):
    rclpy.init(args=args)
    node = DummyIMU()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
