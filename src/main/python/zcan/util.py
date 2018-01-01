import logging

import datetime


def get_logger(suffix=None):
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%d.%m.%Y %H:%M:%S')

    if suffix:
        return logging.getLogger('zcan.{0}'.format(suffix))
    else:
        return logging.getLogger('zcan')


def get_current_time():
    return datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')