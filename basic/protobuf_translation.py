# -*- coding: utf-8 -*-
import strip as strip

from pb_file import l1basic_pb2

def protobuf_translation(receive_data):
    quan_data = receive_data[8:]
    pb_data = l1basic_pb2.l1BasicResponse()

    pb_data.ParseFromString(quan_data)
    result = "%s" % pb_data
    return result
