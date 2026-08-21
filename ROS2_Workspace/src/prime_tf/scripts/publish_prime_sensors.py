#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import TransformStamped
import tf2_ros
class PrimeTFPublisher(Node):
 def __init__(self):
 super().__init__('prime_tf_publisher')
 self.broadcaster = tf2_ros.StaticTransformBroadcaster(self)
 # List of Prime sensors: (child_frame, parent_frame, x, y, z)
 sensors = [
 ("Gimbal_camera", "gimbal_link", 2.61136, 0.00004, -0.71337),
 ("Gimbal_base", "base_link", 2.59761, -0.00001, -0.45744),
 ("LiDAR", "base_link", -0.13862, -0.00176, -0.1943),
 ("GNSS_module", "base_link", 0.38207, 0.0, 0.6371),
 ("Hyperspectural_sensor", "base_link", -1.11855, -0.11134, -0.1863),
 ("Propeller", "base_link", -3.91319, 0.0, 0.03031)
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
 node = PrimeTFPublisher()
 rclpy.spin(node)
 node.destroy_node()
 rclpy.shutdown()
if __name__ == '__main__':
 main()
