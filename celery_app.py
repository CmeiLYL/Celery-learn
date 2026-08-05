import celery

app = celery.Celery(
    'celery_learn',
    broker="redis://127.0.0.1:6379/0",
    backend="redis://127.0.0.1:6379/1",
    include=['customer'],
)
