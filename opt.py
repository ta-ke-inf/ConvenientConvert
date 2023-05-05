import argparse
from const.path import INPUT_PATH, OUPUT_PATH

def parser_opt() :
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', default=INPUT_PATH, type=str, help='Path to input directory or file')
    parser.add_argument('-o', '--output', default=OUPUT_PATH, type=str, help='Path to output directory or file')
    parser.add_argument('--train_size', default=0.7, type=float, help='train data rate')
    parser.add_argument('--test_size', default=0.3, type=float, help='test data rate')
    parser.add_argument('--shuffle', default=True, type=bool, help='Are you shuffle dataset?')
    parser.add_argument('--random_state', default=0, type=int, help='What is randam seed? default = 0')
    parser.add_argument('--stratify', default=True, type=bool, help='Are you stratify each labels?')
    args = parser.parse_args()

    return args