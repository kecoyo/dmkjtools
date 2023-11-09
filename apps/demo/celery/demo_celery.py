from celery import Celery

app = Celery("wedo", broker="redis://localhost")


@app.task
def hello():
    return "hello world"
