from baseconv import base62
import binascii


class UrlShortener:
    @staticmethod
    def shorten(url):
        if not url:
            raise ValueError('url is empty')

        # Generate a checksum
        seed = binascii.crc32(url.encode('utf8'))
        # Base62 encode it in order to get the url id
        return base62.encode(seed)
