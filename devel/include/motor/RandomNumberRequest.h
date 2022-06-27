// Generated by gencpp from file motor/RandomNumberRequest.msg
// DO NOT EDIT!


#ifndef MOTOR_MESSAGE_RANDOMNUMBERREQUEST_H
#define MOTOR_MESSAGE_RANDOMNUMBERREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace motor
{
template <class ContainerAllocator>
struct RandomNumberRequest_
{
  typedef RandomNumberRequest_<ContainerAllocator> Type;

  RandomNumberRequest_()
    {
    }
  RandomNumberRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::motor::RandomNumberRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::motor::RandomNumberRequest_<ContainerAllocator> const> ConstPtr;

}; // struct RandomNumberRequest_

typedef ::motor::RandomNumberRequest_<std::allocator<void> > RandomNumberRequest;

typedef boost::shared_ptr< ::motor::RandomNumberRequest > RandomNumberRequestPtr;
typedef boost::shared_ptr< ::motor::RandomNumberRequest const> RandomNumberRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::motor::RandomNumberRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::motor::RandomNumberRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace motor

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::motor::RandomNumberRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::motor::RandomNumberRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::motor::RandomNumberRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::motor::RandomNumberRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::motor::RandomNumberRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::motor::RandomNumberRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::motor::RandomNumberRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::motor::RandomNumberRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::motor::RandomNumberRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "motor/RandomNumberRequest";
  }

  static const char* value(const ::motor::RandomNumberRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::motor::RandomNumberRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::motor::RandomNumberRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::motor::RandomNumberRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RandomNumberRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::motor::RandomNumberRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::motor::RandomNumberRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // MOTOR_MESSAGE_RANDOMNUMBERREQUEST_H
