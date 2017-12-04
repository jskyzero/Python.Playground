# -*- coding: utf-8 -*-
"""Picture To Ascii picture_to_ascii.py

main part to receive arguements and process pictures then save to output file
"""
from PIL import Image


class PictureToAscii(object):
    """A PictureToAscii class"""

    def __init__(self):
        """initial a PictureToAscii class"""
        self.ascii = list(
            "$@&%B#=-. ")

    def main_func(self, pictures_path, output_dir, ext_name, size):
        """process every picture in picture path list to output dir
        """
        for pic_path in pictures_path:
            data = self.picture_to_ascii(pic_path, size)

            output_path = self.get_output_path(output_dir, pic_path, ext_name)
            self.write_to_file(output_path, data)

    def picture_to_ascii(self, pic_path, size):
        """process picture in pic_path, return ascii data
        if size == None, let size be default size
        """
        pic = Image.open(pic_path)

        width, height = self.default_size(pic.size) if size is None else size
        pic = pic.resize((width, height), Image.NEAREST)
        return "\n".join([
            "".join([self.rgba_to_char(*pic.getpixel((y, x)))
                     for y in xrange(width)])
            for x in xrange(height)])

    def rgb_to_gray(self, red, green, blue):
        """use color's RBG value to calculate a gray value
        """
        return int((19595 * red + 38469 * green + 7472 * blue) >> 16)

    def rgba_to_char(self, red, green, blue, alpha=256):
        """use gray value to select a char in self.ascii
        """
        gray = self.rgb_to_gray(red, green, blue)
        unit = (256.0 + 1) / len(self.ascii)
        return ' ' if alpha == 0 else self.ascii[int(gray / unit)]

    def default_size(self, pic_size):
        """return default size accodinf to pic_size
        """
        width, height = pic_size
        height /= 2
        while width > 100 or height > 50:
            width /= 2
            height /= 2
        return width, height

    def get_output_path(self, output_dir, pic_path, ext_name):
        """output file name will be picture's name
        """
        return output_dir + pic_path.split('/')[-1].split('.')[0] + (
            '.' + ext_name if ext_name else "")

    def write_to_file(self, output_path, data):
        """save date to output_path
        """
        with open(output_path, 'w') as out:
            out.write(data)
