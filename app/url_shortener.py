from baseconv import base62
import binascii


class UrlShortener:
    @staticmethod
    def shorten(url):
        if not url:
            raise ValueError('url is empty')

        seed = binascii.crc32(url.encode('utf8'))
        return base62.encode(seed)
