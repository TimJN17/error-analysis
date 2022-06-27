import os
import sys
import pandas as pd
import numpy as np
from helpers import read_json


def read_file(file_name):
    spec_dict = {}
    count = 0
    with open(file_name, mode="r+") as f:
        lines = f.readlines()
        for line in lines:
            words = line.strip(' ').split()
            spec_dict[count] = words[7]
            count += 1
        return spec_dict


def find_file(specs, directory):
    os.chdir(directory)
    file_dict = {}
    count = 0
    # print(f"the number of files in this directory is: {len(os.listdir(os.getcwd()))}")
    for spec in specs.values():
        for file in os.listdir():
            if spec in file:
                file_dict[count] = json_helper(file)
        count += 1
    return file_dict


def json_helper(file):
    content = read_json(file)
    return content


if __name__ == "__main__":

    # Variables
    directory = sys.argv[1]
    file_name = sys.argv[2]

    # Function calls
    print(f'The directory is: {directory[-10:]}')
    dict_of_specs = read_file(file_name)
    final_dictionary = find_file(dict_of_specs, directory)
    for value in final_dictionary.values():
        print(value)

    # Configurations
    # python 6.token-acquisition.py
    # C:\Users\timjn\Documents\Lawrence_Livermore_Internship\NLP_Professional_work_error_analysis_download\error_analysis-main\data\feature-specs\working
    # C:\Users\timjn\Documents\Lawrence_Livermore_Internship\NLP_Professional_work_error_analysis_download\error_analysis-main\data\feature-specs\errors
    # C:\Users\timjn\Documents\Lawrence_Livermore_Internship\NLP_Professional_work_error_analysis_download\error_analysis-main\data\feature-specs\closest-good-specs.txt
