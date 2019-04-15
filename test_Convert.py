import numpy as np
from PIL import Image
#from skimage import io
import struct
#import blowfish as bf  #for TD

ori = "defect_22_Reflected_Ref_Proc.td"
tmp = "tmpR.im1"

# Read .im1 file
def read_im1(path):
    file = open(path, 'rb')
    buff = file.read()
    five, four, three, two, one = buff[-5], buff[-4], buff[-3], buff[-2], buff[-1]
    width = five + four * pow(2, one)
    height = three + two * pow(2, one)
    print(width,height)
    data = np.zeros(height * width, dtype=np.uint8)
    for i in range(len(buff) - 5):
        data[i] = buff[i]
    data = np.reshape(data, (height, width))
    img = Image.fromarray(data)
    img.show()
    img.save('1.png')
    file.close()
    return img, data

# Read .dat file
def read_dat(path):
    file = open(path, 'r')
    buff = file.readline()[1:]                  # First line: height and width info
    height, width = int(buff.split(' ')[0]), int(buff.split(' ')[1])
    buff = file.readline()                      # Second line: no info used in this function
    buff = file.read()                          # Third line: data info
    buff = buff.split(' ')
    data = np.zeros(height * width, dtype=np.float32)
    for i in range(len(buff) - 1):
        data[i] = float(buff[i]) * 255
    data = np.reshape(data, (width, height))
    img = Image.fromarray(data)
    img = img.transpose(Image.FLIP_TOP_BOTTOM)  # Flip image due to different axis
    img.show()
    file.close()
    return img

# Read .td file
def read_td(path):
    file = open(path, 'rb')
    buff = file.read()
    width = buff[5]                                 # Image width
    height = buff[11]                               # Image height
    image = buff[36:]                               # Image data begins at 36
    key = b'Rev_Rdc'                                # Encryption key
    cipher = bf.Cipher(key)
    data = np.zeros(height * width, dtype=np.uint8)
    i = 0
    while i < len(image):
        crypted = image[i : i + 8]                  # Read 8 bytes
        decrypted = cipher.decrypt_block(crypted)   # Decryption
        for j in range(8):
            data[i + j] = decrypted[j]
        i += 8
    data = np.reshape(data, (height, width))
    img = Image.fromarray(data)
    img.show()
    img.save('2.png')
    file.close()
    return img, data

# Read .png file
def read_png(filename):
    img = io.imread(filename)
    if len(img.shape) == 3:
        img = img[:,:,0]
    img = Image.fromarray(img)
    img.show()
    return img

# Write .im1 file
def write_im1(img, width, height, depth, path):
    binary = []
    for i in range(height):
        for j in range(width):
            binary.append(img.getpixel((j, i)))
    five, four, three, two, one = width, 0, height, 0, depth
    while five >= pow(2, one):
        five -= pow(2, one)
        four += 1
    while three >= pow(2, one):
        three -= pow(2, one)
        two += 1
    binary.append(five)        # The last fifth item is width
    binary.append(four)            # The last fourth item is 0
    binary.append(three)       # The last third item is height
    binary.append(two)            # The last second item is 0
    binary.append(one)        # The last one item is depth
    fw = open(path, 'wb')       # Open tmp.im1 for binary written
    for b in binary:
        byte = struct.pack("B", b)
        fw.write(byte)
    fw.close()

def main():
 #   img, td = read_td('defect_10_Reflected_Ref_Proc.td')
 #   img, im1 = read_im1(r'D:\Work\RDC\Training\Nextchip_ADC_tuning\bigfov\defect_45_Defect.im1')
    img, im1 = read_im1(r'D:\Work\RDC\Training\Nextchip_ADC_tuning\bigfov\defect_45_Transmitted_Ref.im1')



if __name__ == '__main__':
    main()

