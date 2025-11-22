from launch import LaunchDescription
from launch_ros.actions import Node
# 封装终端指令相关类--------------
# from launch.actions import ExecuteProcess
# from launch.substitutions import FindExecutable
# 参数声明与获取-----------------
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
# 文件包含相关-------------------
# from launch.actions import IncludeLaunchDescription
# from launch.launch_description_sources import PythonLaunchDescriptionSource
# 分组相关----------------------
# from launch_ros.actions import PushRosNamespace
# from launch.actions import GroupAction
# 事件相关----------------------
from launch.event_handlers import OnProcessStart, OnProcessExit
from launch.actions import ExecuteProcess, RegisterEventHandler,LogInfo,TimerAction
# 获取功能包下share目录路径-------
# from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    
    turtlesim1=Node(
        package="turtlesim",
        executable="turtlesim_node",
        name="tur1",
        namespace="t1",
        exec_name="tur1",
    )
    
    color=Node(
        package="test06_cpp",
        executable="turtlesim_color_change.py",
        name="color_change_node",
    )
    
    next=TimerAction(
        period=3.0,
        actions=[
            ExecuteProcess(
                cmd=[
            'ros2', 'service', 'call', '/t1/spawn', 'turtlesim/srv/Spawn',
            '{"x": 8.0, "y": 3.0, "theta": 0.0, "name": "tur2"}'
        ],
        output='screen'
            )    
        ],
    )
 
    node_list=[turtlesim1,next,color]
    return LaunchDescription(node_list)