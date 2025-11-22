#!/usr/bin/env python3
#并非注释，是shebang
import rclpy
from rclpy.node import Node
import random
import subprocess

class BackgroundChanger(Node):
    def __init__(self):
        super().__init__('color_change_node')
        
        # 声明参数
        self.declare_parameter('background_r', 69)
        self.declare_parameter('background_g', 86)
        self.declare_parameter('background_b', 255)
        
        self.get_logger().info('Background color changer started')
        self.timer = self.create_timer(2.0, self.change_background)  # 每2秒执行一次
    
    def change_background(self):
        # 生成随机 RGB 颜色值
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        
        self.get_logger().info(f'Changing background to RGB({r}, {g}, {b})')
        
        # 方法1：使用 subprocess 调用 ros2 param set 命令
        try:
            subprocess.run(['ros2', 'param', 'set', '/t1/tur1', 'background_r', str(r)], 
                         check=True, capture_output=True)
            subprocess.run(['ros2', 'param', 'set', '/t1/tur1', 'background_g', str(g)], 
                         check=True, capture_output=True)
            subprocess.run(['ros2', 'param', 'set', '/t1/tur1', 'background_b', str(b)], 
                         check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            self.get_logger().warn(f'Failed to set background color: {e}')

def main():
    rclpy.init()
    node = BackgroundChanger()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()