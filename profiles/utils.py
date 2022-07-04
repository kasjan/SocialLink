import os
import pyqrcode
from SocialLink.settings import MEDIA_ROOT
from django.contrib.sites.models import Site


def qr_code_generator(nick):
    qr = pyqrcode.create(f'{Site.objects.get_current().domain}/{nick}')
    folder = f'{MEDIA_ROOT}/qr_codes'
    if not os.path.exists(folder):
        os.mkdir(folder)
    path = f'qr_codes/{nick}.png'
    file_path = MEDIA_ROOT + '/' + path
    qr.png(f'{file_path}', scale=10)
    return path
