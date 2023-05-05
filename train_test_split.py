import os
from typing import List, Tuple
from opt import parser_opt
import random
import shutil

def main(args):
    train_test_split(
        input_dir = args.input,
        output_dir = args.output,
        train_size = args.train_size,
        test_size = args.test_size,
        shuffle = args.shuffle,
        random_state = args.random_state,
        stratify = args.stratify
    )


        
def train_test_split(
        input_dir: str,
        output_dir: str,
        train_size: float,
        test_size: float,
        shuffle: bool,
        random_state: int,
        stratify: bool
        ) -> None:
    
    dataset_depth = 2
    random.seed(random_state)
    
    for root, dirs, files in os.walk(input_dir):
        if len(dirs)==0 and len(files)>0:
            if shuffle == True:
                random.shuffle(files)

            print(f"[{root}]: {len(files)} files")

            num_train = int(len(files) * train_size)
            train_files: List[str] = files[:num_train]
            test_files: List[str] = files[num_train:]
            dict_files = {'train': train_files, 'test': test_files}

            for phaze, each_files in dict_files.items():
                for filename in each_files:
                    if filename.endswith('.txt'):

                        input_path = os.path.join(root, filename)
                        # output_root = root.replace(input_dir, output_dir)
                        dir_names = root.split(os.path.sep)
                        dir_names[dataset_depth] += ('_' + phaze) # dir -> dir_train or dir_test
                        output_root = os.path.join(*dir_names)
                        output_root = output_root.replace(input_dir, output_dir) # ./in -> ./out
                        output_path = os.path.join(output_root, filename)

                        os.makedirs(output_root, exist_ok=True)
                        shutil.copy(input_path, output_path)



if "__main__" == __name__:
    args = parser_opt()
    main(args)
    