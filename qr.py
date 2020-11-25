import pyqrcode
url=pyqrcode.create("www.python.org")
url.png('qrcode.png',scale=8)