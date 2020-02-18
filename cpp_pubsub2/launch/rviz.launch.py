from launch import LaunchDescription
# from launch.substitutions import EnvironmentVariable
# import os
import launch_ros.actions
import pathlib


 
def generate_launch_description():
    return LaunchDescription([  

        launch_ros.actions.Node(
            # the name of the executable is set in CMakeLists.txt, towards the end of
            # the file, in add_executable(...) and the directives following it
            package='rviz2', 
            node_executable='rviz2', 
            output='screen'),
    ])