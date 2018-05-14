import os
from PIL import Image

def read_single_picture(ori_file):
    """
    read the useful data from a picture
    return the binary
    """
    img = Image.open(ori_file)
    data = img.tobytes()
    # get the length of file
    str_len = ""
    for i in range(4):
        str_len += data[i]

    hex_len = str_len.encode('hex_codec')
    int_len = int(hex_len, 16)
    file_data = data[4:4 + int_len]
    return file_data

def combine(pic_dir, out_file):
    """
    input a dir which contains pictures
    combine the pictures to original file
    """
    file_names = [name for name in os.listdir(pic_dir)]
    num_files = len(file_names)
    # here we need to regenreate the file names by order
    file_names = ['{}/{}.png'.format(pic_dir, i) for i in range(num_files)]
    res_binary = []
    for file_name in file_names:
        if len(res_binary) == 0:
            res_binary = read_single_picture(file_name)
        else:
            res_binary += read_single_picture(file_name)
    out = open(out_file, 'wb')
    out.write(res_binary)
    out.close()



if __name__ == "__main__":
    pic_dir = "./pieces/"
    save_file = "save.mp4"
    combine(pic_dir, save_file)
