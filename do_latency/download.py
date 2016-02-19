# -*- coding: utf-8 -*-
import urllib2
import time


BLOCK_SIZE = 8192


def do_download(url, hook=None):
    """
    Downloads file and returns speed in mbps.
    """
    http_handler = urllib2.urlopen(url)
    headers = http_handler.info()
    file_size = int(headers.getheaders("Content-Length")[0])
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
    return "{:.3f}".format(speed)
