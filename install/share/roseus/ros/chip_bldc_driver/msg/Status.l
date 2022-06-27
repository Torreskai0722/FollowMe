;; Auto-generated. Do not edit!


(when (boundp 'chip_bldc_driver::Status)
  (if (not (find-package "CHIP_BLDC_DRIVER"))
    (make-package "CHIP_BLDC_DRIVER"))
  (shadow 'Status (find-package "CHIP_BLDC_DRIVER")))
(unless (find-package "CHIP_BLDC_DRIVER::STATUS")
  (make-package "CHIP_BLDC_DRIVER::STATUS"))

(in-package "ROS")
;;//! \htmlinclude Status.msg.html
(if (not (find-package "STD_MSGS"))
  (ros::roseus-add-msgs "std_msgs"))


(defclass chip_bldc_driver::Status
  :super ros::object
  :slots (_header _motor_operational_status _battery_voltage _mcu_temperature _motor_command _motor_pid_error ))

(defmethod chip_bldc_driver::Status
  (:init
   (&key
    ((:header __header) (instance std_msgs::Header :init))
    ((:motor_operational_status __motor_operational_status) 0)
    ((:battery_voltage __battery_voltage) 0.0)
    ((:mcu_temperature __mcu_temperature) 0)
    ((:motor_command __motor_command) 0)
    ((:motor_pid_error __motor_pid_error) 0)
    )
   (send-super :init)
   (setq _header __header)
   (setq _motor_operational_status (round __motor_operational_status))
   (setq _battery_voltage (float __battery_voltage))
   (setq _mcu_temperature (round __mcu_temperature))
   (setq _motor_command (round __motor_command))
   (setq _motor_pid_error (round __motor_pid_error))
   self)
  (:header
   (&rest __header)
   (if (keywordp (car __header))
       (send* _header __header)
     (progn
       (if __header (setq _header (car __header)))
       _header)))
  (:motor_operational_status
   (&optional __motor_operational_status)
   (if __motor_operational_status (setq _motor_operational_status __motor_operational_status)) _motor_operational_status)
  (:battery_voltage
   (&optional __battery_voltage)
   (if __battery_voltage (setq _battery_voltage __battery_voltage)) _battery_voltage)
  (:mcu_temperature
   (&optional __mcu_temperature)
   (if __mcu_temperature (setq _mcu_temperature __mcu_temperature)) _mcu_temperature)
  (:motor_command
   (&optional __motor_command)
   (if __motor_command (setq _motor_command __motor_command)) _motor_command)
  (:motor_pid_error
   (&optional __motor_pid_error)
   (if __motor_pid_error (setq _motor_pid_error __motor_pid_error)) _motor_pid_error)
  (:serialization-length
   ()
   (+
    ;; std_msgs/Header _header
    (send _header :serialization-length)
    ;; int16 _motor_operational_status
    2
    ;; float32 _battery_voltage
    4
    ;; int16 _mcu_temperature
    2
    ;; int16 _motor_command
    2
    ;; int32 _motor_pid_error
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; std_msgs/Header _header
       (send _header :serialize s)
     ;; int16 _motor_operational_status
       (write-word _motor_operational_status s)
     ;; float32 _battery_voltage
       (sys::poke _battery_voltage (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; int16 _mcu_temperature
       (write-word _mcu_temperature s)
     ;; int16 _motor_command
       (write-word _motor_command s)
     ;; int32 _motor_pid_error
       (write-long _motor_pid_error s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; std_msgs/Header _header
     (send _header :deserialize buf ptr-) (incf ptr- (send _header :serialization-length))
   ;; int16 _motor_operational_status
     (setq _motor_operational_status (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; float32 _battery_voltage
     (setq _battery_voltage (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; int16 _mcu_temperature
     (setq _mcu_temperature (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int16 _motor_command
     (setq _motor_command (sys::peek buf ptr- :short)) (incf ptr- 2)
   ;; int32 _motor_pid_error
     (setq _motor_pid_error (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get chip_bldc_driver::Status :md5sum-) "10df97be388ae1578fee4bc1bad6eaac")
(setf (get chip_bldc_driver::Status :datatype-) "chip_bldc_driver/Status")
(setf (get chip_bldc_driver::Status :definition-)
      "# 5Hz status message
Header header

int16 motor_operational_status
float32 battery_voltage
int16 mcu_temperature
int16 motor_command
int32 motor_pid_error
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



(provide :chip_bldc_driver/Status "10df97be388ae1578fee4bc1bad6eaac")


