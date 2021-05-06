import os
from typing import Optional

from stegano import lsb


def hide_text_to_png(in_img_path: str, text: str, out_img_path: str) -> bool:
    """Hide text in a png image.

    Args:
        in_img_path (str): the path to the image in which you want to hide the text  # noqa
        text (str): the text you want to hide
        out_img_path (str): the path to the new png image

    Returns:
        bool: the result is a success or failure
    """

    if not os.path.exists(in_img_path) or os.path.isdir(in_img_path):
        print('No image for hiding')
        return False

    secret = lsb.hide(in_img_path, text)
    secret.save(out_img_path)
    return os.path.exists(out_img_path)


def reveal_text_from_png(img_path: str) -> Optional[str]:
    """Reveal text out of a png image.

    Args:
        img_path (str): the path to the image in png format

    Returns:
        str: the encrypted text
    """

    if not os.path.exists(img_path) or os.path.isdir(img_path):
        print('No image for revealing')
        return None

    text = lsb.reveal(img_path)
    return text
