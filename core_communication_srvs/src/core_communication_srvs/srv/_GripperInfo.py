"""autogenerated by genpy from core_communication_srvs/GripperInfoRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GripperInfoRequest(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "core_communication_srvs/GripperInfoRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """


"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GripperInfoRequest, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
"""autogenerated by genpy from core_communication_srvs/GripperInfoResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class GripperInfoResponse(genpy.Message):
  _md5sum = "4483535ab2994ff7413bfbaa2fc66115"
  _type = "core_communication_srvs/GripperInfoResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """
bool isGripperInstalled
float64 minimumOpening
float64 maximumOpening
float64 noMovementTimeout


"""
  __slots__ = ['isGripperInstalled','minimumOpening','maximumOpening','noMovementTimeout']
  _slot_types = ['bool','float64','float64','float64']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       isGripperInstalled,minimumOpening,maximumOpening,noMovementTimeout

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(GripperInfoResponse, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.isGripperInstalled is None:
        self.isGripperInstalled = False
      if self.minimumOpening is None:
        self.minimumOpening = 0.
      if self.maximumOpening is None:
        self.maximumOpening = 0.
      if self.noMovementTimeout is None:
        self.noMovementTimeout = 0.
    else:
      self.isGripperInstalled = False
      self.minimumOpening = 0.
      self.maximumOpening = 0.
      self.noMovementTimeout = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_B3d.pack(_x.isGripperInstalled, _x.minimumOpening, _x.maximumOpening, _x.noMovementTimeout))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 25
      (_x.isGripperInstalled, _x.minimumOpening, _x.maximumOpening, _x.noMovementTimeout,) = _struct_B3d.unpack(str[start:end])
      self.isGripperInstalled = bool(self.isGripperInstalled)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_B3d.pack(_x.isGripperInstalled, _x.minimumOpening, _x.maximumOpening, _x.noMovementTimeout))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 25
      (_x.isGripperInstalled, _x.minimumOpening, _x.maximumOpening, _x.noMovementTimeout,) = _struct_B3d.unpack(str[start:end])
      self.isGripperInstalled = bool(self.isGripperInstalled)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_B3d = struct.Struct("<B3d")
class GripperInfo(object):
  _type          = 'core_communication_srvs/GripperInfo'
  _md5sum = '4483535ab2994ff7413bfbaa2fc66115'
  _request_class  = GripperInfoRequest
  _response_class = GripperInfoResponse