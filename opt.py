import argparse
from const.path import INPUT_PATH, OUPUT_PATH

def parser_opt() :
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default=INPUT_PATH, type=str, help='Path to input directory or file')
    parser.add_argument('-o', '--output', default=OUPUT_PATH, type=str, help='Path to output directory or file')
    args = parser.parse_args()

    return args