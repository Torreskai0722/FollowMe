// Generated by gencpp from file test/RandomNumberResponse.msg
// DO NOT EDIT!


#ifndef TEST_MESSAGE_RANDOMNUMBERRESPONSE_H
#define TEST_MESSAGE_RANDOMNUMBERRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace test
{
template <class ContainerAllocator>
struct RandomNumberResponse_
{
  typedef RandomNumberResponse_<ContainerAllocator> Type;

  RandomNumberResponse_()
    : random_number(0)  {
    }
  RandomNumberResponse_(const ContainerAllocator& _alloc)
    : random_number(0)  {
  (void)_alloc;
    }



   typedef int64_t _random_number_type;
  _random_number_type random_number;





  typedef boost::shared_ptr< ::test::RandomNumberResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::test::RandomNumberResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RandomNumberResponse_

typedef ::test::RandomNumberResponse_<std::allocator<void> > RandomNumberResponse;

typedef boost::shared_ptr< ::test::RandomNumberResponse > RandomNumberResponsePtr;
typedef boost::shared_ptr< ::test::RandomNumberResponse const> RandomNumberResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::test::RandomNumberResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::test::RandomNumberResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::test::RandomNumberResponse_<ContainerAllocator1> & lhs, const ::test::RandomNumberResponse_<ContainerAllocator2> & rhs)
{
  return lhs.random_number == rhs.random_number;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::test::RandomNumberResponse_<ContainerAllocator1> & lhs, const ::test::RandomNumberResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace test

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::test::RandomNumberResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::test::RandomNumberResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test::RandomNumberResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::test::RandomNumberResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test::RandomNumberResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::test::RandomNumberResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::test::RandomNumberResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5e093fd141a0ff6a0e66a47360e82cbb";
  }

  static const char* value(const ::test::RandomNumberResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5e093fd141a0ff6aULL;
  static const uint64_t static_value2 = 0x0e66a47360e82cbbULL;
};

template<class ContainerAllocator>
struct DataType< ::test::RandomNumberResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "test/RandomNumberResponse";
  }

  static const char* value(const ::test::RandomNumberResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::test::RandomNumberResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "int64 random_number\n"
"\n"
;
  }

  static const char* value(const ::test::RandomNumberResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::test::RandomNumberResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.random_number);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RandomNumberResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::test::RandomNumberResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::test::RandomNumberResponse_<ContainerAllocator>& v)
  {
    s << indent << "random_number: ";
    Printer<int64_t>::stream(s, indent + "  ", v.random_number);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TEST_MESSAGE_RANDOMNUMBERRESPONSE_H
