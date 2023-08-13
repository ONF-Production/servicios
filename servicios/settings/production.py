from .base import *


DATABASES = {
    'default': dj_database_url.config(
        # Feel free to alter this value to suit your needs.
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}