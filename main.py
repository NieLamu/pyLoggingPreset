import logging
import logging.config
import configparser
import os


# https://www.yinyubo.cn/?p=160
def get_logger(config_name='log', logs_dir='logs', stream=True, name=__name__):
    conf_file = os.path.join(os.path.dirname(__file__), "%s.ini" % config_name)
    logs_path = os.path.join(os.path.dirname(
        __file__), '..', logs_dir)
    if not os.path.exists(logs_path):
        os.makedirs(logs_path)

    conf = configparser.ConfigParser()
    conf.read(conf_file)
    conf.set("handler_rotatingFileHandler", "args",
             "(r'%s', 'midnight', 1, 30, 'utf-8')" % os.path.join(logs_path, 'default.log'))
    conf.set("handler_errorHandler", "args",
             "(r'%s', 'midnight', 1, 30, 'utf-8')" % os.path.join(logs_path, 'error.log'))
    if not stream:
        conf.set("handler_streamHandler", "level", "ERROR")

    logging.config.fileConfig(conf)
    return logging.getLogger(name)


# get_logger(__name__)
