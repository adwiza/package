import celery

app = celery.Celery(
    'examples_tasks',
    brocker='redis://localhost',
    backend='redis://localhost',
    broker_url='redis://localhost:6379',
)


@app.task
def add(x, y):
    return x + y
