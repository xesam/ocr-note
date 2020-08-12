from io import BytesIO

from PIL import Image

SRC_WIDTH = 1080
SRC_HEIGHT = 1958

DST_WIDTH = 950
DST_HEIGHT = 1260

CROP_BOX = ((SRC_WIDTH - DST_WIDTH) / 2,
            (SRC_HEIGHT - DST_HEIGHT) / 2,
            (SRC_WIDTH - DST_WIDTH) / 2 + DST_WIDTH,
            (SRC_HEIGHT - DST_HEIGHT) / 2 + DST_HEIGHT)
NAME_BOX = (300, 362, 1080, 610)
TIME_BOX = (0, 1478, 1080, 1610)


def to_bytes(region):
    output_buffer = BytesIO()
    region.save(output_buffer, format='PNG')
    return output_buffer.getvalue()


def crop(file_path):
    im = Image.open(file_path).convert('RGB')

    name_region = im.crop(NAME_BOX)
    name_bytes = to_bytes(name_region)

    time_region = im.crop(TIME_BOX)
    time_bytes = to_bytes(time_region)

    crop_region = im.crop(CROP_BOX)

    return name_bytes, time_bytes, crop_region


if __name__ == "__main__":
    (name, ti, crop_img) = crop('./images/5.jpg')
