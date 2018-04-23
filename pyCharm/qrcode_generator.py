''' this code will get in a file, read it, devide it into
    pieces and covert it using base64, then generate multi qrcode
'''

from PIL import Image
import os, sys
import math
import base64
import pyqrcode

CHUNK_SIZE = 1000




# This file is for dev purposes. Each line is one piece of the message being sent individually
# chunk_file = open('chunkfile.txt', 'wb+')

# with open(image_file, 'rb') as infile:
#     while True:
#         # Read 430byte chunks of the image
#         chunk = infile.read(CHUNK_SIZE)
#         if not chunk: break
#
#         # Do what you want with each chunk (in dev, write line to file)
#         chunk_file.write(chunk)
#
# chunk_file.close()


def get_qrcode(source_file):

    binary_list = []
    qr_code_list = []
    counter = 0

    with open(source_file, 'rb') as infile:
        while True:
            #read as chunk
            file_chunk = infile.read(CHUNK_SIZE)
            if not file_chunk: break

            encoded_chunk = base64.b64encode(file_chunk)

            tmp = pyqrcode.create(encoded_chunk, error='L', version=27)
            tmp.show()
            qr_code_list.append(tmp)
            print('chunk', counter)
            counter = counter + 1


    for i in qr_code_list:
        i.show();

    # print(file)
    # print(file_binary)



    # print(len(encoded))
    #
    # leng = len(encoded)
    #
    # if(leng > 1000):
    #     print('oversize')


    # loop = leng/1000



    # for i in range(0, loop + 1):
    #     binary_list[i] = encoded[i * 1000 :(i + 1) * 1000]
    #     qr_code_list[i] = pyqrcode.create(binary_list[i], error='L', version=27)
    #     qr_code_list[i].show()
    #
    # encoded = encoded[:1250]
    #
    #
    #
    #
    # qr_code = pyqrcode.create(encoded, error='L', version=25)
    #
    # qr_code.show()

    # print(encoded)

# def gen_pic(ori_file, save_file):
#     pic = open(ori_file, 'rb')
#     bi = pic.read()
#
#     #get the length of bi
#     bi_len = len(bi)
#
#     # convert to hex str
#     hex_len = "%0*x" % (8, bi_len)
#
#     # convert hex to str
#     str_len = ""
#     for i in range(0, 8, 2):
#         cur = int(hex_len[i:i + 2], 16)
#         str_len += chr(cur)
#
#     bi = str_len + bi
#
#     # pic size 720p Resolution: 1280x720
#     #width = int(math.sqrt(bi_len))
#     width = 426
#     # add something to the end
#     end_str = ""
#     for i in range(bi_len):
#         end_str += 'a'
#
#     bi = bi + end_str
#
#     height = 240
#     #img = Image.frombytes('L', (width, bi_len / width + 1), bi)
#     img = Image.frombytes('L', (width, height), bi)
#     img.save(save_file)

testfile = "/Users/lzhmbp/Documents/GitHub/CBOnetwork/testfile.mp4"
# save_file_dir = "/Users/lzhmbp/Documents/GitHub/CBOnetwork/twitpy/client/out"

# files = os.listdir(testfile)

get_qrcode(testfile)

# file_names = []
# for f in files:
#     file_names.append(f)

# num_files = len(file_names)
# num_finished = 0
# for f in file_names:
#     num_finished += 1
#     gen_pic(ori_file_dir + '/' + f, save_file_dir + '/' + f + '.png')
#     print str(num_finished) + " out of " + str(num_files) + " finished."
#
#
