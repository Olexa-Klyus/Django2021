import os.path
from uuid import uuid1


def upload_to(inctance, file: str):
    ext = file.split('.')[-1]
    return os.path.join(inctance.user.email, 'avatars', f'{uuid1()}.{ext}')
