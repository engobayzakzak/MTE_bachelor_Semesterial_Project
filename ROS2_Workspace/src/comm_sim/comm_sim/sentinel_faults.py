import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random
import time

class SentinelFaults(Node):
    def __init__(self):
        super().__init__('sentinel_faults')
        self.pub = self.create_publisher(String, 'sentinel_status', 10)
        self.create_timer(1.0, self.publish_status)

    def publish_status(self):
        # 10% chance to simulate corrupted data
        if random.random() < 0.1:
            msg = String()
            msg.data = "ERROR: corrupted packet"
        else:
            msg = String()
            msg.data = "Sentinel operational"
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = SentinelFaults()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
