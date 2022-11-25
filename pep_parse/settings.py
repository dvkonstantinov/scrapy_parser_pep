BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = 'pep_parse.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

FEED_EXPORTERS = {
    'csv': 'pep_parse.exporters.CustomCsvItemExporter',
}
PEP_FILENAME = ('results/pep_%(time)s.csv')

FEEDS = {
    PEP_FILENAME: {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    }
}
