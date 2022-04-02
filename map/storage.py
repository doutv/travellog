from io import BytesIO
from django.core.files.storage import Storage
from django.conf import settings
from django.utils.deconstruct import deconstructible
import requests
from django.core.files import File

import logging
logger = logging.getLogger(__name__)


@deconstructible
class SmmsStorage(Storage):
    # https://sm.ms/
    def __init__(self):
        self.option = settings.CUSTOM_STORAGE_OPTIONS

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        files = {'smfile': (name, File(content, name))}
        headers = {'Authorization': self.option["token"]}
        upload_url = self.option["base_url"] + '/upload'
        resp = requests.post(upload_url, files=files, headers=headers)
        if resp.status_code != requests.codes.ok:
            logger.error(
                f"Image Upload Failed: {resp.status_code}-{resp.content}")
            return
        if (resp.json()["success"] == True):
            filename = resp.json()['data']['url']  # url as name
        elif (resp.json()["code"] == "image_repeated"):
            filename = resp.json()['images']
        else:
            logger.error(f"Image Upload Failed: {resp.json()}")
        return filename

    def url(self, name):
        return name

    def delete(self, name):
        pass

    def exists(self, name):
        return False

    def listdir(self, path):
        pass

    def size(self, name):
        pass
