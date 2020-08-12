import datetime
import logging
import re

from ocr import ocr

logging.basicConfig(level=logging.INFO)


def get_words(result):
    if 'words_result' in result:
        return ''.join([item["words"] for item in result['words_result']])
    else:
        return None


def recognize(img_bytes):
    result = ocr.basic(img_bytes)
    words = get_words(result)
    if words:
        logging.info(words)
    else:
        logging.warning('words is None')
    return words


def get_expiration(s):
    rs = re.match(r'\w+\((\d+)\D+(\d+)\D+\)', s)
    exp_year = datetime.date.today().year
    exp_month, exp_day = rs.group(1), rs.group(2)
    return '{}{}{}'.format(exp_year, exp_month, exp_day)


if __name__ == "__main__":
    test_s = '该二维码7天内(8月14日前)有效,重新进入将更新'
    logging.info(get_expiration(test_s))
