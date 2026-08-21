#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros
class SentinelTFPublisher(Node):
 def __init__(self):
 super().__init__('sentinel_tf_publisher')
 self.broadcaster = tf2_ros.StaticTransformBroadcaster(self)
 # List of Sentinel sensors: (child_frame, parent_frame, x, y, z)
 sensors = [
 ("1O_JSN-SR04T", "base_link", 0.09076, 0.06048, 0.00057),
 ("3O_JSN-SR04T", "base_link", -0.00458, 0.11737, 0.00057),
 ("5O_JSN-SR04T", "base_link", -0.10021, 0.06469, 0.00057),
 ("7O_JSN-SR04T", "base_link", -0.1042, -0.04492, 0.00057),
 ("9O_JSN-SR04T", "base_link", 0.00761, -0.10153, 0.00057),
 ("11O_JSN-SR04T", "base_link", 0.08803, -0.0494, 0.00057),
 ("LiDAR", "base_link", 0.09392, -0.00418, 0.0),
 ("RGB_Camera", "base_link", 0.09464, 0.01198, -0.0045),
 ("Telemetry_module", "base_link", 0.0, -0.06195, 0.0),
 ("Antenna", "base_link", -0.01515, 0.09384, -0.01133),
 ("Thermal_camera", "base_link", 0.09392, -0.00418, -0.0091),
 ("Front_holding_plate", "base_link", 0.09392, -0.00418, 0.0),
 ("Linear_actuator", "base_link", 0.0, 0.01575, -0.03534),
 ("Gripper", "actuator_link", 0.0, 0.0, -0.00223)
 ]
 # Publish each sensor as a static transform
 for child_frame, parent_frame, x, y, z in sensors:
 t = TransformStamped()
 t.header.stamp = self.get_clock().now().to_msg()
 t.header.frame_id = parent_frame
 t.child_frame_id = child_frame
 t.transform.translation.x = x
 t.transform.translation.y = y
 t.transform.translation.z = z
 # No rotation (quaternion)
 t.transform.rotation.x = 0.0
 t.transform.rotation.y = 0.0
 t.transform.rotation.z = 0.0
 t.transform.rotation.w = 1.0
 self.broadcaster.sendTransform(t)
 self.get_logger().info(f"Published {parent_frame} -> {child_frame}")
def main(args=None):
 rclpy.init(args=args)
 node = SentinelTFPublisher()
 rclpy.spin(node)
 node.destroy_node()
 rclpy.shutdown()
if __name__ == '__main__':
 main()
