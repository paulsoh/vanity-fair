from .partials import *

DEBUG = False

ALLOWED_HOSTS = [
    '*',
]

AWS_ACCESS_KEY_ID = 'AKIAJOFEWCW6KNOTJKDQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'doreee'

STATICFILES_STORAGE = 'vanityfair.storage.S3PipelineCachedStorage'

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'

AWS_S3_CUSTOM_DOMAIN = 'd24o1a0vx62dlb.cloudfront.net'
AWS_S3_URL_PROTOCOL = 'https'

STATIC_URL = "https://d24o1a0vx62dlb.cloudfront.net/"
