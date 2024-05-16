import pyqrcode
import png
from pyqrcode import QRCode

address = 'https://www.goodreads.com/'
url = pyqrcode.create(address)
url.png('goodreads.png', scale=8)

