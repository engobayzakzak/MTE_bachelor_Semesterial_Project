import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from datetime import datetime, timedelta

class SentinelReceiver(Node):
    def __init__(self):
        super().__init__('sentinel_receiver')

        self.subscription = self.create_subscription(
            String,
            '/telemetry',
            self.listener_callback,
            10
        )

        self.last_msg_time = datetime.now()
        self.timeout = timedelta(seconds=5)

        # Check every second if a message is missing
        self.timer = self.create_timer(1.0, self.watchdog_check)

        self.get_logger().info('SentinelReceiver initialized and monitoring communication...')

    def listener_callback(self, msg):
        self.last_msg_time = datetime.now()
        self.get_logger().info(f'Received: "{msg.data}"')

    def watchdog_check(self):
        now = datetime.now()
        if now - self.last_msg_time > self.timeout:
            self.get_logger().warn('⚠️ Communication fault detected — no message from Prime for >5s')

def main(args=None):
    rclpy.init(args=args)
    node = SentinelReceiver()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

