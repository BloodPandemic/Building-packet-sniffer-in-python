from ctypes import *
import socket
import struct

class IP(Structure):
    _fields_ = [
        ("ihl",             c_ubyte,  4), #4bit unsigned char 
        ("version",         c_ubyte,  4), #4bit unsigned char
        ("tos",             c_ubyte,  8), #1 byte char 
        ("len",             c_ushort, 16), #2 byte unsigned short
        ("id",              c_ushort, 16), #2 byte
        ("offset",          c_ushort, 16),
        ("ttl",             c_ubyte,   8), 
        ("protocol_num",    c_ubyte,   8),
        ("sum",             c_ushort, 16),
        ("src",             c_uint32, 32),
        ("dst",             c_uint32, 32),
    ]
    def __new__(cls, socket_buffer=None):
        return cls.from_buffer_copy(socket_buffer)

    def __init__(self, socket_buffer=None):
        #human readable ip address
        self.src_address = socket.inet_ntoa(struct.pack("<L", self.src))
        self.dst_address = socket.inet_ntoa(struct.pack("<L", self.dst))



