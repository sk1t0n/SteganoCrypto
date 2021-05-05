import os
from typing import Optional

from stegano import lsb


def hide_text_to_png(in_img_path: str, text: str, out_img_path: str) -> bool:
    """Скрывает текст в изображении в формате png.

    Args:
        in_img_path (str): путь к изображению, в котором нужно скрыть текст
        text (str): текст который нужно скрыть
        out_img_path (str): путь к новому изображению в формате png
    """

    if not os.path.exists(in_img_path) or os.path.isdir(in_img_path):
        print('Hide text: image not found')
        return False

    secret = lsb.hide(in_img_path, text)
    secret.save(out_img_path)
    return os.path.exists(out_img_path)


def reveal_text_from_png(img_path: str) -> Optional[str]:
    """Достаёт текст из изображения в формате png.

    Args:
        img_path (str): путь к изображению в формате png

    Returns:
        str: текст
    """

    if not os.path.exists(img_path) or os.path.isdir(img_path):
        print('Reveal text: image not found')
        return None

    text = lsb.reveal(img_path)
    return text
