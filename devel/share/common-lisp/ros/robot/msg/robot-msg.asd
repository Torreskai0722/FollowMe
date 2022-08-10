
(cl:in-package :asdf)

(defsystem "robot-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "SentMessage" :depends-on ("_package_SentMessage"))
    (:file "_package_SentMessage" :depends-on ("_package"))
  ))