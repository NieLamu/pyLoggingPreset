import logging
import logging.config
import os


# https://www.yinyubo.cn/?p=160
def get_logger(config_name='log', name=__name__):
    conf_log = os.path.join(os.path.dirname(__file__), "%s.ini" % config_name)
    print(name, conf_log)
    logging.config.fileConfig(conf_log)
    return logging.getLogger(name)


# get_logger(__name__)
