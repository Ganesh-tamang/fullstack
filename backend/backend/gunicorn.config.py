"""
Gunicorn WSGI server cofiguration
"""

import os
from pathlib import Path

from dotenv import load_dotenv

ENV_FILE_PATH = Path(__file__).parent.parent / ".env"
load_dotenv(ENV_FILE_PATH)
STAGE = os.getenv("STAGE")

worker_class = "gthread"
workers = int(os.environ["GUNICORN_WORKERS"])
threads = int(os.environ["GUNICORN_THREADS"])
capture_output = True
wsgi_app = "core.wsgi:application"

if STAGE == "local":
    reload = True
    accesslog = "-"
    errorlog = "-"
else:
    accesslog = os.environ["GUNICORN_ACCESS_LOG"]
    errorlog = os.environ["GUNICORN_ERROR_LOG"]
