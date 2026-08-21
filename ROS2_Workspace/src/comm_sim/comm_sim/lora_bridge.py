#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from collections import deque
import copy, random
from rclpy.qos import QoSProfile, ReliabilityPolicy
from std_msgs.msg import String
from geometry_msgs.msg import PoseStamped

class LoRaBridge(Node):
    def __init__(self):
        super().__init__('lora_bridge')

        self.declare_parameter('input_topic', '/agent/heartbeat')
        self.declare_parameter('output_topic', '/prime/heartbeats')
        self.declare_parameter('publish_rate', 1.0)
        self.declare_parameter('loss_rate', 0.05)
        self.declare_parameter('queue_size', 100)

        itopic = self.get_parameter('input_topic').get_parameter_value().string_value
        otopic = self.get_parameter('output_topic').get_parameter_value().string_value
        rate = self.get_parameter('publish_rate').get_parameter_value().double_value
        self.loss_rate = self.get_parameter('loss_rate').get_parameter_value().double_value
        qsize = self.get_parameter('queue_size').get_parameter_value().integer_value

        qos_in = QoSProfile(depth=10)
        qos_in.reliability = ReliabilityPolicy.RELIABLE
        qos_out = QoSProfile(depth=5)
        qos_out.reliability = ReliabilityPolicy.BEST_EFFORT

        if itopic.endswith('pose') or 'pose' in itopic:
            self.sub_type = PoseStamped
        else:
            self.sub_type = String

        self.sub = self.create_subscription(self.sub_type, itopic, self._cb, qos_in)
        self.pub = self.create_publisher(self.sub_type, otopic, qos_out)

        self.queue = deque(maxlen=qsize)
        self.timer = self.create_timer(1.0/max(1e-6, rate), self._timer_cb)

        self.get_logger().info(f'LoRaBridge: {itopic} -> {otopic} at {rate}Hz loss={self.loss_rate}')

    def _cb(self, msg):
        self.queue.append(copy.deepcopy(msg))

    def _timer_cb(self):
        if not self.queue:
            return
        msg = self.queue.popleft()
        if random.random() < self.loss_rate:
            self.get_logger().debug('dropped message (simulated loss)')
            return
        self.pub.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = LoRaBridge()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
