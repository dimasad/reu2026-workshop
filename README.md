# reu2026-workshop

Examples for the 2026 Robotics REU at WVU workshop on GitHub and related tools.
The ROS2 package has C++ and Python components, unit tests, and integration tests.

## Package Contents

### Directory Structure
```
src/my_cpp_pkg/                       # ROS2 C++ Package  
├── CMakeLists.txt                    # Build configuration
├── package.xml                       # ROS2 package manifest
├── include/my_cpp_pkg/
│   └── add_numbers.hpp              # C++ header
├── src/
│   ├── talker.cpp                   # ROS2 talker node (C++)
│   └── add_numbers.cpp              # C++ module implementation
└── test/
    ├── test_add_numbers.cpp         # C++ unit tests (gtest)
    └── test_talker_integration.py   # Integration tests (launch_testing)

src/my_python_pkg/                   # ROS2 Python Package  
├── setup.cfg                        # Python package metadata
├── setup.py                         # Python package configuration
├── package.xml                      # ROS2 package manifest
├── my_python_pkg/
│   ├── __init__.py                  # Python package init
│   └── prod_numbers.py              # Python module
└── test/
    └── test_prod_numbers.py         # Python unit tests (pytest)
```

## Components

### 1. C++ Talker Node
- **File**: `src/talker.cpp`
- **Description**: ROS2 node that publishes "Hello World" messages
- **Topic**: `/chatter`
- **Message Type**: `std_msgs/msg/String`
- **Reference**: Based on `demo_nodes_cpp/talker` pattern

### 2. C++ Module: add_numbers
- **Header**: `include/my_cpp_pkg/add_numbers.hpp`
- **Implementation**: `src/add_numbers.cpp`
- **Function**: `int add_numbers(int a, int b)` - Returns the sum of two integers
- **Tests**: `test/test_add_numbers.cpp`
  - Uses Google Test (gtest)
  - 4 test cases covering positive, negative, mixed, and zero values

### 3. Python Module: prod_numbers
- **File**: `my_python_pkg/prod_numbers.py`
- **Function**: `prod_numbers(a, b)` - Returns the product of two numbers
- **Tests**: `test/test_prod_numbers.py`
  - Uses pytest
  - 4 test cases covering positive, negative, mixed, and zero values

### 4. ROS2 Launch and Integration Tests
- **Integration Test**: `test/test_talker_integration.py`
  - Uses `launch_testing` framework
  - Launches talker node
  - Verifies messages are published to `/chatter` topic
  - Validates "Hello World" content

## Building and Testing

### In a ROS2 Environment
```bash
# Build the package
colcon build

# Run all tests
colcon test

# View test results
colcon test-result --all --verbose
```
