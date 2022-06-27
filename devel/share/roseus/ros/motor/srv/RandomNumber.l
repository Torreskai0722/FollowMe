;; Auto-generated. Do not edit!


(when (boundp 'motor::RandomNumber)
  (if (not (find-package "MOTOR"))
    (make-package "MOTOR"))
  (shadow 'RandomNumber (find-package "MOTOR")))
(unless (find-package "MOTOR::RANDOMNUMBER")
  (make-package "MOTOR::RANDOMNUMBER"))
(unless (find-package "MOTOR::RANDOMNUMBERREQUEST")
  (make-package "MOTOR::RANDOMNUMBERREQUEST"))
(unless (find-package "MOTOR::RANDOMNUMBERRESPONSE")
  (make-package "MOTOR::RANDOMNUMBERRESPONSE"))

(in-package "ROS")





(defclass motor::RandomNumberRequest
  :super ros::object
  :slots ())

(defmethod motor::RandomNumberRequest
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

(defclass motor::RandomNumberResponse
  :super ros::object
  :slots (_random_number ))

(defmethod motor::RandomNumberResponse
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

(defclass motor::RandomNumber
  :super ros::object
  :slots ())

(setf (get motor::RandomNumber :md5sum-) "5e093fd141a0ff6a0e66a47360e82cbb")
(setf (get motor::RandomNumber :datatype-) "motor/RandomNumber")
(setf (get motor::RandomNumber :request) motor::RandomNumberRequest)
(setf (get motor::RandomNumber :response) motor::RandomNumberResponse)

(defmethod motor::RandomNumberRequest
  (:response () (instance motor::RandomNumberResponse :init)))

(setf (get motor::RandomNumberRequest :md5sum-) "5e093fd141a0ff6a0e66a47360e82cbb")
(setf (get motor::RandomNumberRequest :datatype-) "motor/RandomNumberRequest")
(setf (get motor::RandomNumberRequest :definition-)
      "---
int64 random_number

")

(setf (get motor::RandomNumberResponse :md5sum-) "5e093fd141a0ff6a0e66a47360e82cbb")
(setf (get motor::RandomNumberResponse :datatype-) "motor/RandomNumberResponse")
(setf (get motor::RandomNumberResponse :definition-)
      "---
int64 random_number

")



(provide :motor/RandomNumber "5e093fd141a0ff6a0e66a47360e82cbb")


