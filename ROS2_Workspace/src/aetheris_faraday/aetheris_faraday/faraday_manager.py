import rclpy
from rclpy.node import Node

class FaradayManager(Node):
    def __init__(self):
        super().__init__('faraday_manager')
        self.get_logger().info("✅ Faraday Manager Node has started.")

def main(args=None):
    rclpy.init(args=args)
    node = FaradayManager()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
