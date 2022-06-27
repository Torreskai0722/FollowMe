;; Auto-generated. Do not edit!


(when (boundp 'chip_bldc_driver::Feedback)
  (if (not (find-package "CHIP_BLDC_DRIVER"))
    (make-package "CHIP_BLDC_DRIVER"))
  (shadow 'Feedback (find-package "CHIP_BLDC_DRIVER")))
(unless (find-package "CHIP_BLDC_DRIVER::FEEDBACK")
  (make-package "CHIP_BLDC_DRIVER::FEEDBACK"))

(in-package "ROS")
;;//! \htmlinclude Feedback.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass chip_bldc_driver::Feedback
  :super ros::object
  :slots (_header _feedback_counter _motor_encoder_counter _motor_rpm_feedback ))

(defmethod chip_bldc_driver::Feedback
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:feedback_counter __feedback_counter) 0)
    ((:motor_encoder_counter __motor_encoder_counter) 0)
    ((:motor_rpm_feedback __motor_rpm_feedback) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _feedback_counter (round __feedback_counter))
   (setq _motor_encoder_counter (round __motor_encoder_counter))
   (setq _motor_rpm_feedback (round __motor_rpm_feedback))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:feedback_counter
   (&optional __feedback_counter)
   (if __feedback_counter (setq _feedback_counter __feedback_counter)) _feedback_counter)
  (:motor_encoder_counter
   (&optional __motor_encoder_counter)
   (if __motor_encoder_counter (setq _motor_encoder_counter __motor_encoder_counter)) _motor_encoder_counter)
  (:motor_rpm_feedback
   (&optional __motor_rpm_feedback)
   (if __motor_rpm_feedback (setq _motor_rpm_feedback __motor_rpm_feedback)) _motor_rpm_feedback)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int32 _feedback_counter
    4
    ;; int32 _motor_encoder_counter
    4
    ;; int32 _motor_rpm_feedback
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int32 _feedback_counter
       (write-long _feedback_counter s)
     ;; int32 _motor_encoder_counter
       (write-long _motor_encoder_counter s)
     ;; int32 _motor_rpm_feedback
       (write-long _motor_rpm_feedback s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int32 _feedback_counter
     (setq _feedback_counter (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _motor_encoder_counter
     (setq _motor_encoder_counter (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;; int32 _motor_rpm_feedback
     (setq _motor_rpm_feedback (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get chip_bldc_driver::Feedback :md5sum-) "3cd2728375779c5e385ddf941da8bc30")
(setf (get chip_bldc_driver::Feedback :datatype-) "chip_bldc_driver/Feedback")
(setf (get chip_bldc_driver::Feedback :definition-)
      "# 20Hz feedback message
Header header

int32 feedback_counter
int32 motor_encoder_counter
int32 motor_rpm_feedback

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



(provide :chip_bldc_driver/Feedback "3cd2728375779c5e385ddf941da8bc30")


