from launch import LaunchDescription
from launch.substitutions import EnvironmentVariable
import os
import launch_ros.actions
import pathlib
from ament_index_python.packages import get_package_share_directory

# To include launch files
import launch.actions
import launch.launch_description_sources
 
def generate_launch_description():
    package_path = str(pathlib.Path(__file__).parents[1]) # get current path and go one level up
    # package_path = get_package_share_directory('cpp_pubsub2')
    parameters_file_path = package_path + '/params/' + 'params.yaml'
    # print(parameters_file_path)

    

    return LaunchDescription([  
        # launch.actions.IncludeLaunchDescription(
        #     launch.launch_description_sources.PythonLaunchDescriptionSource([package_path + '/launch/', 'rviz.launch.py'])),             

        
        # launch.actions.DeclareLaunchArgument(
        #     'params_file',
        #     default_value=parameters_file_path,
        #     # default_value=os.path.join(package_path, 'params', 'params.yaml'),
        #     description='Full path to the ROS2 parameters file to use for robot1 launched nodes'),

        
        
        launch_ros.actions.Node(
            package='cpp_pubsub2', 
            node_executable='talker2', 
            node_name='talkerA', 
            remappings=[('/chatter', '/blahblah')],
            parameters=[parameters_file_path],
            # parameters=[
            #     parameters_file_path,
            #     str(parameters_file_path),
            #     [EnvironmentVariable(name='FILE_PATH'), os.sep, 'params.yaml'],
            # ],
            output='screen'),

        launch_ros.actions.Node(
            package='cpp_pubsub2', 
            node_executable='listener', 
            node_name='listener', 
            remappings=[('/chatter', '/blahblah')],
            # parameters=[parameters_file_path],
            output='screen'),
    ])