import os
import pyqrcode
from PIL import Image


class QR_Gen(object):

    def __init__(self, text):
        self.qr_image = pyqrcode.create(text)

        file_name = "QR Code Result.png"
        save_path = os.path.join(os.path.expanduser("~"), "Desktop")

        name = os.path.join(save_path, file_name)

        self.qr_image.png(name, scale=10)

        image = Image.open(name)
        image = image.resize((400, 400), Image.Resampling.LANCZOS)
        image.show()


if __name__ == "__main__":
    QR_Gen(input("[QR] Enter text or link: "))