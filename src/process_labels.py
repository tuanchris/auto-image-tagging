import sys
import os
import argparse
import json
import re

path = '/Users/tuannguyen/Downloads/Canada_photos/resized'
files = os.listdir(path)

def process_label_file(path):
    configs = []
    for line in open(path,'r'):
        configs.append(line)

    file_name_regex = '(?<=resized_)(.*)(?=","anno)'
    labels_regex = '(?<=labels":)(.*)(?=,"note)'

    labels = dict()
    for config in configs:
        try:
            file_name = re.search(file_name_regex,config).group()
            file_labels = re.search(labels_regex,config).group()
            labels[file_name] = eval(file_labels)
        except AttributeError:
            pass

    return labels

config_file = '../data/Photography multi-label classification.json'
lables = process_label_file(config_file)

path = '../data'
categories = ['animal','building','boat','car','day','doc','human','indoor',
    'mountain','night','object','road','tree','water','food','plane','trash']

def create_training_data(source_path, destination_path, labels, categories):
    source_files = os.listdir(source_path)
    destination_files = labels.keys()

    for cat in categories:
        categories_dir = os.path.join(destination_path, 'labeled_data', cat)
        os.makedirs(categories_dir)

    for file in destination_files:
        source_path = os.path.join(source_path, file)

json_file = 'labels.json'

# def process_label_file(json_file):
with open(json_file) as file1:
    lis = []
    for i in file1:
        lis.append(json.loads(i))

lis[0]['annotation']['labels']

train = float(int(80) / 100)
test = float(int(20)  / 100)

folder_names = []
label_to_urls = {}

for i in lis:
    try:
        if i['annotation']['labels'][0] not in folder_names:
            folder_names.append(i['annotation']['labels'][0])
            label_to_urls[i['annotation']['labels'][0]] = [i['content']]
        else:
            label_to_urls[i['annotation']['labels'][0]].append(i['content'])
    except:
        pass
