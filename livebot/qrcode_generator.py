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


CHUNK_SIZE = 1464 


def gen_pic(ori_file, save_file):
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


#==================================================
# this function will take a file, cut into pices
# return a list of generated pictures
# @param: the name of source file
# return: the genrated list of qr codes
#==================================================
def get_qrcode(source_file):

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

if __name__ == '__main__':
    testfile = "./testfile.mp4"
    savefile = './save.png'
    #get_qrcode(testfile)
    gen_pic(testfile, savefile)
