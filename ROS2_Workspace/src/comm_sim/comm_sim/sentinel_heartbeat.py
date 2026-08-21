import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SentinelHeartbeat(Node):
    def __init__(self):
        super().__init__('sentinel_heartbeat')
        self.pub = self.create_publisher(String, 'sentinel_status', 10)
        self.create_timer(1.0, self.publish_heartbeat)

    def publish_heartbeat(self):
        msg = String()
        msg.data = "Sentinel alive"
        self.pub.publish(msg)
        self.get_logger().info("📡 Heartbeat sent.")

def main(args=None):
    rclpy.init(args=args)
    node = SentinelHeartbeat()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
