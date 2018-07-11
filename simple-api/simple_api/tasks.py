# coding: utf-8

import celery


@celery.shared_task()
def sleep(message, seconds=1):
    import time
    time.sleep(seconds)
    print(message)
    return seconds
