#! /usr/bin/env python3

"""
Description : 
   
    This ros2 node publishes 'Namashkar Doston' messages to a topic

----------

Publishing Topics : 
     
    Topics having 'Namashkar Doston' messages
    type - std_msgs/String

Subscribing Topics:

    None

----------

Author :  Maithresh 
Date   :  06-02-2026

"""
import rclpy #importing ros2 client library for pyrhon
from rclpy.node import Node #importing Node class for creating nodes
from std_msgs.msg import String #importing string msg type for ros2

class minimalpublisher(Node):
      """
      creating a minimal publisher node
      """
      def __init__(self):
            """
            creating a custom node for for publishing messages
            """

            #initializing the node with name
            super().__init__('minimal_py_publisher')

            #creating a pubisher on the topic with a queue size of 10 messages
            self.publisher = self.create_publisher(String,'py_example_topic',10)

            #creating a timer with a period of 1 second to trigger publishing of message 
            timer_period = 1
            self.timer = self.create_timer(timer_period,self.timer_callback)

            #initializing a counter variable for message content
            self.i = 0

      def timer_callback(self):
            """
            callback function executed periodically by the timer
            """

            #creating a string message object
            msg = String()

            #set the message data with a counter
            msg.data = 'Namshkar Doston: %d'%self.i
            
            #publishing the msg you created above to a topic
            self.publisher.publish(msg)

            #log a message indicating the message has been published
            self.get_logger().info('Publishing: "%s"'%msg.data)

            self.i = self.i + 1


def main(args=None):
      """
     Main function to start the ros2 node
     """
      rclpy.init(args=args)

      #create an instance of the minimal publisher node
      minimal_py_publisher = minimalpublisher()

      rclpy.spin(minimal_py_publisher)

      #destroy the node explicitly
      minimal_py_publisher.destroy_node()

      #shutdown ros 2 communication
      rclpy.shutdown()


if __name__ == '__main__':
      
      main()
