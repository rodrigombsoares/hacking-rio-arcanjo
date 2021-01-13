import os
import qrcode
from datetime import datetime
from django.conf import settings


def get_qrcode(session_id):
    cwd = os.getcwd()
    
    url = 'http://34.68.179.212:8000/{}'.format(session_id)
    qr = qrcode.make(url)
    
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    file_name = '{}'.format(str(timestamp).replace('.',''))
    qr_path = os.path.join(settings.BASE_DIR, 'qrcode', file_name)
    
    qr.save(qr_path)
    url = 'http://34.68.179.212:8080/media/{}'.format(file_name)

    return url