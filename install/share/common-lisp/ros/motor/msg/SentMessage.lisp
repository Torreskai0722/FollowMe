; Auto-generated. Do not edit!


(cl:in-package motor-msg)


;//! \htmlinclude SentMessage.msg.html

(cl:defclass <SentMessage> (roslisp-msg-protocol:ros-message)
  ((sender
    :reader sender
    :initarg :sender
    :type cl:string
    :initform "")
   (content
    :reader content
    :initarg :content
    :type cl:string
    :initform ""))
)

(cl:defclass SentMessage (<SentMessage>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <SentMessage>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'SentMessage)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name motor-msg:<SentMessage> is deprecated: use motor-msg:SentMessage instead.")))

(cl:ensure-generic-function 'sender-val :lambda-list '(m))
(cl:defmethod sender-val ((m <SentMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motor-msg:sender-val is deprecated.  Use motor-msg:sender instead.")
  (sender m))

(cl:ensure-generic-function 'content-val :lambda-list '(m))
(cl:defmethod content-val ((m <SentMessage>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader motor-msg:content-val is deprecated.  Use motor-msg:content instead.")
  (content m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <SentMessage>) ostream)
  "Serializes a message object of type '<SentMessage>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'sender))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'sender))
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'content))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'content))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <SentMessage>) istream)
  "Deserializes a message object of type '<SentMessage>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'sender) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'sender) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'content) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'content) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<SentMessage>)))
  "Returns string type for a message object of type '<SentMessage>"
  "motor/SentMessage")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'SentMessage)))
  "Returns string type for a message object of type 'SentMessage"
  "motor/SentMessage")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<SentMessage>)))
  "Returns md5sum for a message object of type '<SentMessage>"
  "b2e1a1fbf660d36f0c4ce4c3ed50a434")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'SentMessage)))
  "Returns md5sum for a message object of type 'SentMessage"
  "b2e1a1fbf660d36f0c4ce4c3ed50a434")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<SentMessage>)))
  "Returns full string definition for message of type '<SentMessage>"
  (cl:format cl:nil "string sender~%string content~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'SentMessage)))
  "Returns full string definition for message of type 'SentMessage"
  (cl:format cl:nil "string sender~%string content~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <SentMessage>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'sender))
     4 (cl:length (cl:slot-value msg 'content))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <SentMessage>))
  "Converts a ROS message object to a list"
  (cl:list 'SentMessage
    (cl:cons ':sender (sender msg))
    (cl:cons ':content (content msg))
))
