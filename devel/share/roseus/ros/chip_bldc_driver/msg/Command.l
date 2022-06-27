;; Auto-generated. Do not edit!


(when (boundp 'chip_bldc_driver::Command)
  (if (not (find-package "CHIP_BLDC_DRIVER"))
    (make-package "CHIP_BLDC_DRIVER"))
  (shadow 'Command (find-package "CHIP_BLDC_DRIVER")))
(unless (find-package "CHIP_BLDC_DRIVER::COMMAND")
  (make-package "CHIP_BLDC_DRIVER::COMMAND"))

(in-package "ROS")
;;//! \htmlinclude Command.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass chip_bldc_driver::Command
  :super ros::object
  :slots (_header _motor_command ))

(defmethod chip_bldc_driver::Command
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:motor_command __motor_command) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _motor_command (round __motor_command))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:motor_command
   (&optional __motor_command)
   (if __motor_command (setq _motor_command __motor_command)) _motor_command)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int16 _motor_command
    2
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int16 _motor_command
       (write-word _motor_command s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int16 _motor_command
     (setq _motor_command (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;;
   self)
  )

(setf (get chip_bldc_driver::Command :md5sum-) "0ea5656f56e42b2757331b0a7720a566")
(setf (get chip_bldc_driver::Command :datatype-) "chip_bldc_driver/Command")
(setf (get chip_bldc_driver::Command :definition-)
      "# Set Motor Command between -1000 and 1000
Header header
int16 motor_command
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

")



(provide :chip_bldc_driver/Command "0ea5656f56e42b2757331b0a7720a566")


