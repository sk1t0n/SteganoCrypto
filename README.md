# SteganoCrypto

Adding text file encryption for [Stegano](https://github.com/cedricbonhomme/Stegano) steganography library.

## Install

```sh
python3 -m pip install -r requirements.txt
```

## Usage

```sh
# Help
python3 main.py -h

# Encrypt
python main.py -p password -i input_img.jpg -f secret.txt -o output_img.png -m 1

# Decrypt
python main.py -p password -i input_img.png -o output_text.txt -m 2
```
