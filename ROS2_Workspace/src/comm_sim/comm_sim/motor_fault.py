#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random
import time

class MotorFault(Node):
    def __init__(self):
        super().__init__('motor_fault')
        self.pub = self.create_publisher(Float32, 'motor/thrust', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.nominal_thrust = 1.0
        self.fault_injected = False
        self.get_logger().info("Motor fault simulator initialized. Nominal thrust = 1.0")

    def timer_callback(self):
        # Simulate random fault
        if not self.fault_injected and random.random() < 0.1:
            self.get_logger().warn("⚠️ Injecting thrust fault!")
            self.nominal_thrust *= random.uniform(0.4, 0.7)
            self.fault_injected = True
        msg = Float32()
        msg.data = self.nominal_thrust
        self.pub.publish(msg)
        self.get_logger().info(f"Publishing thrust value: {msg.data:.2f}")
        # Reset after some time
        if self.fault_injected and random.random() < 0.05:
            self.get_logger().info("✅ Fault cleared, restoring nominal thrust.")
            self.nominal_thrust = 1.0
            self.fault_injected = False

def main(args=None):
    rclpy.init(args=args)
    node = MotorFault()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

