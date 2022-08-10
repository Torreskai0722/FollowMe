;; Auto-generated. Do not edit!


(when (boundp 'robot::RandomNumber)
  (if (not (find-package "ROBOT"))
    (make-package "ROBOT"))
  (shadow 'RandomNumber (find-package "ROBOT")))
(unless (find-package "ROBOT::RANDOMNUMBER")
  (make-package "ROBOT::RANDOMNUMBER"))
(unless (find-package "ROBOT::RANDOMNUMBERREQUEST")
  (make-package "ROBOT::RANDOMNUMBERREQUEST"))
(unless (find-package "ROBOT::RANDOMNUMBERRESPONSE")
  (make-package "ROBOT::RANDOMNUMBERRESPONSE"))

(in-package "ROS")





(defclass robot::RandomNumberRequest
  :super ros::object
  :slots ())

(defmethod robot::RandomNumberRequest
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass robot::RandomNumberResponse
  :super ros::object
  :slots (_random_number ))

(defmethod robot::RandomNumberResponse
  (:init
   (&key
    ((:random_number __random_number) 0)
    )
   (send-super :init)
   (setq _random_number (round __random_number))
   self)
  (:random_number
   (&optional __random_number)
   (if __random_number (setq _random_number __random_number)) _random_number)
  (:serialization-length
   ()
   (+
    ;; int64 _random_number
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int64 _random_number
#+(or :alpha :irix6 :x86_64)
       (progn (sys::poke _random_number (send s :buffer) (send s :count) :long) (incf (stream-count s) 8))
#-(or :alpha :irix6 :x86_64)
       (cond ((and (class _random_number) (= (length (_random_number . bv)) 2)) ;; bignum
              (write-long (ash (elt (_random_number . bv) 0) 0) s)
              (write-long (ash (elt (_random_number . bv) 1) -1) s))
             ((and (class _random_number) (= (length (_random_number . bv)) 1)) ;; big1
              (write-long (elt (_random_number . bv) 0) s)
              (write-long (if (>= _random_number 0) 0 #xffffffff) s))
             (t                                         ;; integer
              (write-long _random_number s)(write-long (if (>= _random_number 0) 0 #xffffffff) s)))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int64 _random_number
#+(or :alpha :irix6 :x86_64)
      (setf _random_number (prog1 (sys::peek buf ptr- :long) (incf ptr- 8)))
#-(or :alpha :irix6 :x86_64)
      (setf _random_number (let ((b0 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4)))
                  (b1 (prog1 (sys::peek buf ptr- :integer) (incf ptr- 4))))
              (cond ((= b1 -1) b0)
                     ((and (= b1  0)
                           (<= lisp::most-negative-fixnum b0 lisp::most-positive-fixnum))
                      b0)
                    ((= b1  0) (make-instance bignum :size 1 :bv (integer-vector b0)))
                    (t (make-instance bignum :size 2 :bv (integer-vector b0 (ash b1 1)))))))
   ;;
   self)
  )

(defclass robot::RandomNumber
  :super ros::object
  :slots ())

(setf (get robot::RandomNumber :md5sum-) "5e093fd141a0ff6a0e66a47360e82cbb")
(setf (get robot::RandomNumber :datatype-) "robot/RandomNumber")
(setf (get robot::RandomNumber :request) robot::RandomNumberRequest)
(setf (get robot::RandomNumber :response) robot::RandomNumberResponse)

(defmethod robot::RandomNumberRequest
  (:response () (instance robot::RandomNumberResponse :init)))

(setf (get robot::RandomNumberRequest :md5sum-) "5e093fd141a0ff6a0e66a47360e82cbb")
(setf (get robot::RandomNumberRequest :datatype-) "robot/RandomNumberRequest")
(setf (get robot::RandomNumberRequest :definition-)
      "---
int64 random_number

")

(setf (get robot::RandomNumberResponse :md5sum-) "5e093fd141a0ff6a0e66a47360e82cbb")
(setf (get robot::RandomNumberResponse :datatype-) "robot/RandomNumberResponse")
(setf (get robot::RandomNumberResponse :definition-)
      "---
int64 random_number

")



(provide :robot/RandomNumber "5e093fd141a0ff6a0e66a47360e82cbb")


