// Auto-generated. Do not edit!

// (in-package robot.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class RandomNumberRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
    }
    else {
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RandomNumberRequest
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RandomNumberRequest
    let len;
    let data = new RandomNumberRequest(null);
    return data;
  }

  static getMessageSize(object) {
    return 0;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot/RandomNumberRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RandomNumberRequest(null);
    return resolved;
    }
};

class RandomNumberResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.random_number = null;
    }
    else {
      if (initObj.hasOwnProperty('random_number')) {
        this.random_number = initObj.random_number
      }
      else {
        this.random_number = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type RandomNumberResponse
    // Serialize message field [random_number]
    bufferOffset = _serializer.int64(obj.random_number, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type RandomNumberResponse
    let len;
    let data = new RandomNumberResponse(null);
    // Deserialize message field [random_number]
    data.random_number = _deserializer.int64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 8;
  }

  static datatype() {
    // Returns string type for a service object
    return 'robot/RandomNumberResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '5e093fd141a0ff6a0e66a47360e82cbb';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    int64 random_number
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new RandomNumberResponse(null);
    if (msg.random_number !== undefined) {
      resolved.random_number = msg.random_number;
    }
    else {
      resolved.random_number = 0
    }

    return resolved;
    }
};

module.exports = {
  Request: RandomNumberRequest,
  Response: RandomNumberResponse,
  md5sum() { return '5e093fd141a0ff6a0e66a47360e82cbb'; },
  datatype() { return 'robot/RandomNumber'; }
};
