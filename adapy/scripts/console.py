#!/usr/bin/env python
"""
Provides a simple console that sets up basic functionality for 
using AdaPy and openravepy.
"""

import IPython
import adapy
import argparse
import logging
import numpy
import openravepy
import rospy

if __name__ == "__main__":
    rospy.init_node('adapy', anonymous=True)

    env, robot = adapy.initialize(
        sim=False,
        attach_viewer='rviz'
	)

    IPython.embed()
