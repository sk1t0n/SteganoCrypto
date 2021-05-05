import argparse
import os

import crypto
from stega import hide_text_to_png, reveal_text_from_png


def encrypt(
    password: str, input_file: str, secret_file: str, output_file: str
) -> bool:
    with open(secret_file) as f:
        secret = f.read()
    enc_secret = crypto.encrypt(password, secret).decode('utf-8')

    result = hide_text_to_png(input_file, enc_secret, output_file)
    return result


def decrypt(password: str, input_file: str, output_file: str) -> bool:
    enc_text = reveal_text_from_png(input_file).encode('utf-8')

    secret = crypto.decrypt(password, enc_text)
    with open(output_file, 'w') as f:
        f.write(secret)
    return os.path.exists(output_file)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', type=str, help='password')
    parser.add_argument(
        '-i', type=str,
        help='input image: encrypt - jpg, png, decrypt: png')
    parser.add_argument(
        '-f', type=str, help='text file for encryption', default=None)
    parser.add_argument(
        '-o', type=str,
        help='output file: encrypt - image png, decrypt - text, for example txt')  # noqa
    parser.add_argument('-m', type=int, help='mode: 1 - encrypt, 2 - decrypt')
    args = parser.parse_args()

    password = args.p
    input_file = args.i
    output_file = args.o
    secret_file = args.f
    mode = args.m

    if mode == 1:
        result = encrypt(password, input_file, secret_file, output_file)
        if result:
            print(f'Successful creation the image file {output_file}')
        else:
            print(f'Failed to create the image file {output_file}')
    elif mode == 2:
        result = decrypt(password, input_file, output_file)
        if result:
            print(f'Successful creation the text file {output_file}')
        else:
            print(f'Failed to create the image {output_file}')
    else:
        print('Invalid mode')


if __name__ == '__main__':
    main()
