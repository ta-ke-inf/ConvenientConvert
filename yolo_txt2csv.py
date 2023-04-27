import os
import csv
from natsort import natsorted
from opt import parser_opt
from typing import List, Tuple


def get_file_name_list(path: str):
    file_name_list = os.listdir(path) 
    return file_name_list

def reset_csv_file(path: str) -> None:
    with open(path, 'w') as f:
        pass

def read_txt_file(base_path: str, filename: str):
    """
    Args:
        base_path (string): base folder path of text files
        filename (string): text file name

    Returns:
        rows (list): each line of rows
    """
    with open(os.path.join(base_path, filename), 'r', newline='') as f:
        rows: List[str] = f.readlines()
        return rows

def write_csv_file(path: str, text_list: List[str]) -> None:
    with open(path, 'a', newline='') as f:
        writer = csv.writer(f, lineterminator="")
        writer.writerow(text_list)
    

def main(args):

    labels_path: str = args.input
    csv_path: str = args.output

    file_name_list = get_file_name_list(labels_path)
    file_name_list = natsorted(file_name_list)

    reset_csv_file(csv_path)

    # write first row to csv
    csv_head = ['filename', 'normal', 'abnormal', 'gray\r\n']
    write_csv_file(csv_path, csv_head)

    for file_name in file_name_list:
        output = [0] * len(csv_head)
        output[0] = file_name
        output.append('\r\n')

        rows: List[str] = read_txt_file(labels_path, file_name)
        for row in rows:
            text_list = row.split(' ')
            confidence_score: str = text_list[5].replace('\r\n', '')
            classId: str = text_list[0]
            
            if   classId == '0':
                output[1] = confidence_score
            
            elif classId == '1':
                output[2] = confidence_score
            
            elif classId == '2':
                output[3] = confidence_score
        
        write_csv_file(csv_path, output)



if "__main__" == __name__:
    args = parser_opt()
    main(args)