/* Auto-generated by genmsg_cpp for file /home/biorob/rosstacks/core_dev/core_communication_msgs/msg/TrajectoryTargetReceivingAck.msg */
#ifndef CORE_COMMUNICATION_MSGS_MESSAGE_TRAJECTORYTARGETRECEIVINGACK_H
#define CORE_COMMUNICATION_MSGS_MESSAGE_TRAJECTORYTARGETRECEIVINGACK_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"


namespace core_communication_msgs
{
template <class ContainerAllocator>
struct TrajectoryTargetReceivingAck_ {
  typedef TrajectoryTargetReceivingAck_<ContainerAllocator> Type;

  TrajectoryTargetReceivingAck_()
  : received(false)
  , errorCode(0)
  , description()
  {
  }

  TrajectoryTargetReceivingAck_(const ContainerAllocator& _alloc)
  : received(false)
  , errorCode(0)
  , description(_alloc)
  {
  }

  typedef uint8_t _received_type;
  uint8_t received;

  typedef uint32_t _errorCode_type;
  uint32_t errorCode;

  typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _description_type;
  std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  description;


  typedef boost::shared_ptr< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct TrajectoryTargetReceivingAck
typedef  ::core_communication_msgs::TrajectoryTargetReceivingAck_<std::allocator<void> > TrajectoryTargetReceivingAck;

typedef boost::shared_ptr< ::core_communication_msgs::TrajectoryTargetReceivingAck> TrajectoryTargetReceivingAckPtr;
typedef boost::shared_ptr< ::core_communication_msgs::TrajectoryTargetReceivingAck const> TrajectoryTargetReceivingAckConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace core_communication_msgs

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> > {
  static const char* value() 
  {
    return "d2e809347de3b1ad80491fdae482c5f5";
  }

  static const char* value(const  ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0xd2e809347de3b1adULL;
  static const uint64_t static_value2 = 0x80491fdae482c5f5ULL;
};

template<class ContainerAllocator>
struct DataType< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> > {
  static const char* value() 
  {
    return "core_communication_msgs/TrajectoryTargetReceivingAck";
  }

  static const char* value(const  ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> > {
  static const char* value() 
  {
    return "bool received\n\
uint32 errorCode\n\
string description\n\
\n\
";
  }

  static const char* value(const  ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> &) { return value(); } 
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.received);
    stream.next(m.errorCode);
    stream.next(m.description);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct TrajectoryTargetReceivingAck_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::core_communication_msgs::TrajectoryTargetReceivingAck_<ContainerAllocator> & v) 
  {
    s << indent << "received: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.received);
    s << indent << "errorCode: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.errorCode);
    s << indent << "description: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.description);
  }
};


} // namespace message_operations
} // namespace ros

#endif // CORE_COMMUNICATION_MSGS_MESSAGE_TRAJECTORYTARGETRECEIVINGACK_H

