import os
import sys
import pandas
import time
import numpy

__all__ = ['df2file', 'file2df']


data_root = 'storage\\'


def df2file(df, file_path):
    create_file(file_path)
    create_file(file_path+'.dtypes')

    if df.index.name is None:
        df.to_csv(data_root+file_path, index=False)
        with open(data_root+file_path+'.dtypes', 'w') as file:
            file.write('$RangeIndex$')
            type_dict = df.dtypes.to_dict()
            for name in type_dict:
                file.write(','+name)
                file.write(','+type_dict[name].name)
    else:
        df.to_csv(data_root+file_path)
        with open(data_root+file_path+'.dtypes', 'w') as file:
            file.write(df.index.name+',')
            file.write(df.index.dtype.name)
            type_dict = df.dtypes.to_dict()
            for name in type_dict:
                file.write(','+name)
                file.write(','+type_dict[name].name)

    create_timestamp(file_path)


def file2df(file_path, update_time=-1):
    if not check_file(file_path, update_time):
        return None

    if not check_file(file_path+'.dtypes'):
        return None

    dtypes = {}
    with open(data_root+file_path+'.dtypes', 'r') as file:
        type_list = file.read().split(',')
        type_len = len(type_list)
        if type_len % 2 != 0:
            for i in range(int(type_len/2)):
                dtypes[type_list[2*i+1]] = numpy.dtype(type_list[2*i+2])
            return pandas.read_csv('file:\\' + os.path.abspath(data_root+file_path), dtype=dtypes)
        else:
            for i in range(int(type_len/2)):
                dtypes[type_list[2*i]] = numpy.dtype(type_list[2*i+1])
            return pandas.read_csv('file:\\' + os.path.abspath(data_root+file_path), dtype=dtypes).set_index(type_list[0])

def create_file(file_path):
    os.makedirs(os.path.dirname(data_root+file_path), exist_ok=True)
    open(data_root+file_path, 'w')


def check_file(file_path, update_time=-1):
    if not os.path.isfile(data_root+file_path):
        return False
    if not os.access(data_root+file_path, os.R_OK | os.W_OK):
        return False
    if update_time >= 0 and not check_timestamp(file_path, update_time):
        return False
    return True


def create_timestamp(file_path):
    create_file(file_path+'.timestamp')
    with open(data_root+file_path+'.timestamp', 'w') as file:
        file.write(str(int(time.time())))


def check_timestamp(file_path, update_time=-1):
    if not check_file(file_path):
        return False
    if update_time >= 0:
        if not check_file(file_path+'.timestamp'):
            return False
        with open(data_root+file_path+'.timestamp', 'r') as file:
            if int(file.read())+update_time < int(time.time()):
                return False
    return True
