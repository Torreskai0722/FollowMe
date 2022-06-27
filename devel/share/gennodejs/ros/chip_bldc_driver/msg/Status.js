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

class Status {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.header = null;
      this.motor_operational_status = null;
      this.battery_voltage = null;
      this.mcu_temperature = null;
      this.motor_command = null;
      this.motor_pid_error = null;
    }
    else {
      if (initObj.hasOwnProperty('header')) {
        this.header = initObj.header
      }
      else {
        this.header = new std_msgs.msg.Header();
      }
      if (initObj.hasOwnProperty('motor_operational_status')) {
        this.motor_operational_status = initObj.motor_operational_status
      }
      else {
        this.motor_operational_status = 0;
      }
      if (initObj.hasOwnProperty('battery_voltage')) {
        this.battery_voltage = initObj.battery_voltage
      }
      else {
        this.battery_voltage = 0.0;
      }
      if (initObj.hasOwnProperty('mcu_temperature')) {
        this.mcu_temperature = initObj.mcu_temperature
      }
      else {
        this.mcu_temperature = 0;
      }
      if (initObj.hasOwnProperty('motor_command')) {
        this.motor_command = initObj.motor_command
      }
      else {
        this.motor_command = 0;
      }
      if (initObj.hasOwnProperty('motor_pid_error')) {
        this.motor_pid_error = initObj.motor_pid_error
      }
      else {
        this.motor_pid_error = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Status
    // Serialize message field [header]
    bufferOffset = std_msgs.msg.Header.serialize(obj.header, buffer, bufferOffset);
    // Serialize message field [motor_operational_status]
    bufferOffset = _serializer.int16(obj.motor_operational_status, buffer, bufferOffset);
    // Serialize message field [battery_voltage]
    bufferOffset = _serializer.float32(obj.battery_voltage, buffer, bufferOffset);
    // Serialize message field [mcu_temperature]
    bufferOffset = _serializer.int16(obj.mcu_temperature, buffer, bufferOffset);
    // Serialize message field [motor_command]
    bufferOffset = _serializer.int16(obj.motor_command, buffer, bufferOffset);
    // Serialize message field [motor_pid_error]
    bufferOffset = _serializer.int32(obj.motor_pid_error, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Status
    let len;
    let data = new Status(null);
    // Deserialize message field [header]
    data.header = std_msgs.msg.Header.deserialize(buffer, bufferOffset);
    // Deserialize message field [motor_operational_status]
    data.motor_operational_status = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [battery_voltage]
    data.battery_voltage = _deserializer.float32(buffer, bufferOffset);
    // Deserialize message field [mcu_temperature]
    data.mcu_temperature = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [motor_command]
    data.motor_command = _deserializer.int16(buffer, bufferOffset);
    // Deserialize message field [motor_pid_error]
    data.motor_pid_error = _deserializer.int32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += std_msgs.msg.Header.getMessageSize(object.header);
    return length + 14;
  }

  static datatype() {
    // Returns string type for a message object
    return 'chip_bldc_driver/Status';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '10df97be388ae1578fee4bc1bad6eaac';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # 5Hz status message
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
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Status(null);
    if (msg.header !== undefined) {
      resolved.header = std_msgs.msg.Header.Resolve(msg.header)
    }
    else {
      resolved.header = new std_msgs.msg.Header()
    }

    if (msg.motor_operational_status !== undefined) {
      resolved.motor_operational_status = msg.motor_operational_status;
    }
    else {
      resolved.motor_operational_status = 0
    }

    if (msg.battery_voltage !== undefined) {
      resolved.battery_voltage = msg.battery_voltage;
    }
    else {
      resolved.battery_voltage = 0.0
    }

    if (msg.mcu_temperature !== undefined) {
      resolved.mcu_temperature = msg.mcu_temperature;
    }
    else {
      resolved.mcu_temperature = 0
    }

    if (msg.motor_command !== undefined) {
      resolved.motor_command = msg.motor_command;
    }
    else {
      resolved.motor_command = 0
    }

    if (msg.motor_pid_error !== undefined) {
      resolved.motor_pid_error = msg.motor_pid_error;
    }
    else {
      resolved.motor_pid_error = 0
    }

    return resolved;
    }
};

module.exports = Status;
