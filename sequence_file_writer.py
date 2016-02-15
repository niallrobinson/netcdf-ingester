from tempfile import SpooledTemporaryFile

from hadoop.io.SequenceFile import CompressionType
from hadoop.io import BytesWritable, Text
from hadoop.io import SequenceFile

import iris


def write_seq_file(file_name, data_dict):
    writer = SequenceFile.createWriter(file_name, Text, BytesWritable)
    for key, value in data_dict.iteritems():
        print key, ", " ,
        key_writer = Text()
        key_writer.set(key)
        
        value_writer = BytesWritable()
        iris.save(value, "temp.nc")
        with open("temp.nc", "rb") as f:
            value_writer.set(f.read())
        writer.append(key_writer, value_writer)
    writer.close()



if __name__ == '__main__':
    pass