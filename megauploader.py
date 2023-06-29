from mega import Mega

import os


def upload_file(path: str):
    client = Mega()
    client.login(os.getenv("MEGA_USER"), os.getenv("MEGA_PASSWORD"))

    folder = client.find('sejda')
    client.upload(path, folder[0])
    