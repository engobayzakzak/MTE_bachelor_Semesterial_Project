import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class PrimeTransmitter(Node):
    def __init__(self):
        super().__init__('prime_transmitter')
        self.publisher_ = self.create_publisher(String, '/telemetry', 10)
        self.timer = self.create_timer(1.0, self.publish_message)

    def publish_message(self):
        msg = String()
        msg.data = 'Telemetry OK'
        self.publisher_.publish(msg)
        self.get_logger().info('Published: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    node = PrimeTransmitter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
