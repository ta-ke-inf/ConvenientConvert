import argparse
from const.path import INPUT_PATH, OUPUT_PATH

def parser_opt() :
    parser = argparse.ArgumentParser()
    parser.add_argument('input_dir', default=INPUT_PATH, type=str, help='input directory')
    parser.add_argument('output_dir', default=OUPUT_PATH, type=str, help='output directory')
    args = parser.parse_args()

    return args