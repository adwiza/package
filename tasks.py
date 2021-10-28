import celery

app = celery.Celery(
    'example-chain',
    brocker='redis://localhost',
    backend='redis://localhost',
    broker_url='redis://localhost:6379',
    task_routes={'tasks.add': {'queue': 'add'}, 'tasks.divide': {'queue': 'divide'}},

)


@app.task
def add(x, y):
    return x + y


@app.task
def divide(x, y):
    return x / y
