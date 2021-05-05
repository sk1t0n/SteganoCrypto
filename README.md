# stegano_crypto

Добавление шифрования текстовых файлов для библиотеки стеганографии Stegano.

## Install

```sh
pipenv install
```

## Usage

```sh
# Help
python main.py -h

# Encrypt
python main.py -p password -i input_img.jpg -f secret.txt -o output_img.png -m 1

# Descrypt
python main.py -p password -i input_img.png -o output_text.txt -m 2
```
