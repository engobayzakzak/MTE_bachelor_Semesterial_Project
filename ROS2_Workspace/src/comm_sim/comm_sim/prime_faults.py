import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import time

class PrimeFaults(Node):
    def __init__(self):
        super().__init__('prime_faults')
        self.sub = self.create_subscription(String, 'sentinel_status', self.callback, 10)
        self.last_msg_time = self.get_clock().now().seconds_nanoseconds()[0]
        self.create_timer(1.0, self.check_timeout)

    def callback(self, msg):
        self.last_msg_time = self.get_clock().now().seconds_nanoseconds()[0]
        if "ERROR" in msg.data:
            self.get_logger().warn(f"⚠️ Corrupted data detected: {msg.data}")

    def check_timeout(self):
        now = self.get_clock().now().seconds_nanoseconds()[0]
        if now - self.last_msg_time > 5:
            self.get_logger().error("❌ Sentinel node unresponsive (timeout > 5s).")
        else:
            self.get_logger().info("✅ Sentinel link healthy.")

def main(args=None):
    rclpy.init(args=args)
    node = PrimeFaults()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
