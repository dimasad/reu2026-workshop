"""Integration tests for the talker node using launch_testing."""

import pytest
import unittest

from launch import LaunchDescription
from launch_ros.actions import Node
from launch_testing.actions import ReadyToTest
import launch_testing
import rclpy
from std_msgs.msg import String


@pytest.mark.launch_test
def generate_test_description():
    """Generate test launch description."""
    talker_node = Node(package="my_cpp_pkg", executable="talker", name="talker")
    return (
        LaunchDescription([talker_node, ReadyToTest()]),
        {"talker": talker_node},
    )


class TestTalkerNode(unittest.TestCase):
    """Tests for the talker node."""

    def setUp(self):
        """Set up test fixtures."""
        rclpy.init()
        self.node = rclpy.create_node("test_talker_listener")

    def tearDown(self):
        """Tear down test fixtures."""
        self.node.destroy_node()
        rclpy.shutdown()

    def test_talker_publishes_to_chatter(self, launch_service, proc_output):
        """Test that talker publishes to chatter topic."""
        # Create a subscription to the chatter topic
        messages = []

        def callback(msg):
            messages.append(msg.data)

        subscription = self.node.create_subscription(String, "chatter", callback, 10)

        # Wait for some messages
        rclpy.spin_once(self.node, timeout_sec=2.0)
        rclpy.spin_once(self.node, timeout_sec=2.0)
        rclpy.spin_once(self.node, timeout_sec=2.0)

        self.node.destroy_subscription(subscription)

        # Check that we received messages with "Hello World"
        self.assertTrue(
            any("Hello World" in msg for msg in messages),
            'Expected to receive "Hello World" message on /chatter topic',
        )
