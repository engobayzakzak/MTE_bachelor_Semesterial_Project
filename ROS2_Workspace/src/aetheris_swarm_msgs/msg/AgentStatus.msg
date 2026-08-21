# Unique ID of the reporting agent
string agent_id

# Current position (ENU frame)
geometry_msgs/Point current_position

# Current orientation
geometry_msgs/Quaternion current_orientation

# Battery percentage [0.0 - 100.0]
float32 battery_level

# Current operational mode
string mode
