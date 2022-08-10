;; Auto-generated. Do not edit!


(when (boundp 'robot::SentMessage)
  (if (not (find-package "ROBOT"))
    (make-package "ROBOT"))
  (shadow 'SentMessage (find-package "ROBOT")))
(unless (find-package "ROBOT::SENTMESSAGE")
  (make-package "ROBOT::SENTMESSAGE"))

(in-package "ROS")
;;//! \htmlinclude SentMessage.msg.html


(defclass robot::SentMessage
  :super ros::object
  :slots (_sender _content ))

(defmethod robot::SentMessage
  (:init
   (&key
    ((:sender __sender) "")
    ((:content __content) "")
    )
   (send-super :init)
   (setq _sender (string __sender))
   (setq _content (string __content))
   self)
  (:sender
   (&optional __sender)
   (if __sender (setq _sender __sender)) _sender)
  (:content
   (&optional __content)
   (if __content (setq _content __content)) _content)
  (:serialization-length
   ()
   (+
    ;; string _sender
    4 (length _sender)
    ;; string _content
    4 (length _content)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _sender
       (write-long (length _sender) s) (princ _sender s)
     ;; string _content
       (write-long (length _content) s) (princ _content s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _sender
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _sender (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _content
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _content (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get robot::SentMessage :md5sum-) "b2e1a1fbf660d36f0c4ce4c3ed50a434")
(setf (get robot::SentMessage :datatype-) "robot/SentMessage")
(setf (get robot::SentMessage :definition-)
      "string sender
string content

")



(provide :robot/SentMessage "b2e1a1fbf660d36f0c4ce4c3ed50a434")


