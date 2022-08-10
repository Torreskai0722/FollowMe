;; Auto-generated. Do not edit!


(when (boundp 'ros_autonomous_slam::PointArray)
  (if (not (find-package "ROS_AUTONOMOUS_SLAM"))
    (make-package "ROS_AUTONOMOUS_SLAM"))
  (shadow 'PointArray (find-package "ROS_AUTONOMOUS_SLAM")))
(unless (find-package "ROS_AUTONOMOUS_SLAM::POINTARRAY")
  (make-package "ROS_AUTONOMOUS_SLAM::POINTARRAY"))

(in-package "ROS")
;;//! \htmlinclude PointArray.msg.html
(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(defclass ros_autonomous_slam::PointArray
  :super ros::object
  :slots (_points ))

(defmethod ros_autonomous_slam::PointArray
  (:init
   (&key
    ((:points __points) (let (r) (dotimes (i 0) (push (instance geometry_msgs::Point :init) r)) r))
    )
   (send-super :init)
   (setq _points __points)
   self)
  (:points
   (&rest __points)
   (if (keywordp (car __points))
       (send* _points __points)
     (progn
       (if __points (setq _points (car __points)))
       _points)))
  (:serialization-length
   ()
   (+
    ;; geometry_msgs/Point[] _points
    (apply #'+ (send-all _points :serialization-length)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; geometry_msgs/Point[] _points
     (write-long (length _points) s)
     (dolist (elem _points)
       (send elem :serialize s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; geometry_msgs/Point[] _points
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _points (let (r) (dotimes (i n) (push (instance geometry_msgs::Point :init) r)) r))
     (dolist (elem- _points)
     (send elem- :deserialize buf ptr-) (incf ptr- (send elem- :serialization-length))
     ))
   ;;
   self)
  )

(setf (get ros_autonomous_slam::PointArray :md5sum-) "3fb3f9dacc279b964c4c8341122c34df")
(setf (get ros_autonomous_slam::PointArray :datatype-) "ros_autonomous_slam/PointArray")
(setf (get ros_autonomous_slam::PointArray :definition-)
      "# An array of points

geometry_msgs/Point[] points

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

")



(provide :ros_autonomous_slam/PointArray "3fb3f9dacc279b964c4c8341122c34df")


