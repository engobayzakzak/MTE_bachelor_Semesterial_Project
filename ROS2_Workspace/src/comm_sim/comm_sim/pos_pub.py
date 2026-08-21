#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseStamped
from rclpy.qos import QoSProfile, ReliabilityPolicy
import math

class PosePub(Node):
    def __init__(self):
        super().__init__('agent_pose')
        q = QoSProfile(depth=10)
        q.reliability = ReliabilityPolicy.RELIABLE
        self.pub = self.create_publisher(PoseStamped, '/agent/pose', q)
        self.t = 0.0
        self.timer = self.create_timer(0.05, self.timer_cb)  # 20 Hz

    def timer_cb(self):
        ps = PoseStamped()
        ps.header.stamp = self.get_clock().now().to_msg()
        ps.header.frame_id = 'map'
        ps.pose.position.x = math.cos(self.t) * 10.0
        ps.pose.position.y = math.sin(self.t) * 10.0
        ps.pose.position.z = 100.0
        self.pub.publish(ps)
        self.t += 0.05

def main(args=None):
    rclpy.init(args=args)
    node = PosePub()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
