import os
import soundfile as sf
from opt import parser_opt


def convert_caf_to_wav(input_path, output_path):
    data, samplerate = sf.read(input_path)
    sf.write(output_path, data, samplerate)


def main(args):
    input_dir = args.input
    output_dir = args.output
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if filename.endswith('.caf'):
                input_path = os.path.join(root, filename)
                output_path = input_path.replace(input_dir, output_dir).replace('.caf', '.wav')
                output_dir = os.path.dirname(output_path)

                os.makedirs(output_dir, exist_ok=True)

                convert_caf_to_wav(input_path, output_path)


if __name__ == '__main__':
    args = parser_opt()
    main(args)
