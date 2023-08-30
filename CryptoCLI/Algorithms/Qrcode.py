from PIL import Image
import qrcode
import os.path

def encode(text, show=True):
    IMG = qrcode.make(text)
    IMG.save("qrcode.jpg")
    if show:
        image = Image.open(os.path.abspath("qrcode.jpg"))
        image.show()

