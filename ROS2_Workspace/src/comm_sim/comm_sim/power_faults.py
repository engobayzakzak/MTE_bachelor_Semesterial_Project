#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random
import time

class PowerFault(Node):
    def __init__(self):
        super().__init__('power_fault')
        self.pub = self.create_publisher(Float32, 'battery/voltage', 10)
        self.timer = self.create_timer(0.5, self.timer_callback)
        self.nominal_voltage = 44.4 # Example: 4S LiPo battery (4.2V * 4)
        self.fault_state = None
        self.get_logger().info("Power fault simulator initialized. Nominal voltage = 44.4V")

    def timer_callback(self):
        voltage = self.nominal_voltage

        # Randomly simulate voltage sag or noise
        if random.random() < 0.05:  # 5% chance per cycle to trigger a fault
            self.fault_state = random.choice(['sag', 'imbalance', 'noise'])
            self.get_logger().warn(f"⚠️ Power fault injected: {self.fault_state.upper()}")

        # Simulate the effect of each fault type
        if self.fault_state == 'sag':
            voltage *= random.uniform(0.7, 0.9)
        elif self.fault_state == 'imbalance':
            voltage -= random.uniform(0.5, 1.0)
        elif self.fault_state == 'noise':
            voltage += random.uniform(-0.2, 0.2)

        # Publish voltage value
        msg = Float32()
        msg.data = voltage
        self.pub.publish(msg)
        self.get_logger().info(f"Voltage reading: {msg.data:.2f}V")

        # Randomly recover
        if self.fault_state and random.random() < 0.1:
            self.get_logger().info("✅ Power fault cleared, voltage normalized.")
            self.fault_state = None

def main(args=None):
    rclpy.init(args=args)
    node = PowerFault()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
