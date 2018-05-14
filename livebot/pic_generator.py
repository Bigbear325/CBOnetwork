''' this code will get in a file, read it, devide it into
    pieces and covert it using base64, then generate multi qrcode
'''

from PIL import Image
import os, sys
import math
import base64
import pyqrcode
import subprocess
from tqdm import *
import shutil


CHUNK_SIZE = 1464 


def file2pics(ori_file, save_file):
    """
    this function will accept a file name, convert it to a picture
    store this picture to the save_file
    params: input file with path, save file with path
    return: none
    """
    pic = open(ori_file, 'rb')
    bi = pic.read()
    bi_len = len(bi)
    hex_len = "%0*x" % (8, bi_len)
    str_len = ""
    for i in range(0, 8, 2):
        cur = int(hex_len[i:i + 2], 16)
        str_len += chr(cur)
    bi = str_len + bi
    width = int(math.sqrt(bi_len))
    # add something to the end
    end_str = ""
    for i in range(bi_len):
        end_str += 'a'
    bi = bi + end_str
    img = Image.frombytes('L', (width, bi_len / width + 1), bi)
    img.save(save_file)


def get_qrcode(source_file):
    """
    this function will take a file, cut into pieces return a list of generated pictures
    param: the name of source file
    return: the genrated list of qr codes
    """
    binary_list = []
    qr_code_list = []
    counter = 0

    with open(source_file, 'rb') as infile:
        while True:
            #read as chunk
            file_chunk = infile.read(CHUNK_SIZE)
            encoded_chunk = base64.b64encode(file_chunk)
            binary_list.append(encoded_chunk)
            if not file_chunk:
                break

        for file_chunk in tqdm(binary_list):
            tmp = pyqrcode.create(encoded_chunk, error='L', version=32)
            qr_code_list.append(tmp)

    for i in qr_code_list:
        i.show();

def cut_file(source_file, aim_path, chunk_size):
    """
    this function will take a source file, cut it into pieces with chunk size
    store them to the aim path
    return a list of cut names
    """
    ori_bin = open(source_file, 'rb')
    chunk_list = []
    while True:
        cur_bin = ori_bin.read(chunk_size)
        if not cur_bin:
            break
        chunk_list.append(cur_bin)
    cur_chunk_id = 0
    cut_name_list = []
    for chunk in chunk_list:
        cur_file_name = '{}/{}.part'.format(aim_path, cur_chunk_id)
        cut_name_list.append(cur_file_name)
        f = open(cur_file_name, 'wb')
        f.write(chunk)
        f.close()
        cur_chunk_id += 1
    return cut_name_list

def check_dir(path):
    """
    this function takes a path and check it
    if does not exist, create a dir
    """
    directory = os.path.dirname(path + '/')
    try:
        os.stat(directory)
    except:
        os.mkdir(directory) 
        print ('Path {} does not exist, created'.format(path))


def big_file2picture(source_file, save_dic, chunk_size = 65535):
    """
    for big file with name source file, cut it into chunks
    save the cut file to save dic
    """
    tmp_dic = './tmpdic/'
    check_dir(tmp_dic)
    check_dir(save_dic)

    name_list = cut_file(source_file, tmp_dic, chunk_size)
    aim_file_id = 0
    for file_name in name_list:
        file2pics(file_name, '{}/{}.png'.format(save_dic, aim_file_id))
        aim_file_id += 1
    shutil.rmtree(tmp_dic, ignore_errors=False, onerror=None)


if __name__ == '__main__':
    testfile = "./testfile.mp4"
    aim_path = './pieces'
    big_file2picture(testfile, aim_path)

