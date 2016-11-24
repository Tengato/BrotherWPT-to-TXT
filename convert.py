import argparse
import os
import sys


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file_dir")
    args = parser.parse_args()

    file_list = os.listdir(args.input_file_dir)

    files_to_convert = [os.path.join(args.input_file_dir, file) for file in file_list if file[-4:].lower() == '.wpt']
    for file_name in files_to_convert:
        input_file_bytes = b''
        with open(file_name, 'rb') as input_file:
            input_file_bytes = input_file.read()

        output_file_path = os.path.splitext(file_name)[0] + '.txt'
        with open(output_file_path, 'w') as output_file:
            for byte in input_file_bytes:
                if byte >= 32 and byte <= 126:
                    output_file.write(chr(byte))
                elif byte == 0:
                    output_file.write(' ')
                elif byte == 2:
                    output_file.write('\n')

if __name__ == '__main__':
    main()
