# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
from .application import *

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(PROJECT_BASE_DIR, 'dist', 'static')

MEDIA_ROOT = os.path.join(PROJECT_BASE_DIR, 'dist', 'media')

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)


PIPELINE = {
    'STYLESHEETS': {
        'vendor': {
            'source_filenames': (
              'vanityfair/css/bootstrap.min.css',
            ),
            'output_filename': 'css/vendor.css',
        },
        'main': {
            'source_filenames': (
              'vanityfair/css/application.sass',
            ),
            'output_filename': 'css/vanityfair.min.css',
        },
    },

    'JAVASCRIPT': {
        'vendor': {
            'source_filenames': (
              'vanityfair/js/jquery-1.12.2.min.js',
              'vanityfair/js/bootstrap.min.js',
            ),
            'output_filename': 'js/vendor.js',
        },
        'main': {
            'source_filenames': (
              'vanityfair/js/detail.js',
              'vanityfair/js/newvideo.js',
            ),
            'output_filename': 'js/main.js',
        },
    },

    'COMPILERS': {
        'pipeline.compilers.sass.SASSCompiler',
    }
}

PIPELINE['JS_COMPRESSOR'] = 'pipeline.compressors.NoopCompressor'
