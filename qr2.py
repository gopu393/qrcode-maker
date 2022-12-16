import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_M,
                             box_size=80, border=4)
qr.add_data("https://www.youtube.com/channel/UCdL10FHIt5hM9pRzHTE4eRQ")
qr.make(fit=True)
img=qr.make_image(fill_color="pink",black_color="blue")
img.save("youtube channel.png")
