#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from rosflight_msgs.msg import GPS
from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024, 768)


def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.latitude)
    camera.capture('%s.jpg'%(data.latitude))

def listener():

    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("/gps", GPS, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()