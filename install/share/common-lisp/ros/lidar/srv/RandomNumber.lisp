; Auto-generated. Do not edit!


(cl:in-package lidar-srv)


;//! \htmlinclude RandomNumber-request.msg.html

(cl:defclass <RandomNumber-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass RandomNumber-request (<RandomNumber-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RandomNumber-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RandomNumber-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lidar-srv:<RandomNumber-request> is deprecated: use lidar-srv:RandomNumber-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RandomNumber-request>) ostream)
  "Serializes a message object of type '<RandomNumber-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RandomNumber-request>) istream)
  "Deserializes a message object of type '<RandomNumber-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RandomNumber-request>)))
  "Returns string type for a service object of type '<RandomNumber-request>"
  "lidar/RandomNumberRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RandomNumber-request)))
  "Returns string type for a service object of type 'RandomNumber-request"
  "lidar/RandomNumberRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RandomNumber-request>)))
  "Returns md5sum for a message object of type '<RandomNumber-request>"
  "5e093fd141a0ff6a0e66a47360e82cbb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RandomNumber-request)))
  "Returns md5sum for a message object of type 'RandomNumber-request"
  "5e093fd141a0ff6a0e66a47360e82cbb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RandomNumber-request>)))
  "Returns full string definition for message of type '<RandomNumber-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RandomNumber-request)))
  "Returns full string definition for message of type 'RandomNumber-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RandomNumber-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RandomNumber-request>))
  "Converts a ROS message object to a list"
  (cl:list 'RandomNumber-request
))
;//! \htmlinclude RandomNumber-response.msg.html

(cl:defclass <RandomNumber-response> (roslisp-msg-protocol:ros-message)
  ((random_number
    :reader random_number
    :initarg :random_number
    :type cl:integer
    :initform 0))
)

(cl:defclass RandomNumber-response (<RandomNumber-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <RandomNumber-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'RandomNumber-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name lidar-srv:<RandomNumber-response> is deprecated: use lidar-srv:RandomNumber-response instead.")))

(cl:ensure-generic-function 'random_number-val :lambda-list '(m))
(cl:defmethod random_number-val ((m <RandomNumber-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader lidar-srv:random_number-val is deprecated.  Use lidar-srv:random_number instead.")
  (random_number m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <RandomNumber-response>) ostream)
  "Serializes a message object of type '<RandomNumber-response>"
  (cl:let* ((signed (cl:slot-value msg 'random_number)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 18446744073709551616) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) unsigned) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) unsigned) ostream)
    )
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <RandomNumber-response>) istream)
  "Deserializes a message object of type '<RandomNumber-response>"
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) unsigned) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'random_number) (cl:if (cl:< unsigned 9223372036854775808) unsigned (cl:- unsigned 18446744073709551616))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<RandomNumber-response>)))
  "Returns string type for a service object of type '<RandomNumber-response>"
  "lidar/RandomNumberResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RandomNumber-response)))
  "Returns string type for a service object of type 'RandomNumber-response"
  "lidar/RandomNumberResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<RandomNumber-response>)))
  "Returns md5sum for a message object of type '<RandomNumber-response>"
  "5e093fd141a0ff6a0e66a47360e82cbb")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'RandomNumber-response)))
  "Returns md5sum for a message object of type 'RandomNumber-response"
  "5e093fd141a0ff6a0e66a47360e82cbb")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<RandomNumber-response>)))
  "Returns full string definition for message of type '<RandomNumber-response>"
  (cl:format cl:nil "int64 random_number~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'RandomNumber-response)))
  "Returns full string definition for message of type 'RandomNumber-response"
  (cl:format cl:nil "int64 random_number~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <RandomNumber-response>))
  (cl:+ 0
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <RandomNumber-response>))
  "Converts a ROS message object to a list"
  (cl:list 'RandomNumber-response
    (cl:cons ':random_number (random_number msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'RandomNumber)))
  'RandomNumber-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'RandomNumber)))
  'RandomNumber-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'RandomNumber)))
  "Returns string type for a service object of type '<RandomNumber>"
  "lidar/RandomNumber")