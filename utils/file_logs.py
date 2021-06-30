import logging
from logging.handlers import TimedRotatingFileHandler
import re, os


def setup_log(log_path, log_name):
    if not os.path.exists(log_path):
        os.makedirs(log_path)

    log_name = os.path.join(log_path, log_name)
    logger = logging.getLogger(log_name)
    logger.setLevel(level=logging.INFO)

    file_handler = TimedRotatingFileHandler(
        filename=log_name, when="D",
        interval=1, backupCount=30, encoding='utf-8')
    file_handler.suffix = "%Y-%m-%d_%H:%M:%S.log"
    # extMatch是编译好正则表达式，用于匹配日志文件名后缀
    # 需要注意的是suffix和extMatch一定要匹配的上，如果不匹配，过期日志不会被删除。
    file_handler.extMatch = re.compile(r"^\d{4}-\d{2}-\d{2}_\d{2}:\d{2}:\d{2}.log$")
    file_handler.setFormatter(
        logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s'))

    # 日志输出到幕幕
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s[line:%(lineno)d] - %(message)s'))

    logger.addHandler(file_handler)
    logger.addHandler(console)

    return logger
