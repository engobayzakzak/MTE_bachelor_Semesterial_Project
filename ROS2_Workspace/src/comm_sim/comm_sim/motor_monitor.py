import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray

class MotorMonitor(Node):
    def __init__(self):
        super().__init__('motor_monitor')
        self.subscription = self.create_subscription(Float32MultiArray, '/motor_speeds', self.callback, 10)
        self.threshold = 1000.0  # RPM deviation threshold

    def callback(self, msg):
        avg_speed = sum(msg.data) / len(msg.data)
        for i, speed in enumerate(msg.data):
            if abs(speed - avg_speed) > self.threshold:
                self.get_logger().warn(f'⚠️ Possible actuator fault — Motor {i+1} deviates by >{self.threshold} RPM')

def main(args=None):
    rclpy.init(args=args)
    node = MotorMonitor()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
