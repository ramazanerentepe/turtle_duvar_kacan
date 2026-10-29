import math
import random
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class DuvarKacan(Node):
    def __init__(self):
        super().__init__('duvar_kacan')

        self.declare_parameter('hiz', 2.0)
        self.declare_parameter('min_sinir' , 1.0)
        self.declare_parameter('max_sinir' , 10.0)

        self.pose = None
        self.hedef = None

        self.sub = self.create_subscription(Pose , '/turtle1/pose' , self.pose_cb , 10)
        self.pub = self.create_publisher(Twist , '/turtle1/cmd_vel' , 10)
        self.create_timer(0.1 ,self.kontrol)
        self.create_timer(1.0 , self.log)

    def pose_cb(self , msg):
        self.pose = msg
    
    def kontrol(self):
        if self.pose == None :
            return
        hiz = self.get_parameter('hiz').value
        mn = self.get_parameter('min_sinir').value
        mx = self.get_parameter('max_sinir').value
        x , y , th = self.pose.x , self.pose.y , self.pose.theta

        cmd = Twist()
        if mn <= x <= mx and mn <= y <= mx:
            self.hedef = None
            cmd.linear.x = hiz
        else:
            if self.hedef is None:
                self.hedef = (random.uniform(3 ,8) , random.uniform(3 , 8))
            aci = math.atan2(self.hedef[1]- y , self.hedef[0] - x )
            fark = math.atan2(math.sin(aci - th), math.cos(aci - th))
            if abs(fark) > 0.1 :
                cmd.angular.z = 2.0 if fark > 0 else -2.0
            else:
                cmd.linear.x = hiz

        self.pub.publish(cmd)

    def log(self):
        if self.pose:
            self.get_logger().info(f'x: {self.pose.x:.2f} y: {self.pose.y:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = DuvarKacan()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
