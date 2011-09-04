# Scrapy settings for linkedIn project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'linkedIn'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['linkedIn.spiders']
NEWSPIDER_MODULE = 'linkedIn.spiders'
DEFAULT_ITEM_CLASS = 'linkedIn.items.LinkedinItem'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)


SCHEDULER_ORDER = 'DFO'
FEED_URI = 'items.json'
FEED_FORMAT = 'json'


ITEM_PIPELINES = ['linkedIn.pipelines.LinkedinPipeline']
