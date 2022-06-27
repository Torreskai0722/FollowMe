// Auto-generated. Do not edit!

// (in-package chip_bldc_driver.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let std_msgs = _finder('std_msgs');

//-----------------------------------------------------------

class Feedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.feedback_counter = null;
      this.motor_encoder_counter = null;
      this.motor_rpm_feedback = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('feedback_counter')) {
        this.feedback_counter = initObj.feedback_counter
      }
      else {
        this.feedback_counter = 0;
      }
      if (initObj.hasOwnProperty('motor_encoder_counter')) {
        this.motor_encoder_counter = initObj.motor_encoder_counter
      }
      else {
        this.motor_encoder_counter = 0;
      }
      if (initObj.hasOwnProperty('motor_rpm_feedback')) {
        this.motor_rpm_feedback = initObj.motor_rpm_feedback
      }
      else {
        this.motor_rpm_feedback = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Feedback
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [feedback_counter]
    bufferOffset = _serializer.int32(obj.feedback_counter, buffer, bufferOffset);
    // Serialize message field [motor_encoder_counter]
    bufferOffset = _serializer.int32(obj.motor_encoder_counter, buffer, bufferOffset);
    // Serialize message field [motor_rpm_feedback]
    bufferOffset = _serializer.int32(obj.motor_rpm_feedback, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Feedback
    let len;
    let data = new Feedback(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [feedback_counter]
    data.feedback_counter = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [motor_encoder_counter]
    data.motor_encoder_counter = _deserializer.int32(buffer, bufferOffset);
    // Deserialize message field [motor_rpm_feedback]
    data.motor_rpm_feedback = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 12;
  }

  static datatype() {
    // Returns string type for a message object
    return 'chip_bldc_driver/Feedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3cd2728375779c5e385ddf941da8bc30';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # 20Hz feedback message
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Feedback(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.feedback_counter !== undefined) {
      resolved.feedback_counter = msg.feedback_counter;
    }
    else {
      resolved.feedback_counter = 0
    }

    if (msg.motor_encoder_counter !== undefined) {
      resolved.motor_encoder_counter = msg.motor_encoder_counter;
    }
    else {
      resolved.motor_encoder_counter = 0
    }

    if (msg.motor_rpm_feedback !== undefined) {
      resolved.motor_rpm_feedback = msg.motor_rpm_feedback;
    }
    else {
      resolved.motor_rpm_feedback = 0
    }

    return resolved;
    }
};

module.exports = Feedback;
