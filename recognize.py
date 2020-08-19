import datetime
import logging
import re

from ocr import ocr

logging.basicConfig(level=logging.INFO)


def repair(word):
    word = word.replace('菜乌驿站', '菜鸟驿站')
    word = word.replace('1+1同城生活一', '1+1同城生活—')
    return word


def get_chatroom_name(result):
    if 'words_result' in result:
        return ''.join([item["words"] for item in result['words_result']])
    else:
        return 'error'


def recognize(img_bytes):
    result = ocr.basic(img_bytes)
    chatroom_name = get_chatroom_name(result)
    chatroom_name = repair(chatroom_name)
    if chatroom_name:
        logging.info(chatroom_name)
    else:
        logging.warning('words is None')
    return chatroom_name


def get_expiration(s):
    rs = re.match(r'\w+\((\d+)\D+(\d+)\D+\)', s)
    exp_year = datetime.date.today().year
    exp_month, exp_day = rs.group(1), rs.group(2)
    return '{}{}{}'.format(exp_year, exp_month, exp_day)


if __name__ == "__main__":
    test_name = '1+1同城生活一乐易居菜乌驿站优惠群1.2020826'
    logging.info(repair(test_name))
    test_s = '该二维码7天内(8月14日前)有效,重新进入将更新'
    logging.info(get_expiration(test_s))
