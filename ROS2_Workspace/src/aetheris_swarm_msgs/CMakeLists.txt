cmake_minimum_required(VERSION 3.8)
project(aetheris_swarm_msgs)

#COMMENTED||if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
#COMMENTED||  add_compile_options(-Wall -Wextra -Wpedantic)
#COMMENTED||endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

#COMMENTED||if(BUILD_TESTING)
#COMMENTED||  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
#COMMENTED||  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
#COMMENTED||  set(ament_cmake_cpplint_FOUND TRUE)
#COMMENTED||  ament_lint_auto_find_test_dependencies()
#COMMENTED||endif()

#COMMENTED||ament_package()
find_package(geometry_msgs REQUIRED)

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/AgentCommand.msg"
  "msg/AgentStatus.msg"
  "msg/SwarmState.msg"
  DEPENDENCIES geometry_msgs
)

ament_package()
#COMMENTED||ament_export_dependencies(rosidl_default_runtime)
