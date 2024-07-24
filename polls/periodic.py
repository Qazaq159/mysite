from .celery import app


@app.task
def task_one():
    print('one done!')


@app.task
def task_two():
    print('two done!')


@app.task
def task_three():
    print('thr done!')


@app.task
def task_four():
    print('fou done!')


@app.task
def task_five():
    print('fiv done!')


@app.task
def task_six():
    print('six done!')
