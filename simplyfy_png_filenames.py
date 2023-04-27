import os
import sys
import argparse
from opt import parser_opt
import shutil


def main(args):
    # 引数から対象フォルダパスを取得
    input_dir = args.input
    output_dir = args.output
    
    # 対象フォルダ内のPNGファイルを再帰的に検索
    count = 0
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(".png"):
                # 新しいファイル名を生成
                old_path = os.path.join(root, file)
                new_filename = f"{file.split('_')[0]}_{str(count).zfill(2)}.png"
                new_path = os.path.join(output_dir, os.path.relpath(root, input_dir), new_filename)
                count+=1

                output_subdir = os.path.join(output_dir, os.path.relpath(root, input_dir))
                if not os.path.exists(output_subdir):
                    os.makedirs(output_subdir)
                
                shutil.copyfile(old_path, new_path)
                # ファイル名を変更
                
                # ログ出力
                print(f"{old_path} -> {new_path}")

if __name__ == "__main__":
    # コマンドライン引数をパース
    args = parser_opt()    
    # プログラムのメイン処理を実行
    main(args)
