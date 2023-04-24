import os
import soundfile as sf
from opt import parser_opt
from const.path import INPUT_PATH, OUPUT_PATH


def convert_caf_to_wav(input_path, output_path):
    data, samplerate = sf.read(input_path)
    sf.write(output_path, data, samplerate)


def main(args):
    for root, dirs, files in os.walk(args.input_dir):
        for filename in files:
            if filename.endswith('.caf'):
                input_path = os.path.join(root, filename)
                output_path = input_path.replace(args.input_dir, args.output_dir).replace('.caf', '.wav')
                output_dir = os.path.dirname(output_path)

                os.makedirs(output_dir, exist_ok=True)

                print(input_path, output_path)
                convert_caf_to_wav(input_path, output_path)


if __name__ == '__main__':
    default_in = INPUT_PATH
    default_out = OUPUT_PATH
    args = parser_opt(default_in, default_out)
    print(args)
    main(args)
