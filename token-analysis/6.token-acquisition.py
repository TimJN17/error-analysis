import os
import sys
import pandas as pd
import numpy as np
from helpers import read_json


def read_file(fname):
    spec_dict = {}
    count = 0
    with open(fname, mode="r+") as f:
        lines = f.readlines()
        for line in lines:
            words = line.strip(' ').split()
            spec_dict[count] = words[7]
            count += 1
        return spec_dict


def find_file(specs, direc_tory):
    os.chdir(direc_tory)
    file_dict = {}
    count = 0
    for spec in specs.values():
        for file in os.listdir():
            if spec in file:
                file_dict[count] = json_helper(file)
        count += 1
    return file_dict


def print_dictionary(directory_, filename, dictionary_object):
    os.chdir(directory_)
    if os.path.exists(filename):
        os.remove(filename)
    final_df = pd.DataFrame(list(dictionary_object.values())[0], dtype=str, columns=['Tokens'])
    for value in list(dictionary_object.values())[1:]:
        df = pd.DataFrame(value, dtype=str, columns=['Tokens__'])
        final_df = pd.concat([final_df, df], axis=1, ignore_index=True)
    np.savetxt(X=final_df, fname=filename, fmt='%s', newline='\n', delimiter='  |  ')
    return -1


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
    print_dictionary(filename="closest-good-specs-array.txt", dictionary_object=final_dictionary,
                     directory_=directory[0:-8])

    # for value in final_dictionary.values():
    #     print(value)

    # Configurations
    # python 6.token-acquisition.py
    # C:\Users\timjn\Documents\Lawrence_Livermore_Internship\NLP_Professional_work_error_analysis_download\error_analysis-main\data\feature-specs\working
    # C:\Users\timjn\Documents\Lawrence_Livermore_Internship\NLP_Professional_work_error_analysis_download\error_analysis-main\data\feature-specs\errors
    # C:\Users\timjn\Documents\Lawrence_Livermore_Internship\NLP_Professional_work_error_analysis_download\error_analysis-main\data\feature-specs\closest-good-specs.txt
