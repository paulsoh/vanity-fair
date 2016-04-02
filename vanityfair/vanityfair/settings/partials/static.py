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
        'hello': {
            'source_filenames': (
              'vanityfair/css/*.css',
            ),
            'output_filename': 'css/hello.css',
            'extra_context': {
                'media': 'screen,projection',
            },
        },
    },
    'JAVASCRIPT': {
        'hello_js': {
            'source_filenames': (
              'vanityfair/js/*.js',
            ),
            'output_filename': 'js/hello.js',
        }
    }
}
