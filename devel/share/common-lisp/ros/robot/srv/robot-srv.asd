
(cl:in-package :asdf)

(defsystem "robot-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "RandomNumber" :depends-on ("_package_RandomNumber"))
    (:file "_package_RandomNumber" :depends-on ("_package"))
  ))