import qrcode as qr
from PIL import Image

qr = qr.QRCode(version=1,
            error_correction=qr.constants.ERROR_CORRECT_H,
            box_size=10,border=10)
qr.add_data("https://youtu.be/nXiDrxZXd6E?si=2GRXuFl6Hkbp4tV-")
qr.make(fit=True)
img = qr.make_image(fit_color="red",back_color='white')
img.save('Imran_khan_sexologist_channel.png')
