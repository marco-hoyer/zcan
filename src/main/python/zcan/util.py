import logging


def get_logger(suffix=None):
    logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%d.%m.%Y %H:%M:%S')

    if suffix:
        return logging.getLogger('zcan.{0}'.format(suffix))
    else:
        return logging.getLogger('zcan')
