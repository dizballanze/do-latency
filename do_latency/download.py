# -*- coding: utf-8 -*-
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import time


BLOCK_SIZE = 8192


def do_download(url, hook=None):
    """
    Downloads file and returns speed in mbps.
    """
    http_handler = urllib2.urlopen(url)
    file_size = float(http_handler.headers["Content-Length"])
    start_time = time.time()
    status_downloaded = 0
    while True:
        buf = http_handler.read(BLOCK_SIZE)
        if not buf:
            break
        if hook is not None:
            status_downloaded += len(buf)
            progress = (float(status_downloaded) / file_size) * 100
            if progress >= 1:
                hook(int(progress))
                status_downloaded = ((float(progress) - int(progress)) / 100) * file_size
    speed = ((file_size * 8) / (1024 * 1024)) / (time.time() - start_time)
    http_handler.close()
    return "{:06.3f}".format(speed)
