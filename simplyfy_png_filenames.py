import os
import sys
import argparse
from opt import parser_opt
import shutil


def main(args):
    input_dir = args.input
    output_dir = args.output
    
    count = 0
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".png"):
                old_path = os.path.join(root, file)
                new_filename = f"{file.split('_')[0]}_{str(count).zfill(2)}.png"
                new_path = os.path.join(output_dir, os.path.relpath(root, input_dir), new_filename)
                count+=1

                output_subdir = os.path.join(output_dir, os.path.relpath(root, input_dir))
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)
                
                shutil.copyfile(old_path, new_path)
                
                print(f"{old_path} -> {new_path}")

if __name__ == "__main__":
    args = parser_opt()    
    main(args)
