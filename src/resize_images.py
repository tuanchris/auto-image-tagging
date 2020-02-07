import os
import cv2
import numpy as np
from tqdm import tqdm
import sys
import argparse

def resize_img(input_path, file_name, output_path, size = 266):
    '''
    Downsize an image for faster processing

        - input_path: folders that contains images
        - file_name: name of image
        - output_path: output folder path
        - size: max width/height to downsize
    '''
    full_input_path = os.path.join(input_path, file_name)
    img = cv2.imread(full_input_path)

    max_dim = max(img.shape)
    scale_percent = 266/max_dim

    width = int(img.shape[1] * scale_percent)
    height = int(img.shape[0] * scale_percent)

    img = cv2.resize(img, (width, height),interpolation = cv2.INTER_AREA)

    full_output_path = os.path.join(output_path,file_name)
    cv2.imwrite(full_output_path, img)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Downsize all images in a folder')
    parser.add_argument('input_path', help='Path to folder containing images')
    parser.add_argument('output_path', help='Path to output folder')
    parser.add_argument('-s','--size', default='266', help='Maxium width/height size')

    args = parser.parse_args()

    files = os.listdir(args.input_path)

    for file in tqdm(files):
        try:
            resize_img(args.input_path, file, args.output_path, args.size)
            print(f'Converted file {file}')

        except:
            pass
            print(f'Cannot convert file {file}')
