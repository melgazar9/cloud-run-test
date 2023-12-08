import os
from waitress import serve
from apscheduler.schedulers.background import BackgroundScheduler

from flask import Flask
from datetime import datetime

from logger import *

app = Flask(__name__)

TEXT = os.getenv('HELLO_TEXT')

@app.route('/')
def hello_world():
    log()
    logging.info(TEXT)
    return 'Hello World.'

@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    with app.app_context():
        return make_response("Server is running...", 200)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    scheduler = BackgroundScheduler(job_defaults={'max_instances': 2})
    cron = {"year": "*", "month": "*", "day": "*", "week": "*", "day_of_week": "*", "hour": "17", "minute": "0", "second": "0"}

    scheduler.add_job(hello_world, trigger='cron', **cron, jitter=30)

    scheduler.start()

    serve(app, host='0.0.0.0', port=8888, threads=2)
