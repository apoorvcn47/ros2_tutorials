from launch import LaunchDescription
# from launch.substitutions import EnvironmentVariable
# import os
import launch_ros.actions
import pathlib

# To include launch files
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
# from launch.substitutions import ThisLaunchFileDir
 
def generate_launch_description():
    package_path = str(pathlib.Path(__file__).parents[1]) # get current path and go one level up
    parameters_file_path = package_path + '/params/' + 'params.yaml'
    print(parameters_file_path)

    return LaunchDescription([  
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([package_path + '/launch/', 'rviz.launch.py'])),
             

        launch_ros.actions.Node(
            # the name of the executable is set in CMakeLists.txt, towards the end of
            # the file, in add_executable(...) and the directives following it
            package='cpp_pubsub2', 
            node_executable='talker2', 
            node_name='talkerA', 
            remappings=[('/chatter', '/blahblah')],
            parameters=[parameters_file_path],
            output='screen'),

        launch_ros.actions.Node(
            # the name of the executable is set in CMakeLists.txt, towards the end of
            # the file, in add_executable(...) and the directives following it
            package='cpp_pubsub2', 
            node_executable='listener', 
            node_name='listener', 
            remappings=[('/chatter', '/blahblah')],
            parameters=[parameters_file_path],
            output='screen'),
    ])