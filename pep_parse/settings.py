import logging

from pep_parse.constants import BASE_DIR

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'


ROBOTSTXT_OBEY = True


FEEDS = {
    'results/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

LOG_LEVEL = logging.INFO
LOG_STDOUT = True
LOG_DIR = BASE_DIR / 'logs'
LOG_DIR.mkdir(exist_ok=True)
LOG_FILE = BASE_DIR / 'logs/spider.log'
LOG_FORMAT = "%(asctime)s [%(name)s] %(levelname)s: %(message)s"
