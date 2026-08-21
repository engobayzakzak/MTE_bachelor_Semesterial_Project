import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix
import random

class DummyGPS(Node):
    def __init__(self):
        super().__init__('dummy_gps')
        self.pub = self.create_publisher(NavSatFix, 'gps/fix', 10)
        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = NavSatFix()
        msg.latitude = 52.0 + random.uniform(-0.0001, 0.0001)
        msg.longitude = 13.0 + random.uniform(-0.0001, 0.0001)
        msg.altitude = 100.0 + random.uniform(-1.0, 1.0)
        self.pub.publish(msg)
        self.get_logger().info("Published dummy GPS fix")

def main(args=None):
    rclpy.init(args=args)
    node = DummyGPS()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
