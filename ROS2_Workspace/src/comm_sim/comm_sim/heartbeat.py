#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from rclpy.qos import QoSProfile, ReliabilityPolicy

class HeartbeatPub(Node):
    def __init__(self):
        super().__init__('agent_heartbeat')
        q = QoSProfile(depth=10)
        q.reliability = ReliabilityPolicy.BEST_EFFORT
        self.pub = self.create_publisher(String, '/agent/heartbeat', q)
        self.timer = self.create_timer(0.2, self.timer_cb)  # 5 Hz

    def timer_cb(self):
        m = String()
        m.data = f"agent1 alive {self.get_clock().now().to_msg().sec}"
        self.pub.publish(m)

def main(args=None):
    rclpy.init(args=args)
    node = HeartbeatPub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
