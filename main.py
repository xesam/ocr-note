import glob
import logging
import os
import time
from sys import argv

from crop import crop
from recognize import recognize, get_expiration

logging.basicConfig(level=logging.INFO)


def single(file_path, dst_dir):
    logging.info('start {}'.format(file_path))
    name_bytes, time_bytes, crop_region = crop(file_path)
    time.sleep(1)
    chat_name = recognize(name_bytes)
    time.sleep(1)
    qr_time = recognize(time_bytes)
    exp_time = get_expiration(qr_time)
    ext_name = os.path.splitext(file_path)[1]
    dst_file_name = "{}.{}{}".format(chat_name, exp_time, ext_name)
    dst_file_path = os.path.join(os.path.abspath(dst_dir), dst_file_name)
    logging.info(dst_file_name)
    crop_region.save(dst_file_path)
    logging.info('finish {}'.format(file_path))


def run(src_dir, dst_dir):
    abs_src_dir = os.path.abspath(src_dir)
    all_files = glob.glob("{}/*".format(abs_src_dir))
    for f_name in all_files:
        single(f_name, dst_dir)


if __name__ == "__main__":
    script, argv_src_dir, argv_dst_dir, *rest = argv
    run(argv_src_dir, argv_dst_dir)
