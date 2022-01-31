from celery import shared_task


@shared_task
def divide(x, y):
    import time
    time.sleep(7)
    return x / y

