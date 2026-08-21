import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class PrimeMonitor(Node):
    def __init__(self):
        super().__init__('prime_monitor')
        self.sub = self.create_subscription(String, 'sentinel_status', self.callback, 10)
        self.last_heartbeat_time = self.get_clock().now().seconds_nanoseconds()[0]
        self.create_timer(1.0, self.check_heartbeat)

    def callback(self, msg):
        self.last_heartbeat_time = self.get_clock().now().seconds_nanoseconds()[0]
        self.get_logger().info(f"✅ Received: {msg.data}")

    def check_heartbeat(self):
        now = self.get_clock().now().seconds_nanoseconds()[0]
        if now - self.last_heartbeat_time > 5:
            self.get_logger().error("❌ Sentinel not responding (no heartbeat > 5s)")
        else:
            self.get_logger().info("🟢 Link healthy")

def main(args=None):
    rclpy.init(args=args)
    node = PrimeMonitor()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
