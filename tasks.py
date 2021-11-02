import celery
import random

app = celery.Celery(
    'example-retry',
    brocker='redis://localhost',
    backend='redis://localhost',
    broker_url='redis://localhost:6379',
    # task_routes={'tasks.add': {'queue': 'add'}, 'tasks.divide': {'queue': 'divide'}},

)


class UnluckyException(Exception):
    pass


@app.task(
    bind=True,
    retry_backoff=True,
    retry_kwargs={'max_retries': 3}
)
def multiply_roulette(self, x, y):
    try:
        if random.random() < 1/6:
            raise UnluckyException
        return x / y
    except UnluckyException as exc:
        self.retry(exc=exc)
