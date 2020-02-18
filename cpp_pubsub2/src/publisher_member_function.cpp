#include <iostream>
#include <memory>

#include "rclcpp/rclcpp.hpp"

#include "std_msgs/msg/string.hpp"

int main(int argc, char * argv[])
{
  rclcpp::init(argc, argv);

  // rclcpp::NodeOptions node_options;
  // node_options.allow_undeclared_parameters(true);
  // node_options.initial_parameters(initial_parameters);
  auto node = rclcpp::Node::make_shared("talker2");
  // rclcpp::NodeOptions node_options;
  // node_options.allow_undeclared_parameters(true);
  // node_options.automatically_declare_parameters_from_overrides();
  // node->declare_parameter("xyz");
  // node->declare_parameter("items");

  rmw_qos_profile_t custom_qos_profile = rmw_qos_profile_default;
  custom_qos_profile.depth = 7;

  auto chatter_pub = node->create_publisher<std_msgs::msg::String>("chatter", custom_qos_profile);

  rclcpp::WallRate loop_rate(2);

  auto msg = std::make_shared<std_msgs::msg::String>();
  auto i = 1;

  while (rclcpp::ok()) {
    msg->data = "Hello World: " + std::to_string(i++);
    // std::cout << "Publishing: '" << msg->data << "'" << std::endl;
    chatter_pub->publish(msg);
    rclcpp::spin_some(node);
    loop_rate.sleep();
  }

  return 0;
}