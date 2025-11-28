import qrcode as qr
from PIL import Image
qr1=qr.QRCode(version=1,error_correction=qr.constants.ERROR_CORRECT_H,box_size=5,border=3)
qr1.add_data("https://github.com/jainroshan785-blip/python-oops-")
qr1.make(fit=True)
img=qr1.make_image(fill_color="black",back_color="aqua")
img.save("git repo of python oops.png")