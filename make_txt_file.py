import os

PATH = "./dataset"



def create_files(path):
    max_depth = 0
    for root, dirs, files in os.walk(path):
        depth = root.count(os.path.sep)
        max_depth = max(max_depth, depth)
    for root, dirs, files in os.walk(path):
        depth = root.count(os.path.sep)
        if depth == max_depth:
            dirname = os.path.basename(root)
            for i in range(1, 101):
                filename = os.path.join(root, f"{dirname}_{i}.txt")
                open(filename, 'w').close()

# 以下のように実行します
create_files("/path/to/directory")


# 以下のように実行します
if "__main__" == __name__:
    create_files(PATH)
