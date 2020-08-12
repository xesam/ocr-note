import json
import os

from aip import AipOcr


class Ocr:
    def __init__(self, cfg_file_path):
        with open(cfg_file_path, 'r') as in_file:
            cfg = json.load(in_file)
            self.app_id = cfg['APP_ID']
            self.api_key = cfg['API_KEY']
            self.secret_key = cfg['SECRET_KEY']
            self.client = AipOcr(self.app_id, self.api_key, self.secret_key)

    def basic(self, image_bytes):
        return self.client.basicGeneral(image_bytes)


ocr = Ocr(os.path.join(os.path.dirname(__file__), 'ocr.config.json'))

if __name__ == '__main__':
    print(ocr.app_id)
    print(ocr.api_key)
    print(ocr.secret_key)
