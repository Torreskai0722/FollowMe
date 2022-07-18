#!/usr/bin/env python3
import rospy
import threading
from chip_bldc_driver.msg import Command
from geometry_msgs.msg import Twist

class DonkeyController:

    def __init__(self, rate):

        rospy.init_node('Donkey_controller')

        rospy.Subscriber("cmd_vel", Twist, self.set_objective_controller_command)

        self.rate = rospy.Rate(rate)

        self.front_left = rospy.Publisher('/motor_driver_1/Command', Command, queue_size=10)
        self.back_right = rospy.Publisher('/motor_driver_2/Command', Command, queue_size=10)
        self.back_left = rospy.Publisher('/motor_driver_3/Command', Command, queue_size=10)
        self.front_right = rospy.Publisher('/motor_driver_0/Command', Command, queue_size=10)

        rospy.Subscriber("/motor_driver_2/feedback", Feedback, self.update_br_feedback)
        rospy.Subscriber("/motor_driver_1/feedback", Feedback, self.update_fl_feedback)
        rospy.Subscriber("/motor_driver_0/feedback", Feedback, self.update_fr_feedback)
        rospy.Subscriber("/motor_driver_3/feedback", Feedback, self.update_bl_feedback)

        self.lxAddly = 0.4
        self.scale = 30 / 3.1415926 / 0.076

        while not rospy.is_shutdown():
            self.publish_controller_command()
            self.rate.sleep()

    def set_objective_controller_command(self, msg):

        spd = msg.linear.x
        steering = msg.angular.z

        self.obj_fl = int((spd - (self.lxAddly) * steering) * self.scale) // 4
        self.obj_fr = int((spd + (self.lxAddly) * steering) * self.scale) // 4
        self.obj_bl = int((spd - (self.lxAddly) * steering) * self.scale) // 4 
        self.obj_br = int((spd + (self.lxAddly) * steering) * self.scale) // 4


    def publish_controller_command(self):

        fl = self.obj_fl
        fr = self.obj_fr
        bl = self.obj_bl
        br = self.obj_br

        print(f"front_left : {fl}, back_right : {fr}, back_left : {bl}, front_right : {br}")

        commandFL = Command()
        commandFR = Command()
        commandBL = Command()
        commandBR = Command()

        commandFL.motor_command = fl * -1 if abs(fl) >= 8 else 0
        commandBR.motor_command = br if abs(br) >= 8 else 0
        commandBL.motor_command = bl * -1 if abs(bl) >= 8 else 0
        commandFR.motor_command = fr if abs(fr) >= 8 else 0
        
        print(f"front_left : {commandFL.motor_command}, back_right : {commandFR.motor_command}, back_left : {commandBL.motor_command}, front_right : {commandFR.motor_command}")

        commandFL.header.stamp = rospy.Time.now()
        commandBR.header.stamp = rospy.Time.now()
        commandBL.header.stamp = rospy.Time.now()
        commandFR.header.stamp = rospy.Time.now()

        self.front_left.publish(commandFL)
        self.back_right.publish(commandBR)
        self.back_left.publish(commandBL)
        self.front_right.publish(commandFR)

    def update_br_command(self, msg):
        #print(msg.header.stamp.secs, self.start_time.secs, msg.header.stamp.nsecs,  msg.header.stamp.nsecs // 10 ** 8)
        ind = (msg.header.stamp.secs - self.start_time.secs) * 10 + (msg.header.stamp.nsecs // 10 ** 8)
        self.data.add('back_right_command', msg.motor_command * self.command_ratio, ind)

    def update_fl_command(self, msg):
        ind = (msg.header.stamp.secs - self.start_time.secs) * 10 + (msg.header.stamp.nsecs // 10 ** 8)
        self.data.add('front_left_command', msg.motor_command * self.command_ratio, ind)

    def update_fr_command(self, msg):
            
        ind = (msg.header.stamp.secs - self.start_time.secs) * 10 + (msg.header.stamp.nsecs // 10 ** 8)
        self.data.add('front_right_command', msg.motor_command * self.command_ratio, ind)

    def update_bl_command(self, msg):

        ind = (msg.header.stamp.secs- self.start_time.secs) * 10 + (msg.header.stamp.nsecs // 10 ** 8)
        self.data.add('back_left_command', msg.motor_command * self.command_ratio, ind)

def main():

    controller = DonkeyController()

if __name__ == '__main__':
    main()


    
