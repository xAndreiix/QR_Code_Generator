# Import QRcode from pyqrcode
import pyqrcode
import png
from pyqrcode import QRCode

def generate_qr_code(data: str, svg_filename="myqrcode.svg", png_filename="myqrcode.png"):
    if not data:
        raise ValueError("Input string for QR code generation cannot be empty.")

    url = pyqrcode.create(data)
    url.svg(svg_filename, scale=8)
    url.png(png_filename, scale=6)

    return True
